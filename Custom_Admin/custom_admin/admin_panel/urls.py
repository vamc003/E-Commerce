from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminpanel, name='adminpanel'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('userhome/', views.userhome, name='userhome'),
    path('home/', views.homepage, name='home'),
    # Add more paths as needed
]