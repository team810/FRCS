from django.db import models
from teams.models import Team

# Create your models here.
class Pit_stats:
    team_num = models.IntegerField(verbose_name="Team Number")
    robot_weight = models.DecimalField(max_digits='5', decimal_places = '2')
    robot_frame_length = models.DecimalField(max_digits='5', decimal_places = '2')
    robot_frame_width = models.DecimalField(max_digits='5', decimal_places = '2')
    robot_drivetrain_type = models.CharField(max_length=100)
    robot_vision_type = models.CharField(max_length=100)
    robot_vision_implement = models.BooleanField()
    robot_goal = models.CharField(max_length=100)
    robot_autonomous = models.BooleanField()
    robot_highlow = models.CharField(max_length=100)
    robot_climb = models.BooleanField()
    robot_control_panel = models.BooleanField()
    notes = models.TextField(max_length=100)

class Stat(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    pit_stats = models.OneToOneField(Pit_stats, on_delete=models.PROTECT)
    #game_stats = models.OneToOneField('Game_stats', on_delete=models.PROTECT)

#class Game_stats:
    