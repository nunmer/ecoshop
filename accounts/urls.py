from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views  # Import your custom views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'), 
    path('auth/logout/', views.custom_logout, name='logout'),
    # path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('register/', views.register, name='register'),
]
