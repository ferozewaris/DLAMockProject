from django.urls import path, include
# from .views import upload_data, list_objects, get_object
from rest_framework import routers
from .views import UploadData, ListObjects, GetObject

urlpatterns = [
    path('upload_data', UploadData.UploadDataView.as_view(), name='upload_data'),
    path('list_objects', ListObjects.ListObjectsView.as_view(), name='list_objects'),
    path('get_objects', GetObject.GetObjectView.as_view(), name='get_objects')
]