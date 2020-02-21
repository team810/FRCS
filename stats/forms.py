from django import forms
from django.forms import ModelForm
from .models import Pit_stats, Game_stats
from users.models import CustomUser

BOT_HEIGHT = [
	
 ('Low', 'Low'),
 ('High', 'High'),
]


DRIVETRAIN_TYPE = [
    ('Skid', 'Skid'),
    ('Omni', 'Omni'),
	('Swerve','Swerve'),
	('Other','Other'),	
]

VISION_TYPE = [
	
 ('None', 'None'),
 ('Limelight', 'Limelight'),
 ('Raspberry Pi', 'Raspberry Pi'),
 ('Kinect', 'Kinect'),
 ('Other', 'Other'),
]

GOAL_SHOT = [
 
 ('Lower', 'Lower'),
 ('Inner', 'Inner'),
 ('Outer', 'Outer'),
 ('Both Low and High', 'Both Low and High'),
]



TRUE_FALSE = [
	('No', 'No'),
	('Yes', 'Yes'),
]

class pit_scout_form(ModelForm):
	robot_drivetrain_type = forms.CharField(widget=forms.Select(choices=DRIVETRAIN_TYPE))
	robot_highlow = forms.CharField(widget=forms.Select(choices=BOT_HEIGHT))
	robot_vision_type = forms.CharField(widget=forms.Select(choices=VISION_TYPE))
	robot_goal = forms.CharField(widget=forms.Select(choices=GOAL_SHOT))
	robot_vision_implement = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_autonomous = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_climb = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_control_panel = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	class Meta:
		model = Pit_stats
		fields = '__all__'

class game_scout_form(ModelForm):
	pass