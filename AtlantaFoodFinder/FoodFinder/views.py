from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Food Finder home page.")

def login(request):
    return render(request, "FoodFinder/login.html")

def create_account(request):
    return render(request, "FoodFinder/create_account.html")

def restaurant(request):
    return render(request, "FoodFinder/restaurant.html")

def favorites(request):
    return render(request, "FoodFinder/favorites.html")
