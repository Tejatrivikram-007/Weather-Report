from django.shortcuts import render
import requests
from django.conf import settings


def get_weather(city):
    api_key = settings.API_KEY

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    return response.json()

def weather_report(request):
    city = request.GET.get('city', 'Mysore')  #default mysore
    weather_data = get_weather(city) 
    context = {
        'city': city,
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description'],
        'icon': weather_data['weather'][0]['icon'],
    }
    return render(request, 'weather_report.html', context)
