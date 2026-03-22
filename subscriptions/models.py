from django.db import models
from weather.models import City
# Create your models here.

class Subscription(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE, related_name="subscriptions")
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_sent_at = models.DateTimeField(null=True, blank=True)
