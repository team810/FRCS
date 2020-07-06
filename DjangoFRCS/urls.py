"""DjangoFRCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from stats import views as scout_views
from . import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
from rest_framework.authtoken import views 
from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import CoreJSONRenderer
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer



urlpatterns = [
    path('', include('users.urls')),
    path('', include('api.urls')),
    path('feedback/', include('feedback.urls')),
    path('scout/game/', scout_views.scout, name = 'scout-view'),
    path('scout/pit/', scout_views.pit_scout, name = 'Pitscout-view'),
    path('datahub/', scout_views.scouthub, name = 'scouthub-view'),
    path('pit-detail/<int:pk>/', scout_views.PitDetailView.as_view(), name = 'pitdata-view'),
    path('game-detail/<int:pk>/', scout_views.ScoutDetailView.as_view(), name = 'gamedata-view'),
    #path('pit-data/', scout_views.pitdata, name = 'pitdata-view'),
    #path('game-data/', scout_views.gamedata, name = 'gamedata-view'),
    path('list/pit', scout_views.PitListView.as_view(), name = 'pitdatahub-view'),
    path('list/game', scout_views.ScoutListView.as_view(), name = 'gamedatahub-view'),
    path('flag/<int:pk>', scout_views.pitFlag , name='pit-flag-view'),
    url(r'^api/', include('api.urls')),
    
    
    


]

if settings.DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]
