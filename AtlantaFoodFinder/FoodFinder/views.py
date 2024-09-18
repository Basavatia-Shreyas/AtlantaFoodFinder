from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

from .templates.forms import CreateUserForm

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Food Finder home page.")

def login(request):
    return render(request, "FoodFinder/login.html")

@csrf_protect
def create_account(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {"form" : form}
    return render(request, "FoodFinder/create_account.html", context)

def restaurant(request):
    return render(request, "FoodFinder/restaurant.html")

def favorites(request):
    return render(request, "FoodFinder/favorites.html")
