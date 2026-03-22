import requests
import os
from dotenv import load_dotenv
from pathlib import Path
from django.core.management.base import BaseCommand
from weather.models import City, WeatherSnapshot
from datetime import datetime
from django.utils import timezone

class Command(BaseCommand):
    help = "get or create city"

    def add_arguments(self, parser):
        parser.add_argument("--city", required=True)



    def handle(self, *args, **options):
        city_name = options["city"]

        load_dotenv(Path(".") / ".env")
        API_KEY = os.getenv("OPENWEATHER_API_KEY")
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city_name,
            "appid": API_KEY,
            "units": "metric",
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f"Error API! City '{city_name}' not found."))
            return

        data : dict = response.json()

        city, created = City.objects.get_or_create(
            name=data["name"],
            defaults={
                "country_code": data["sys"]["country"],
                "lat": data["coord"]["lat"],
                "lon": data["coord"]["lon"],
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f"Created city: {city.name}"))
        else:
            self.stdout.write(self.style.WARNING(f"City already exists: {city.name}"))

        observation_time = timezone.make_aware(datetime.fromtimestamp(data["dt"]))

        WeatherSnapshot.objects.create(
            city=city,
            temperature=data["main"]["temp"],
            description=data["weather"][0]["description"],
            wind_speed=data["wind"]["speed"],
            humidity=data["main"]["humidity"],
            observed_at=observation_time,
        )
        self.stdout.write(self.style.SUCCESS(f"Successfully saved weather snapshot for {city.name}!"))