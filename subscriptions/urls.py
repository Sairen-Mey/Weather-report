from django.urls import path

from . import views

# app_name = 'subscriptions'

urlpatterns = [
    path('sub_create/', views.subscription_create, name="sub_created"),
    path('sub_success/', views.subscription_success, name="sub_success"),
]