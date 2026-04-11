from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.


def create_account(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')#

    form = RegisterForm()

    return render(request, "accounts/create_account.html", {"form": form})


