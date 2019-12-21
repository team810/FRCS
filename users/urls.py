from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name = 'home-view'),
    path('login/', views.login, name = 'login-view'),
    path('register/', views.register, name = 'register-view'),
    path('scout/', views.scout, name = 'scout-view'),
    path('scouthub/', views.scouthub, name = 'scouthub-view'),
]