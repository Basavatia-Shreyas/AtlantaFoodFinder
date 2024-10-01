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
from FoodFinder.models import Profile

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from urllib.parse import urlencode

import googlemaps
map_client = googlemaps.Client(api_key)

from .templates.forms import CreateUserForm

# Create your views here.
@csrf_protect
def index(request):

    current_loc = map_client.geolocate(consider_ip=True)
    if current_loc == None:
        current_loc = {'location': {'lat': 33.7707008, 'lng': -84.3874304}, 'accuracy': 1050.952656998642}

    cuisine_restaurants = {"results" : []}
    if request.user.is_authenticated:
        favoriteCuisine = request.user.profile.favoriteCuisine
        #print(favoriteCuisine)
        cuisine_restaurants = map_client.places(favoriteCuisine + " restaurants")
        for index, restaurant in enumerate(cuisine_restaurants['results']):
            try:
                photo_reference = restaurant["photos"][0]["photo_reference"]
                link = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
                cuisine_restaurants['results'][index]["photo_link"] = link
                cuisine_restaurants['results'][index].pop("photos", None)
            except:
                pass
    
    rating = request.GET.get("rating")
    radius = request.GET.get("radius")
    search = request.GET.get('search')

    if rating:
        rating = int(rating)
    if radius:
        radius = int(radius) * 1609


    if radius and search:
        print(type(rating))
        print(type(radius))
        try:
            current_loc = map_client.geolocate(consider_ip=True)
            response = map_client.places_nearby(keyword=search, location=current_loc['location'], radius=radius, type="restaurant")

            if rating:
                print("RATING")
                response['results'] = [place for place in response.get('results', []) if place.get('rating', 0) >= rating]

        except Exception as e:
            current_loc = {'location': {'lat': 33.7707008, 'lng': -84.3874304}, 'accuracy': 1050.952656998642}
            response = {"Error": "Couldn't load nearby restaurants"}
    elif radius:
        try:
            current_loc = map_client.geolocate(consider_ip=True)
            response = map_client.places_nearby(location=current_loc['location'], radius=radius, type="restaurant")
            print(radius)
            if rating:
                response['results'] = [place for place in response.get('results', []) if place.get('rating', 0) >= rating]

        except Exception as e:
            current_loc = {'location': {'lat': 33.7707008, 'lng': -84.3874304}, 'accuracy': 1050.952656998642}
            response = {"Error": "Couldn't load nearby restaurants"}
    elif rating:
         # If there's a search query, use the Places API to search for it
        try:
            response = map_client.places(type="restaurant")
            response['results'] = [place for place in response.get('results', []) if place.get('rating', 0) >= rating]
        except Exception as e:
            print(f"Error fetching search results: {e}")
            response = {"Error": "Couldn't perform search"}
    elif search:
        #print(search)
        response = map_client.places(search + " restaurant", type="restaurant")
        context = {"response": response['results'], "current_location": current_loc, "google_maps_api_key": api_key}
    else:
        response = map_client.places_nearby(location=current_loc['location'], radius=500, type="restaurant")
        if response["status"] != "OK":
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
        #print(current_loc)
        context = {"response": response['results'], "current_location": current_loc, "google_maps_api_key": api_key, 'cuisine': cuisine_restaurants['results']}
    else:
        print(f"Error: {response['status']}")
        context = response

    if request.method == "POST":
        if "place" in request.POST.keys():
            #print("POST REQUEST", request.POST)
            base_url = reverse('restaurant')
            place_id = request.POST.get("place")
            query_string = urlencode({'place': place_id})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
        elif "search" in request.POST.keys():
            #print("SEARCH", request.POST)
            base_url = reverse('index')
            search_query = request.POST.get("search")
            query_string = urlencode({'search': search_query})
            url = '{}?{}'.format(base_url, query_string)

            return redirect(url) 
    return render(request, "FoodFinder/home.html", context=context)

@csrf_protect
def loginPage(request):

    favorite_cuisine = request.GET.get("cuisine")

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
            print(request.POST)

            favoriteCuisine = request.POST.get("cuisine")
            #print(favoriteCuisine)
            if form.is_valid():
                form.save()
                user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password1"))

                cuisine = request.POST.get("cuisine")
                #user.profile.favoriteCuisine = cuisine
                profile = Profile(user=user, favoriteCuisine=cuisine, favorites="")
                profile.save()

                base_url = reverse('login')
                query_string = urlencode({'cuisine': cuisine})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
            else:
                error_str = ''.join([f'{value} ' for key, value in form.error_messages.items()]).strip()
                messages.info(request, error_str)

        context = {"form" : form}
        return render(request, "FoodFinder/create_account.html", context)

@csrf_protect
def restaurant(request):
    place_id = request.GET.get('place')
    response = map_client.place(place_id)


    current_loc = map_client.geolocate(consider_ip=True)

    links = []
    try:
        for photo in response["result"]["photos"]:
            photo_reference = photo["photo_reference"]
            links.append(f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}")
    except:
        pass

    response["photo_links"] = links
    response["favorites"] = request.user.profile.favorites

    if response["status"] == "OK":
        #print('Successful search!')
        context = {"response": response, "current_location": current_loc, "google_maps_api_key": api_key}
    else:
        print(f"Error: {response['status']}")
        context = response
    
    if request.method == "POST":
        if "favorite" in request.POST.keys():
            print("favorite request")
            # Add to the current user's favorites
            if place_id not in request.user.profile.favorites and len(request.user.profile.favorites) < 280:
                print("adding to favorites")
                curr_profile = Profile.objects.get(user=request.user)
                curr_profile.favorites += " " + place_id
                curr_profile.save()
            if place_id in request.user.profile.favorites:
                curr_profile = Profile.objects.get(user=request.user)
                curr_profile.favorites = curr_profile.favorites.replace(" " + place_id, "")
                curr_profile.save()
            
            base_url = reverse('restaurant')
            place_id = request.POST.get("place")
            query_string = urlencode({'place': place_id})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)

    return render(request, "FoodFinder/restaurant.html", context=context)

@login_required(login_url="login")
def favorites(request):
    favorite_str = Profile.objects.get(user=request.user).favorites
    #print(favorite_str)
    favorites = favorite_str.split(" ")
    response = {"favorites":[]}
    print(favorites)
    for place_id in favorites[1:]:
        print("PLACEID", place_id)
        temp_response = map_client.place(place_id)
        if temp_response["status"] == "OK":
            photo_reference = temp_response['result']['photos'][0]["photo_reference"]
            link = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_reference}&key={api_key}"
            temp_response['result']["photo_link"] = link
            response['favorites'].append(temp_response['result'])

    current_loc = map_client.geolocate(consider_ip=True)
    if current_loc == None:
        current_loc = {'location': {'lat': 33.7707008, 'lng': -84.3874304}, 'accuracy': 1050.952656998642}

    if request.method == "POST":
        if "place" in request.POST.keys():
            #print("POST REQUEST", request.POST)
            base_url = reverse('restaurant')
            place_id = request.POST.get("place")
            query_string = urlencode({'place': place_id})
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)

    context={"response": response["favorites"], "google_maps_api_key": api_key, "current_location": current_loc}
    
    return render(request, "FoodFinder/favorites.html", context=context)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'FoodFinder/password_reset.html'
    email_template_name = 'FoodFinder/password_reset_email.html'
    subject_template_name = 'FoodFinder/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')

