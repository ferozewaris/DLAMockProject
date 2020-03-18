from django.urls import path, include
from .views import upload_data, list_objects, get_object
from rest_framework import routers


urlpatterns = [
    path('upload_data', upload_data, name='upload_data'),
    path('list_objects', list_objects, name='list_objects'),
    path('get_object', get_object, name='get_object')
]