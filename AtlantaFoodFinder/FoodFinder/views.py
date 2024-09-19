from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .templates.forms import CreateUserForm


# Create your views here.
def index(request):
    return render(request, "FoodFinder/home.html")

@csrf_protect
def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Username or password is incorrect")

    context = {}
    return render(request, "FoodFinder/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@csrf_protect
def create_account(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
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

@login_required(login_url="login")
def favorites(request):
    return render(request, "FoodFinder/favorites.html")
