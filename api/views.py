from django.shortcuts import render
from django.shortcuts import render, redirect
from .serializers import MatchSerializer, PitStatSerializer, UserSerializer
from rest_framework.viewsets import ModelViewSet
from stats.models import Match, Pit_stats
from users.models import CustomUser
from rest_framework.authtoken.models import Token

        
def StatsAPI(request):
    return render(request, 'api/api.html')

class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    lookup_field = ('team_num')
    
class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = ('username')

class PitViewSet(ModelViewSet):
    queryset = Pit_stats.objects.all()
    serializer_class = PitStatSerializer
    

