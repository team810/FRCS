from django.db import models
from teams.models import Team

# Create your models here.

class Pit_stats(models.Model):
    team_num = models.IntegerField(null = True)
    robot_weight = models.DecimalField(max_digits=5, decimal_places = 2, null = True)
    robot_frame_length = models.DecimalField(max_digits=5, decimal_places = 2, null = True)
    robot_frame_width = models.DecimalField(max_digits=5, decimal_places = 2, null = True)
    robot_drivetrain_type = models.CharField(max_length=100, null = True)
    robot_vision_type = models.CharField(max_length=100, null = True)
    robot_vision_implement = models.CharField(max_length=100, null = True)
    robot_goal = models.CharField(max_length=100, null = True)
    robot_autonomous = models.CharField(max_length=100, null = True)
    robot_highlow = models.CharField(max_length=100, null = True)
    robot_climb = models.CharField(max_length=100, null = True)
    robot_buddy_climb = models.CharField(max_length=100, null = True)
    robot_control_panel = models.CharField(max_length=100, null = True)
    notes = models.TextField(max_length=100, null = True)

    def __str__(self):
        return f'{self.team_num} Pit Stats'

class Stat(models.Model):
    pass
    #team = models.ForeignKey(Team, on_delete=models.PROTECT)
    #pit_stats = models.OneToOneField(Pit_stats, on_delete=models.PROTECT)
    #game_stats = models.OneToOneField('Game_stats', on_delete=models.PROTECT)

#class Game_stats:
    