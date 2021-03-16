import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from info_hm_city.settings import WEATHER_APP_ID
# from picnic_area_app.forms import AddNewElementForm
from picnic_area_app.models import PicnicArea, Category
from .services import PicnicAreaService


def index(request):
    return render(request, 'picnic_area/index.html')


@csrf_exempt
def picnic_places(request):
    # Вызывается для обновления данных в БД из источника открытых данных Югры
    PicnicAreaService.update_picnic_places_in_db()

    picnic_areas = PicnicArea.objects.all()

    all_picnic_areas = []
    for picnic_area in picnic_areas:
        picnic_area_info = {
            'name': picnic_area.NAME_PICNIC,
            'description': picnic_area.DESCRIPTION,
            'address': picnic_area.ADDRESS_LANDMARK,
            'service_provider': picnic_area.SERVICE_PROVIDER,
            'phone': picnic_area.PHONE,
            'geocoord': picnic_area.GEOCOORD,
            'photo': picnic_area.THE_PHOTO,
            'date_update': picnic_area.DATE_UPDATE,
        }

        all_picnic_areas.append(picnic_area_info)

    context = {
        'picnic_areas': all_picnic_areas,
        'weather_hm_info': get_weather_hm()
    }

    return render(request, 'picnic_area/picnic_places.html', context)


def get_weather_hm():
    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=' + WEATHER_APP_ID
    city = 'Ханты-Мансийск'

    res = requests.get(url.format(city)).json()  # из json в формат словарей
    city_info = {
        'city': city,
        'temp': res["list"][0]["main"]["temp"],
        'icon': res["list"][0]["weather"][0]["icon"]
    }

    return city_info


def add_new_element_on_site(request):
    return render(request, 'picnic_area/add_new_element.html')


def get_categories(self):
    categories = Category.objects.all()

    data_category_temp = []
    for category in categories:
        categories_info = {
            'name': category.name,
            'icon': category.icon,
            'description': category.description,
        }

        data_category_temp.append(categories_info)

    context = {
        'categories': data_category_temp,
    }
    return render(self, 'picnic_area/all_categories.html', context)

# class AddReview(View):
#     """Отзывы"""
#
#     def post(self, request):
#         form = AddNewElementForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)  # приостановка сохранения формы для внесения каких то изменений
#             form.save()  # сохранение данных формы в БД
#         return redirect(movie.get_absolute_url())
