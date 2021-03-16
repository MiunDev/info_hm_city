import requests
from django.views.decorators.csrf import csrf_exempt
from picnic_area_app.models import PicnicArea, Category


@csrf_exempt
def update_picnic_places_in_db():
    url = 'https://data.admhmao.ru/api/data/?id=1933871'

    # заголовки
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()

    print(res)

    # удаляем все записи из открытых данных
    # delete_row_from_od()

    # добавляем свежие данные
    category = Category.objects.all()[0]

    for item in res['Items']:
        str_service_provider = item['Cells']['SERVICE_PROVIDER']
        result_str_service_provider = str_service_provider.replace('\\', '')

        str_address_landmark = item['Cells']['ADDRESS_LANDMARK']
        result_str_address_landmark = str_address_landmark.replace('\\', '')

        PicnicArea.objects.update_or_create(
            NAME_PICNIC=item['Cells']['NAME_PICNIC'],
            ADDRESS_LANDMARK=result_str_address_landmark,
            SERVICE_PROVIDER=result_str_service_provider,
            PHONE=item['Cells']['PHONE'],
            GEOOBJECT_NAME=item['Cells']['GEOOBJECT_NAME'],
            GEOCOORD=item['Cells']['GEOCOORD'],
            THE_PHOTO='picnic_area/base_image.jpg',
            CATEGORY=category,
            DATA_FROM_OD=1,
        )


def delete_row_from_od():
    PicnicArea.objects.filter(DATA_FROM_OD=1).delete()
