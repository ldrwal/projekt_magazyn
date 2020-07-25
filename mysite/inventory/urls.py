from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("account/signup/", views.signup, name="signup"),
	path("account/signin/", views.signin, name="signin"),
	path("account/logout/", views.logout_view, name="logout"),
	path("dashboard/", views.dashboard, name="dashboard"),
	path("stock_items/", views.stock_item_list, name="stock-items"),
	path("items/", views.items, name="item"),
	path("items/list/", views.item_list, name="item-list"),
	path("item/create/", views.create_item, name="create-item"),
	# path("item/<id>/edit/", views.edit_item, name="edit-item"),
	# path("item/<id>/remove/", views.remove_item, name="item_delete"),
]