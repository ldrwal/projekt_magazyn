from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from .models import Item, StockItem, StockLocation


# Create your views here.
@login_required(login_url="/account/signin/")
def index(request):
    return render(request, "index.html", {})


def signup(request):
    if request.method == "POST":
        if request.POST.get("pwd1") == request.POST.get("pwd2"):
            print(request.POST.get("pwd1"))
            user = User.objects.create(
                username=request.POST.get("username")
            )
            user.set_password(request.POST.get("pwd1"))
            user.save()
            return redirect("/account/signin/")
        else:
            return redirect("/account/signup/")
    return render(request, "signup.html", {})


def signin(request):
    if request.method == "POST":
        pass
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect("/dashboard/")
        else:
            messages.error(request, "Username or password error!")
            return redirect("/account/signin/")
    return render(request, "login.html", {})


def logout_view(request):
    logout(request)
    return redirect("/account/signin/")


@login_required(login_url="/account/signin/")
def dashboard(request):
    return render(request, "dashboard.html", {})


@csrf_exempt
@login_required(login_url="/account/signin/")
def products(request):
    return render(request, "product.html", {})


@csrf_exempt
def create_item(request):
    data = dict()
    if request.method == "GET":
        default_location = StockLocation.objects.all()
        data['html'] = render_to_string('modules/tables_item.html', {"default_location": default_location})
    else:
        print(request.FILES)
        Item.objects.create(
            name=request.POST["name"],
            description=request.POST["description"],
            keywords=request.POST["description"],
            default_location=StockLocation.objects.get(id=request.POST["StockLocation"]),
            producer=request.POST["producer"],
            product_series=request.POST["product_series"],
            manufacturer_index=request.POST["manufacturer_index"],
        )
        item_lists = Item.objects.all()
        data['html'] = render_to_string('modules/tables_item.html', {"items": item_lists})
    return JsonResponse(data)


@csrf_exempt
def item_list(request):
    item_lists = Item.objects.all()
    context = {'items': item_lists}
    return render(request, "inventory/tables_item.html", context)