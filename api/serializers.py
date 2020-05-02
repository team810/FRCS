from rest_framework import serializers
from stats.models import Match, Pit_stats
from users.models import CustomUser

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PitStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pit_stats
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ['password', 'is_staff', 'is_team_admin', 'is_active', 'is_verified', 'id']