import requests
from django.shortcuts import render
from weather.models import CityWeather
from .forms import CityForm
from info_hm_city.settings import WEATHER_APP_ID


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=' + WEATHER_APP_ID

    if request.method == 'POST':
        form = CityForm(request.POST)  # request.POST == значения которые получаем от пользователя из формы
        form.save()  # сохранение данных в БД

    form = CityForm()  # очистка формы

    city = CityWeather.objects.all()

    city_info = {
        'city': city.name,
        'temp': city["list"][0]["main"]["temp"],
        'icon': city["list"][0]["weather"][0]["icon"]
    }

    context = {'weather_info': city_info}

    return render(request, 'include/header.html', context)
