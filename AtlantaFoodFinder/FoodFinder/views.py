import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

import json
import requests

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import googlemaps
map_client = googlemaps.Client(api_key)

from .templates.forms import CreateUserForm

# Create your views here.
@csrf_protect
def index(request):
    find_place = map_client.find_place("Blue India", 'textquery')
    place_id = find_place["candidates"][0]["place_id"]
    response = map_client.place(place_id)

    if response["status"] == "OK":
        print('Successful search!')
        print(response)  # Print the JSON response from the API
        context = response
        #return JsonResponse({'status': 'success', 'data': response})
    else:
        print(f"Error: {response['status']}")
        print(response)
        context = response
        #return JsonResponse({'status': 'error', 'message': response}, status=response['status'])

    return render(request, "FoodFinder/home.html", context=context)

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
