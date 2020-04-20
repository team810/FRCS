from django.shortcuts import render
from django.shortcuts import render, redirect
from .serializers import MatchSerializer
from rest_framework.viewsets import ModelViewSet
from stats.models import Match
# Create your views here.

def StatsAPI(request):
    return render(request, 'api/api.html')

class MatchViewSet(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

