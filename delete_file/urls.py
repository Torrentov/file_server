from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/file_remove', include('file_remove.urls'))
]