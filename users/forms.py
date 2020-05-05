from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.db.models import Q
from django.contrib.auth.forms import UserChangeForm
from .models import Profile
from stats.models import Match
from django.http import request

def getProfileFirstName(request):
    f_placeholder = Profile.objects.get(request.user).first_name
    print(f_placeholder)
    return f_placeholder

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'password-form',


        }
    ))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    email = forms.EmailField(validators=[validate_email], label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'id': 'email-form',
        }
    ))
    team_num = forms.IntegerField(label='Username', widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Team Number',
            'id': 'team_num_reg',
            'onchange': 'changeRegName()'
        }
    ))
    is_team_admin = forms.BooleanField(label='Is Admin', required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'inp-cbx',
            'style': 'display: none;',
            'id': 'cbx'

        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'team_num']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return password

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct()

        # TODO: Need to create non active user error message

        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError(
                "Invalid credentials - user does note exist")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("credentials are not correct")
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username'
        )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)


class GameEditForm(forms.ModelForm):
    class Meta:
        model = Match
        exclude = ['competition', 'stat', 'user']


class NameEditForm(forms.ModelForm):
    
    
    first_name = forms.CharField(label='First Name', required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'form-first_name'
        }
    ))
    
    last_name = forms.CharField(label='Last Name', required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'form-last_name'
            
        }
    ))

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
        )
      

class ProfileSettingsForm(forms.ModelForm):
    
    viewPitResubmit = forms.BooleanField(label='viewPitResubmit', required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'inp-cbx',
            'style': 'display: none;',
            'id': 'cbx',
        }
    ))
    
    class Meta:
        model = Profile
        fields = ('viewPitResubmit',)

class TeamSettingsForm(forms.ModelForm):

    canEditStats = forms.BooleanField(label='canEditStats', required=False, widget=forms.CheckboxInput(
        attrs={
            'class': 'inp-cbx',
            'style': 'display: none;',
            'id': 'cbx',
        }
    ))
    class Meta:
        model = Profile
        fields = ('canEditStats',)