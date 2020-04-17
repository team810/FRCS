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

urlpatterns = [
    path('', include('users.urls')),
    path('feedback/', include('feedback.urls')),

    path('scout/', scout_views.scout, name = 'scout-view'),
    path('pitscout/', scout_views.pit_scout, name = 'Pitscout-view'),
    path('scouthub/', scout_views.scouthub, name = 'scouthub-view'),
    path('pit-detail/<int:pk>/', scout_views.PitDetailView.as_view(), name = 'pitdata-view'),
    path('game-detail/<int:pk>/', scout_views.ScoutDetailView.as_view(), name = 'gamedata-view'),
    #path('pit-data/', scout_views.pitdata, name = 'pitdata-view'),
    #path('game-data/', scout_views.gamedata, name = 'gamedata-view'),
    path('pit-data-hub/', scout_views.PitListView.as_view(), name = 'pitdatahub-view'),
    path('game-data-hub/', scout_views.ScoutListView.as_view(), name = 'gamedatahub-view'),
    #path('stats-edit/<int:pk>/', scout_views.edit_stats , name = 'edit-stats-view'),

    

    #path('test/', PitScoutView.as_view(), name = 'test-view'),
]

if settings.DEBUG:
    urlpatterns += [path('admin/', admin.site.urls)]
