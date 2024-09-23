import requests
from django.core.management.base import BaseCommand
from FoodFinder.models import Restaurant  # Replace 'myapp' with your actual app name

class Command(BaseCommand):
    help = 'Fetch restaurants from Google Places API'

    def handle(self, *args, **kwargs):
        api_key = 'AIzaSyAzUAD-CDwQINhVb-xyJSxovR61L6Pau24'  # Replace with your actual API key
        location = '37.7749,-122.4194'  # Example: San Francisco
        radius = 5000  # Search within 5 km
        type = 'restaurant'
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={api_key}'

        response = requests.get(url)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Error fetching data: {response.status_code}'))
            return

        data = response.json()
        for place in data.get('results', []):
            Restaurant.objects.update_or_create(
                place_id=place['place_id'],
                defaults={
                    'name': place.get('name'),
                    'address': place.get('vicinity'),
                    'rating': place.get('rating'),
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored restaurants'))
