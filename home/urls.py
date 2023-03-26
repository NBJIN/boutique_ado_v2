from django.contrib import admin
from django.urls import path
from . import views  # have to import views in order to get views up and runing


urlpatterns = {
    path('', views.index, name='home')
}
