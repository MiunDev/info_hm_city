from .models import CityWeather
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = CityWeather
        fields = ['name']
        widgets = {'name': TextInput(attrs={  # параметры для поля ввода
            'class': 'form-control',
            'name': 'city',
            'id': 'city',
            'placeholder': 'Введите город'
        })}
