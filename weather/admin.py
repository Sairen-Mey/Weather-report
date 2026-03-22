from django.contrib import admin
from .models import City, WeatherSnapshot
# Register your models here.


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name","country_code","lon", "lat", "created_at")

@admin.register(WeatherSnapshot)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ("city", "description","temperature", "wind_speed", "created_at", "observed_at", "humidity", "raw")
