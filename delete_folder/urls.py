from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/folder_remove', include('folder_remove.urls'))
]