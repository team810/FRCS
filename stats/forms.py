from django import forms
from django.forms import ModelForm
from .models import Pit_stats

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
	robot_drivetrain_type.widget.attrs.update({'class': 'form-control'})
	robot_highlow = forms.CharField(widget=forms.Select(choices=BOT_HEIGHT))
	robot_highlow.widget.attrs.update({'class': 'form-control'})
	robot_vision_type = forms.CharField(widget=forms.Select(choices=VISION_TYPE))
	robot_vision_type.widget.attrs.update({'class': 'form-control'})
	robot_goal = forms.CharField(widget=forms.Select(choices=GOAL_SHOT))
	robot_goal.widget.attrs.update({'class': 'form-control'})
	robot_vision_implement = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_vision_implement.widget.attrs.update({'class': 'form-control'})
	robot_autonomous = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_autonomous.widget.attrs.update({'class': 'form-control'})
	robot_climb = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_climb.widget.attrs.update({'class': 'form-control'})
	robot_control_panel = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_control_panel.widget.attrs.update({'class': 'form-control'})
	class Meta:
		model = Pit_stats
		fields = '__all__'