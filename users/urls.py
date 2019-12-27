from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = 'home-view'),
    path('login/', views.login, name = 'login-view'),
    path('register/', views.register, name = 'register-view'),
    path('scout/', views.scout, name = 'scout-view'),
    path('scouthub/', views.scouthub, name = 'scouthub-view'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout-view'),
    path('userpage/', views.UserPage, name = 'user-view')
]