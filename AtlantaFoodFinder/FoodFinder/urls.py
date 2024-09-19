from django.urls import path
from . import views

urlpatterns = [
    # Main index/home page
    path('', views.index, name='index'),

    # Restaurant detail page, dynamically generated for each restaurant
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),

    # Additional routes (e.g., for login, favorites, etc.)
    path('login/', views.login_view, name='login'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('create-account/', views.create_account_view, name='create_account'),
]
