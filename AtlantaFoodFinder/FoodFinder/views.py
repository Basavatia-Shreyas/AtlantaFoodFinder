from django.shortcuts import render
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
api_key = os.getenv('SECRET_KEY')
import googlemaps
gmaps = googlemaps.Client(key=api_key)
def searchSpecific(query):
 try:
  result = gmaps.places(query=query, type='restaurant')
  if result["status"] == "OK":
   print('Successful search!')
   context = {"result": result['results'], "api_key": api_key}
   for place in result['results']:
    print(f"Name: {place['name']}")
    print(f"Address: {place['formatted_address']}")
    print(f"Rating: {place.get('rating', 'No rating')}")
    print()
    return context
   else:
    print(f"Error: {result['status']}")
    return {"status": result['status'], "message": "Search failed"}

 except (googlemaps.exceptions.ApiError, googlemaps.exceptions.Timeout,
          googlemaps.exceptions.TransportError) as e:
  print("An error occured")
  return {"status": "ERROR", "message": str(e)}

def searchCuisine(query):