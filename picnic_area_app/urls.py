from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('picnic_places/', views.picnic_places),
    path('add_new_element/', views.add_new_element_on_site),
    path('all_categories/', views.get_categories),
]
