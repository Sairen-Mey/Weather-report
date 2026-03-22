from django.contrib.gis.gdal.prototypes.srs import from_proj
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import re_newlines

from forms import SubscriptionForm
# Create your views here.


def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscription success')
        return redirect('something is wrong')
    else:
        form = SubscriptionForm()

    return render(request, "subscriptions/create_subscription.html", {"form":form})

def subscription_success(request):
    return render(request, "subscriptions/create_subscription.html")
