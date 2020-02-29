from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.db.models import Q
from django.contrib.auth.forms import UserChangeForm

User = get_user_model()

class UserCreationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput(
		attrs={
            'class': 'form-control',
            'placeholder': 'Password',
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
            'id': 'email-form'
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
		if not user_qs_final.exists() and user_qs_final.count != 1:
			raise forms.ValidationError("Invalid credentials - user does note exist")
		user_obj = user_qs_final.first()
		if not user_obj.check_password(password):
			raise forms.ValidationError("credentials are not correct")
		self.cleaned_data["user_obj"] = user_obj
		return super(UserLoginForm, self).clean(*args, **kwargs)

