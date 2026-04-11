from django.shortcuts import render, redirect, get_object_or_404


from .forms import SubscriptionForm
# Create your views here.


def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sub_success')
        print("wrong")
        #return redirect('something is wrong')

    form = SubscriptionForm()

    return render(request, "subscriptions/create_subscription.html", {"form":form})

def subscription_success(request):
    return render(request, "subscriptions/subscription_succsessful.html")
