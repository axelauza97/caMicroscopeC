from .views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('', index, name='index'),
    path('capture/<int:spectr>/', images, name='capture'),

]
