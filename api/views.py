from django.shortcuts import render
from django.shortcuts import render, redirect
from .serializers import MatchSerializer, PitStatSerializer, UserSerializer, EmailSerializer, TeamSerializer
from rest_framework.viewsets import ModelViewSet
from stats.models import Match, Pit_stats
from users.models import CustomUser
from rest_framework.authtoken.models import Token
from teams.models import Team
from rest_framework import generics
from django.views.generic import ListView
from rest_framework import mixins

        
def StatsAPI(request):
    return render(request, 'api/api.html')
    
class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    lookup_field = ('team_code')
    
class UserDetailViewSet(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = ('username')
    
class EmailViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = EmailSerializer
    lookup_field = ('email')

class PitViewSet(ModelViewSet):
    queryset = Pit_stats.objects.all()
    serializer_class = PitStatSerializer
    lookup_field = ('team_num')
    

class TeamDetailViewset(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = ('team_code')
    

    