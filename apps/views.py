# Python Modules
from typing import Any

# Django Modules
from django.shortcuts import render
from datetime import datetime
import pytz

def welcome(request):
    return render(request, 'index.html')

def users(request):
    users_data = [
        {'name': 'Danial', 'age':20}, 
        {'name': 'Aibek', 'age':21},
        {'name': 'Asyl', 'age':19},
        {'name': 'Miras', 'age':22},

    ]
    return render(request, 'users.html', {'users': users_data})


def city_time(request):
    city = request.GET.get('city', 'UTC')
    cities = {
        'Astana': 'Asia/Nur-Sultan',
        'London': 'Europe/London',
        'New York': 'America/New_York', 
        'Tokyo': 'Asia/Tokyo',
        'Sydney': 'Australia/Sydney',
    }
    timezone = pytz.timezone(cities.get(city, 'UTC'))
    now = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'city_time.html', {'city': city, 'current_time': current_time})

counter_value = 0   
def counter(request):
    global counter_value
    if "increment" in request.GET:
        counter_value += 1
    elif "reset" in request.GET:
        counter_value -= 1
    return render(request, 'counter.html', {'counter': counter_value})




