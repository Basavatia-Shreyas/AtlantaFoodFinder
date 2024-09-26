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
from django.views.decorators.http import require_POST
from .models import Restaurant, Favorite


import googlemaps
map_client = googlemaps.Client(api_key)

from .templates.forms import CreateUserForm
import requests

# Create your views here.
# @csrf_protect
# def index(request):
#
#     try:
#         current_loc = map_client.geolocate(consider_ip=True)
#         response = map_client.places_nearby(location=current_loc['location'], radius=500, type="restaurant")
#     except:
#         current_loc = {'location': {'lat': 33.7707008, 'lng': -84.3874304}, 'accuracy': 1050.952656998642}
#         response = {"Error" : "Couldn't load nearby restaurants"}
#     for index, restaurant in enumerate(response['results']):
#         try:
#             photo_reference = restaurant["photos"][0]["photo_reference"]
#             link = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
#             response['results'][index]["photo_link"] = link
#             response['results'][index].pop("photos", None)
#         except:
#             pass
#
#     if response["status"] == "OK":
#         print('Successful search!')
#         print(current_loc)
#         context = {"response": response['results'], "current_location": current_loc, "google_maps_api_key": api_key}
#     else:
#         print(f"Error: {response['status']}")
#         context = response
#
#     return render(request, "FoodFinder/home.html", context=context)

@csrf_protect
def index(request):
    global current_loc
    query = request.GET.get('search')
    searched = False

    if query:
        searched = True
        # If there's a search query, use the Places API to search for it
        try:
            response = map_client.places(query=query, type="restaurant")
        except Exception as e:
            print(f"Error fetching search results: {e}")
            response = {"Error": "Couldn't perform search"}
    else:
        searched = False
        # Default behavior: get nearby restaurants
        try:
            current_loc = map_client.geolocate(consider_ip=True)
            response = map_client.places_nearby(location=current_loc['location'], radius=5000, type="restaurant")
        except Exception as e:
            current_loc = {'location': {'lat': 33.7707008, 'lng': -84.3874304}, 'accuracy': 1050.952656998642}
            response = {"Error": "Couldn't load nearby restaurants"}

    # Process response to add photo links
    for index, restaurant in enumerate(response.get('results', [])):
        try:
            photo_reference = restaurant.get("photos", [{}])[0].get("photo_reference")
            if photo_reference:
                link = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
                response['results'][index]["photo_link"] = link
                response['results'][index].pop("photos", None)
        except Exception as e:
            print(f"Error processing photos: {e}")

    # Prepare context based on the response status
    if response.get("status") == "OK":
        print('Successful search!')
        context = {"response": response['results'], "current_location": current_loc, "google_maps_api_key": api_key}
    else:
        print(f"Error: {response.get('status')}")
        context = response

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

def restaurant(request):
    return render(request, "FoodFinder/restaurant.html")

@login_required(login_url="login")
def favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('restaurant')
    return render(request, "FoodFinder/favorites.html", {'favorites': favorites})

@login_required(login_url="login")
@require_POST
def toggle_favorite(request):
    restaurant_id = request.POST.get('restaurant_id')
    print(restaurant_id)

    try:
        restaurant = Restaurant.objects.get(place_id=restaurant_id)
    except Restaurant.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Restaurant not found'}, status=404)

    favorite, created = Favorite.objects.get_or_create(user=request.user, restaurant=restaurant)

    if not created:
        favorite.delete()
        is_favorite = False
    else:
        is_favorite = True

    return JsonResponse({'status': 'success', 'is_favorite': is_favorite})


@login_required(login_url="login")
def get_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('restaurant')
    favorite_restaurants = [
        {
            'id': fav.restaurant.place_id,
            'name': fav.restaurant.name,
            # Add other restaurant fields as needed
        }
        for fav in favorites
    ]
    return JsonResponse({'favorites': favorite_restaurants})



