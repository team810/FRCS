from rest_framework import serializers
from stats.models import Match, Pit_stats

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PitStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pit_stats
        fields = '__all__'