from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home , name='home'),
    path('about', views.about , name='about'),
    path('ratecard', views.ratecard , name='ratecard'),
    path('calculator', views.calculator , name='calculator'),
    path('signin', views.signin , name='signin'),
    path('signup', views.signup , name='signup'),
    path('schedule_pickup', views.schedule_pickup , name='schedule_pickup'),
]