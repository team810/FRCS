import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import request
from teams.models import Team
import string
from .models import Pit_stats
from .forms import pit_scout_form
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.base import TemplateResponseMixin
import tbapy
#from .forms import CustomUserCreationForm
#from .models import UserProfile
#from .backends import CustomUserAuth as auth
# Create your views here.

@login_required
def scout(request):
  return render(request, 'stats/scout.html', {'team_num': request.user.team_num})

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
  return render(request, 'stats/pit-data.html')

def gamedata(request):
  return render(request, 'stats/game-data.html')

def pitdatahub(request):
  return render(request, 'stats/pit-data-hub.html')

def gamedatahub(request):
  return render(request, 'stats/game-data-hub.html')

def test(request):
  return render(request, 'stats/test.html')

def pit_scout(request):
  form = pit_scout_form(request.POST)
  competitions = []
  if request.method == 'POST':
    if form.is_valid():
      form.save(commit=False)
      team_num = form.cleaned_data['team_num']

      if not Team.objects.filter(team_num = team_num).exists():
        Team.objects.create(team_num = team_num)

      if Pit_stats.objects.filter(team_num = team_num).exists():
        #Do something
        pass

      form.save()
    else:
      return redirect('home-view')
  return render(request, 'stats/pit-scout.html', {'form': form})

def get_competitions(self, team_num):
  tba = tbapy.TBA('PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw')
  return tba.team_matches(team_num)
