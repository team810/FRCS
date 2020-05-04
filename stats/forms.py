from django import forms
from django.forms import ModelForm
from .models import Pit_stats, Game_stats, Match
from users.models import CustomUser
import json, requests




BOT_HEIGHT = [
 ('Low - below 28"', 'Low - below 28"'),
 ('High - above 28"', 'High - above 28"'),
]


DRIVETRAIN_TYPE = [
    ('4 Wheel Skid', '4 Wheel Skid'),
    ('6 Wheel Skid', '6 Wheel Skid'),
    ('8 Wheel Skid', '8 Wheel Skid'),
    ('Treads', 'Treads'),
    ('Omni', 'Omni'),
    ('Swerve','Swerve'),
    ('Other','Other'),	
]

VISION_TYPE = [
    
 ('None', 'None'),
 ('Limelight', 'Limelight'),
 ('Raspberry Pi', 'Raspberry Pi'),
 ('Other', 'Other'),
]

GOAL_SHOT = [
 
 ('Lower', 'Lower'),
 ('Inner', 'Inner'),
 ('Outer', 'Outer'),
 ('Both Low and High', 'Both Low and High'),
]



TRUE_FALSE = [
    ('0', 'No'),
    ('100', 'Yes'),
]

PENALTIES = [
    ('None', 'None'),
    ('Disbaled', 'Disabled'),
    ('Foul', 'Foul'),
    ('Tech Foul', 'Tech Foul'),
    ('Yellow Card', 'Yellow Card'),
    ('Red Card', 'Red Card')
]

CP = [
    ('No', 'No'),
    ('Positional', 'Positional'),
    ('Rotational', 'Rotational'),
    ('Both Position and Rotation', 'Both Position and Rotation')
    
]

class pit_scout_form(ModelForm):
    robot_drivetrain_type = forms.CharField(widget=forms.Select(choices=DRIVETRAIN_TYPE))
    robot_highlow = forms.CharField(widget=forms.Select(choices=BOT_HEIGHT))
    robot_vision_type = forms.CharField(widget=forms.Select(choices=VISION_TYPE))
    robot_goal = forms.CharField(widget=forms.Select(choices=GOAL_SHOT))
    robot_vision_implement = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_autonomous = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_climb = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_buddy_climb = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_control_panel_pos = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_control_panel_rot = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))

    class Meta:
        model = Pit_stats
        exclude = ['user', 'scouted_team_num']

MATCH_TYPE = [
    ('Qualifying Match','Qualifying Match'),
    ('Quarter Final','Quarter Final'),
    ('Semi Final','Semi Final'),
    ('Final','Final'),
    ('Elimination Final','Elimination Final')
]

class game_scout_form(ModelForm):
    #match_number
    match_type = forms.CharField(widget=forms.Select(choices=MATCH_TYPE))
    initiation_line = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_climb = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_generator = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    defense_played = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    robot_climb_help = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    penalties = forms.CharField(widget=forms.Select(choices=PENALTIES))
    control_panel_rot = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
    control_panel_pos = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
 
    class Meta:
        model = Match
        exclude = ['team_num' , 'stat', 'user', 'match_id', 'scouted_team_code']