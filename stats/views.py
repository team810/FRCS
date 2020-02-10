import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import request
from teams.models import Team
import string
from stats.models import Pit_stats
from stats.forms import pit_scout_form
from django.views.generic.edit import CreateView
from stats.models import Pit_stats
#from .forms import CustomUserCreationForm
#from .models import UserProfile
#from .backends import CustomUserAuth as auth
# Create your views here.

@login_required
def scout(request):
    return render(request, 'stats/scout.html')

@login_required
def pitscout(request):
    form = pit_scout_form()
    if request.method == 'post':
        form.save()
        return redirect('index-view')
    return render(request, 'stats/pit-scout.html', {'form': form})

def scouthub(request):
    return render(request, 'stats/scout-hub.html', {'team_count': Team.objects.all().count()})

def pitdata(request):
    return render(request, 'stats/pit-data.html')

def gamedata(request):
    return render(request, 'stats/game-data.html')

@login_required
def feed(request):
    return render(request, 'stats/feed.html')

def pitdata(request):
  return render(request, 'users/pitdata.html')

def gamedata(request):
  return render(request, 'users/gamedata.html')

def pitdatahub(request):
  return render(request, 'users/pit-data-hub.html')

def gamedatahub(request):
  return render(request, 'users/game-data-hub.html')
