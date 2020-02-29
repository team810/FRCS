from django import forms
from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
		attrs={
            
            'class': 'form-control',
            'placeholder': 'First Name',
            'id': 'name-form'
        }
	))
    team_num = forms.IntegerField(label='Last Name', widget=forms.NumberInput(
		attrs={
            'class': 'form-control',
            'placeholder': 'Team Number',
            'id': 'team-form'
        }
	))
    message = forms.CharField(label='Message', widget=forms.Textarea(
		attrs={
            'class': 'form-control',
            'placeholder': 'Message',
            'id': 'msg-form'
        }
	))

    class Meta:
        model = Feedback
        fields = ['first_name', 'team_num', 'message']
