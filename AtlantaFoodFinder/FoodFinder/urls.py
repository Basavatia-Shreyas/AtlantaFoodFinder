from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("createaccount/", views.create_account, name="create account"),
    path("home/", views.index, name="index"),
    path("favorites/", views.favorites, name="favorites"),
    path("restaurant/", views.restaurant, name="restaurant"),
]