from django.db import models
from users.models import CustomUser
from stats.models import Game_stats

# Create your models here.

class Team(models.Model):
    team_users = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    team_num = models.IntegerField()
    def __str__(self):
        return f'{self.team_num} Team'

class Match(models.Model):
    match_num = models.IntegerField()
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    game_stats = models.ForeignKey(Game_stats, on_delete=models.SET_NULL, null = True)
