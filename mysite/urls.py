
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('count/',views.count,name='count'),
    path('abouts/',views.abouts,name='abouts'),
    path('home/',views.home),
]
