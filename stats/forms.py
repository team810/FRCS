from django import forms
from .models import Pit_stats
class pit_scout_form(forms.ModelForm):
    pass
'''
    class Meta:
        model = Pit_stats
        fields = '__all__'
        widgets = {
            'team_num': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Team Number'}),
            'robot_weight': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Robot Weight', 'step': '0.1'}),
            'robot_frame_length': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Robot Frame Length', 'step': '0.1'}),
            'robot_frame_width': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Robot Frame Width', 'step': '0.1'}),
            'robot_drivetrain_type': TextInput(attrs={'class': 'form-control', 'placeholder': 'Team Number'}),
            'robot_vision_type': TextInput(attrs={'class': 'form-control', 'placeholder': 'Robot Vision'}),
            'robot_vision_implement': TextInput(attrs={'class': 'form-control', 'placeholder': 'Implement Vision'}),
            'robot_goal': TextInput(attrs={'class': 'form-control', 'placeholder': 'Goal Robot'}),
            'robot_autonomous': TextInput(attrs={'class': 'form-control', 'placeholder': 'Autonomous'}),
            'robot_highlow': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Team Number'}),
            'robot_climb': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Team Number'}),
            'robot_control_panel': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Team Number'}),
            'notes': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Team Number'}),
'''
        #}
