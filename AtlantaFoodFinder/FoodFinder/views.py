# const position = { lat: parseFloat('{{ current_location.location.lat }}'), lng: parseFloat('{{ current_loc.location.lng }}') };
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
from django.urls import reverse

from urllib.parse import urlencode

import googlemaps
map_client = googlemaps.Client(api_key)

from .templates.forms import CreateUserForm

# Create your views here.
@csrf_protect
def index(request):
    try:
        current_loc = map_client.geolocate(consider_ip=True)
        response = map_client.places_nearby(location=current_loc['location'], radius=500, type="restaurant")
    except:
        current_loc = {'location': {'lat': 33.7707008, 'lng': -84.3874304}, 'accuracy': 1050.952656998642}
        response = {"Error" : "Couldn't load nearby restaurants"}
    for index, restaurant in enumerate(response['results']):
        try:
            photo_reference = restaurant["photos"][0]["photo_reference"]
            link = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
            response['results'][index]["photo_link"] = link
            response['results'][index].pop("photos", None)
        except:
            pass

    if response["status"] == "OK":
        #print('Successful search!')
        print(current_loc)
        context = {"response": response['results'], "current_location": current_loc, "google_maps_api_key": api_key}
    else:
        print(f"Error: {response['status']}")
        context = response

    if request.method == "POST":
        base_url = reverse('restaurant')
        place_id = request.POST.get("place")
        query_string =  urlencode({'place': place_id})
        url = '{}?{}'.format(base_url, query_string)
        return redirect(url)

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

            favoriteCuisine = request.POST.get("cuisine")
            print(favoriteCuisine)
            if form.is_valid():
                form.save()
                return redirect("index")
            else:
                messages.info(request, "Please enter valid values for all the fields")

        context = {"form" : form}
        return render(request, "FoodFinder/create_account.html", context)

@csrf_protect
def restaurant(request):
    place_id = request.GET.get('place')
    response = map_client.place(place_id)

    if response["status"] == "OK":
        print('Successful search!')
        context = {"response": response}
    else:
        print(f"Error: {response['status']}")
        context = response
    return render(request, "FoodFinder/restaurant.html", context=context)

@login_required(login_url="login")
def favorites(request):
    return render(request, "FoodFinder/favorites.html")
