from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=50, blank=True)
    lon = models.DecimalField(max_digits=8, decimal_places=5)
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='city_name_idx'),
            models.Index(fields=['country_code'], name='city_country_code'),
        ]
        constraints = [
            models.UniqueConstraint(fields=["lat", "lon"], name="uniq_city_lat_lon")
        ]

    def __str__(self):
        if self.country_code:
            return f"{self.name}, {self.country_code}"
        return  self.name

class WeatherSnapshot(models.Model):
    city = models.ForeignKey('City',on_delete=models.CASCADE, related_name='weather_snapshots')
    description = models.CharField(max_length=255)
    temperature = models.IntegerField()
    wind_speed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    observed_at = models.DateTimeField()
    humidity = models.IntegerField()
    raw = models.JSONField(default=dict, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["city", "observed_at"], name="uniq_weather_snapshot_city_observed_at")
        ]

    def is_recent(self) -> bool:
        return self.observed_at >= timezone.now() - timedelta(hours=3)

    def __str__(self):
        return f"{self.city} at {self.observed_at.strftime('%Y-%m-%d %H:%M')}"

