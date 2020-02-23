from django import forms
from django.forms import ModelForm
from .models import Pit_stats, Game_stats
from users.models import CustomUser

#BOT_HEIGHT = [
#	
# ('Low - Below 28' 'Low - Below 28'),
# ('High - Above 28', 'High - Above 28'),
#]

#!WONT RUN JS -- NEED 'ONCHANGE' ATTRIBUTE ADDED

#TODO - change low to 'low - below 28"'
#TODO - change high to 'High - above 28"'

BOT_HEIGHT = [
	
 ('Low - below 28"', 'Low - below 28"'),
 ('High - above 28"', 'High - above 28"'),
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
	robot_buddy_climb = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))

	class Meta:
		model = Pit_stats
		fields = '__all__'

MATCH_TYPE = [
	('Qualifying Match','Qualifying Match'),
	('Quarter Final','Quarter Final'),
	('Semi Final','Semi Final'),
	('Final','Final'),
	('Elimination Final','Elimination Final')
]

COMPETITIONS = []

class game_scout_form(ModelForm):
	users = None
	competitions = forms.ModelChoiceField(queryset=users)
	#match_number
	match_type = forms.CharField(widget=forms.Select(choices=MATCH_TYPE))
	initiation_line = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	control_panel = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_climb = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_generator = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	defense_played = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	robot_climb_help = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))
	penalties = forms.CharField(widget=forms.Select(choices=TRUE_FALSE))

	def __init__(self, user, *args, **kwargs):
		self.user = user
		self.users = CustomUser.objects.all()
		super(game_scout_form, self).__init__(*args, **kwargs)
		self.fields['competitions'].queryset = self.users

	class Meta:
		model = Game_stats
		exclude = ['team_num', 'team']
