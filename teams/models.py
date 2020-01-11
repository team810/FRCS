from django.db import models
from users.models import CustomUser

# Create your models here.
class Team(models.Model):
    team_users = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team_num = models.IntegerField()

    def __str__(self):
        return f'{self.team_num} Team'