from django.shortcuts import render, get_object_or_404
from .models import Restaurant  # Assuming you have a Restaurant model

# View for the main page
def index(request):
    # You could pass all restaurant data to the index for display
    restaurants = Restaurant.objects.all()
    return render(request, 'index.html', {'restaurants': restaurants})

# View for restaurant details
def restaurant_detail(request, restaurant_id):
    # Get the restaurant or return a 404 if it doesn't exist
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})

# View for login
def login_view(request):
    return render(request, 'login.html')

# View for favorites
def favorites_view(request):
    return render(request, 'favorites.html')

# View for account creation
def create_account_view(request):
    return render(request, 'createAccount.html')

