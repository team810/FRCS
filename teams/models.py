from django.db import models

# Create your models here.
class Team(models.Model):
    team_users = models.ForeignKey('users')
    team_name = models.CharField()
    team_num = models.IntegerField()

    def __str__(self):
        return self.team_name