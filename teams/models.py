from django.db import models
from users.models import CustomUser
from stats.models import Game_stats

# Create your models here.

class Match(models.Model):
    match_num = models.IntegerField()
    game_stats = models.ForeignKey(Game_stats, on_delete=models.SET_NULL, null = True)

class Team(models.Model):
    team_users = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    team_num = models.IntegerField()
    matches = models.ForeignKey(Match, on_delete=models.SET_NULL, null = True)
    def __str__(self):
        return f'{self.team_num} Team'
