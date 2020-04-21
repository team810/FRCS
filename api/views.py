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
    
class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PitViewSet(ModelViewSet):
    queryset = Pit_stats.objects.all()
    serializer_class = PitStatSerializer
    
def getKey(request):
    return render(request, 'api/key.html', {'key': Token})

def Match(request):
    return render(request, 'api/match.html')

def Pit(request):
    return render(request, 'api/pit.html')

def auth(request):
    return render(request, 'api/auth.html')

def errors(request):
    return render(request, 'api/errors.html')