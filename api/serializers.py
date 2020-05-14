from rest_framework import serializers
from stats.models import Match, Pit_stats
from users.models import CustomUser, Profile
from teams.models import Team
from django.http import request
from rest_framework.validators import UniqueTogetherValidator




class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PitStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pit_stats
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    
    username = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    match_count = serializers.SerializerMethodField('get_match_count')
    pit_count = serializers.SerializerMethodField('get_pit_count')
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'match_count', 'pit_count')
        
    def get_match_count(self, request):
        match_num = Match.objects.filter(user=request.username).count(),
        match_num = int(''.join(map(str, match_num)))
        return match_num
    
    def get_pit_count(self, request):
        pit_num = Pit_stats.objects.filter(user=request.username).count(),
        pit_num = int(''.join(map(str, pit_num))) 
        return pit_num

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email',)
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image', 'user')
        
class TeamSerializer(serializers.ModelSerializer):
    
    team_num = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    
    match_count = serializers.SerializerMethodField('get_match_count')
    pit_count = serializers.SerializerMethodField('get_pit_count')
    isPitScouted = serializers.SerializerMethodField('get_is_pit_scouted')
    global_match_count = serializers.SerializerMethodField('get_global_match_count')
    
    class Meta:
        model = Team
        fields = ('team_num', 'team_users', 'match_count', 'pit_count', 'isPitScouted', 'global_match_count')
        
    def get_match_count(self, request):
        match_num = Match.objects.filter(team_num=request.team_num).count(),
        match_num = int(''.join(map(str, match_num)))
        return match_num
    
    def get_pit_count(self, request):
        pit_num = Pit_stats.objects.filter(team_num=request.team_num).count(),
        pit_num = int(''.join(map(str, pit_num))) 
        return pit_num
    
    def get_global_match_count(self, request):
        global_match_num = Match.objects.filter(scouted_team_num=request.team_num).count(),
        global_match_num = int(''.join(map(str, global_match_num))) 
        return global_match_num
    
    
    def get_is_pit_scouted(self, request):
        isScouted = Pit_stats.objects.filter(team_num=request.team_num).count()
        
        if isScouted:
            return True
        else:
            return False
        
        

class UserValidateSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=CustomUser.objects.all(),
                fields=['username', 'email']
            )
        ]