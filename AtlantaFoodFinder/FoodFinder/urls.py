from django.urls import path
from FoodFinder.views import ResetPasswordView

from . import views

urlpatterns = [
    path("", views.loginPage, name="login"),
    path("createaccount/", views.create_account, name="create account"),
    path("home/", views.index, name="index"),
    path("favorites/", views.favorites, name="favorites"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("logout/", views.logoutUser, name="logout"),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

]