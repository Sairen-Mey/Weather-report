from django.contrib import admin
from .models import Subscription





@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('city','email','is_active','created_at','last_sent_at')
    ordering = ('-created_at',)
    search_fields = ('city','email','is_active')
    list_filter = ('created_at','is_active')
