from django import forms
from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
		attrs={
            'style': 'background-color: rgba(250,250,250,0.3);',
            'class': 'form-control',
            'placeholder': 'First Name'
        }
	))
    team_num = forms.IntegerField(label='Last Name', widget=forms.NumberInput(
		attrs={
            'style': 'background-color: rgba(250,250,250,0.3);',
            'class': 'form-control',
            'placeholder': 'Team Number'
        }
	))
    message = forms.CharField(label='Message', widget=forms.Textarea(
		attrs={
            'style': 'background-color: rgba(250,250,250,0.3);',
            'class': 'form-control',
            'placeholder': 'Message'
        }
	))

    class Meta:
        model = Feedback
        fields = ['first_name', 'team_num', 'message']
