from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.loginPage, name="login"),
    path("createaccount/", views.create_account, name="create account"),
    path("home/", views.index, name="index"),
    path("favorites/", views.favorites, name="favorites"),
    path("restaurant/", views.restaurant, name="restaurant"),
    path("logout/", views.logoutUser, name="logout"),
    path('api/toggle-favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('api/get-favorites/', views.get_favorites, name='get_favorites'),
]