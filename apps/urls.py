from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='home'),
    path('users/', views.users, name='users'),
    path('city_time/', views.city_time, name='city_time'),
    path('cnt/', views.counter, name='counter'),
]
