from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("account/signup/", views.signup, name="signup"),
	path("account/signin/", views.signin, name="signin"),
	path("account/logout/", views.logout_view, name="logout"),
	path("dashboard/", views.dashboard, name="dashboard"),
	path("items/", views.item_list, name="items"),
	path("stock_items/", views.stock_item_list, name="stock-items"),
	# path("item/list/", views.item_list, name="item-list"),
	# path("item/create/", views.create_item, name="create-item"),
]