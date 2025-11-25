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
    path('signout', views.signout , name='signout'),
    path('auth/callback', views.auth_callback , name='auth_callback'),
    path('schedule_pickup', views.schedule_pickup , name='schedule_pickup'),
    path('ai_analyze', views.ai_analyze , name='ai_analyze'),
    path('view_pickups', views.view_pickups , name='view_pickups'),
]