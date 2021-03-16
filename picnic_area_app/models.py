from datetime import datetime
from django.db import models


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    icon = models.ImageField("Иконка", upload_to="categories/", default='')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class PicnicArea(models.Model):
    """Зоны для пикника"""
    currentDate = datetime.now()
    formatedDate = currentDate.strftime("%Y-%m-%d %H:%M")

    NAME_PICNIC = models.CharField("Наименование места для пикника", max_length=100)
    DESCRIPTION = models.TextField("Описание", default="Описание отсутствует...")
    ADDRESS_LANDMARK = models.CharField("Адресный ориентир", max_length=100, default='')
    SERVICE_PROVIDER = models.CharField("Обслуживающая организация", max_length=100, default='')
    PHONE = models.CharField("Телефон", max_length=100, default='')
    GEOOBJECT_NAME = models.CharField("Наименование геобъекта", max_length=100, default='')
    GEOCOORD = models.CharField("Геокоординаты", max_length=100, default='')
    THE_PHOTO = models.ImageField("Фото", upload_to="picnic_area/", null=True)
    DATE_UPDATE = models.DateTimeField(default=formatedDate, blank=True)
    CATEGORY = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )
    DATA_FROM_OD = models.BooleanField(default=False)
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.NAME_PICNIC

    class Meta:
        verbose_name = "Зона для пикника"
        verbose_name_plural = "Зоны для пикника"
