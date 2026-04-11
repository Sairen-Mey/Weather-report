from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.create_account, name="register"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login')
]