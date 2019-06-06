from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/upload', include('upload.urls')),
    path('/delete_file', include('delete_file.urls')),
    path('/delete_folder', include('delete_folder.urls')),
    path('/mkdir', include('mkdir.urls')),
    path('/rename', include('rename.urls')),
]
