from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    team_num = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Team Number'
        }
    ))

    password = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))

    class Meta:
        model = User
        fields = (
            'email', 
            'team_num', 
            'password', 
            'username'
        )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        team_num = self.cleaned_data['team_num']
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']

        if commit:
            user.save()

        return user