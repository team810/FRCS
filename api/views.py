from django.shortcuts import render
from django.shortcuts import render, redirect
from .serializers import MatchSerializer, PitStatSerializer, UserSerializer, EmailSerializer, TeamSerializer, UserValidateSerializer, ProfileSerializer,UserSerializer
from rest_framework.viewsets import ModelViewSet
from stats.models import Match, Pit_stats
from users.models import CustomUser, Profile
from rest_framework.authtoken.models import Token
from teams.models import Team
from rest_framework import generics
from django.views.generic import ListView
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.core import serializers



class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered
    users. GET request returns the registered users whereas
    a POST request allows to create a new user.
    """
    permission_classes = [IsAdminUser]

    def get(self, format=None):
        users = CustomUser.objects.all()
        serializer = UserValidateSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserValidateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )


        
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
    lookup_field = ('team_num')
    
    
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = ("user_id")


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = ("auth_token")
