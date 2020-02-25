from django.db import models
import tbapy
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
class Stat:
    pass

class Game_stats(models.Model):
    team = models.OneToOneField(Team, on_delete = models.CASCADE) #TAKE NULL = TRUE OUT IN PROD
    

class Match(models.Model):
    stat = models.ForeignKey(Game_stats, on_delete = models.CASCADE, null = True)
    team_num = models.IntegerField(null = True)
    competition = models.CharField(max_length=100, null = True)
    match_number = models.IntegerField(null = True)
    match_type = models.CharField(max_length=100, null = True)
    scouted_team_num = models.IntegerField(null = True)
    initiation_line = models.CharField(max_length=3, null = True)
    auto_low_goal_scored = models.IntegerField(null = True)
    auto_outer_goal_scored = models.IntegerField(null = True)
    auto_inner_goal_scored = models.IntegerField(null = True)
    low_goal_scored = models.IntegerField(null = True)
    outer_goal_scored = models.IntegerField(null = True)
    inner_goal_scored = models.IntegerField(null = True)
    control_panel = models.CharField(max_length=3, null = True)
    robot_climb = models.CharField(max_length=3, null = True)
    robot_generator = models.CharField(max_length=3, null = True)
    defense_played = models.CharField(max_length=3, null = True)
    defense_percentage = models.IntegerField(null = True)
    robot_climb_help = models.CharField(max_length=3, null = True)
    #For penalities ask how many if yes
    penalties = models.CharField(max_length=100, null = True)
    notes = models.CharField(max_length=100, null = True)

    def __str__(self):
        return f'{self.team_num} scouting {self.scouted_team_num} at {self.competition} match number {self.match_number}'