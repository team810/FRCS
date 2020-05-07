from django.db import models
from users.models import CustomUser
import random, string
# Create your models here.

class Team(models.Model):
    team_users = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    team_num = models.IntegerField()
    team_code = models.CharField(max_length=7, null=True)
    def __str__(self):
        return f' Team {self.team_num}'
    
