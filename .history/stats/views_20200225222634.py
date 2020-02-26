import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import request
from teams.models import Team
import string
from .models import Pit_stats, Game_stats
from .forms import pit_scout_form, game_scout_form
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.detail import SingleObjectMixin, BaseDetailView, SingleObjectTemplateResponseMixin
import tbapy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from users.views import JsonResponse

def scouthub(request):
  return render(request, 'stats/scout-hub.html', {'team_count': Team.objects.all().count()})

def pitdata(request):
  return render(request, 'stats/pit-data.html')

#class ScoutDetailView(DetailView):
#  model = Game_stats
  #return render(request, 'stats/game-data.html')

class ScoutListView(ListView):
  model = Game_stats
  template_name = 'stats/game_stats_list'  # <app>/<model>_<viewtype>.html
  context_object_name = 'stats'
  ordering = ['-id']

class PitListView(ListView):
  model = Pit_stats
  template_name = 'stats/pit_stats_list'
  context_object_name = 'teams'
  ordering = ['-id']


class PitDetailView(DetailView):
  model = Pit_stats

@login_required
def feed(request):
  return render(request, 'stats/feed.html')

def gamedata(request):
  return render(request, 'stats/game-data.html')

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
        return redirect('home-view')
      form.save()
      return redirect('home-view')
    else:
      return redirect('home-view')
  return render(request, 'stats/pit-scout.html', {'form': form})

@login_required
def scout(request):
  form = game_scout_form(request.POST)
  if request.method == 'POST':
    print(form.errors)
    print(form.non_field_errors)
    if form.is_valid():
      #Saving team number of user to Game_stats object
      obj = form.save(commit=False)
      obj.team_num = request.user.team_num
      #Gathering data
      team_num = form.cleaned_data['scouted_team_num']
      #Creating new team if necessary
      if not Team.objects.filter(team_num = team_num).exists():
        Team.objects.create(team_num = team_num)
      #Finally, add Game_stats object to the team
      obj.stat = Team.objects.get(team_num = team_num).game_stats
      form.save()
      return redirect('home-view')
    else:
      return redirect('scout-view')
  return render(request, 'stats/scout.html', {'form': form})

class ExtendedView(DetailView):
  """A base view for displaying a single object."""
  model = Game_stats
  def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    data = self.get_context_data(object=self.object)
    if self.request.GET:
      data__ = JsonForm(request.GET)
      if data__.is_valid():
        json = data__.cleaned_data['json']
        if json == 'true':
          return JsonResponse({'data': data})
    return self.render_to_response(data)