from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.http import urlquote
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import get_template
from .templates import users
import random
import string
import smtplib
import tbapy
import requests
import json
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

#Custom user model
class CustomUserManager(BaseUserManager):

    
    def create_user(self, username, email, team_num, password, **kwargs):
        if not email:
            raise ValueError("Email must be present")

        email = self.normalize_email(email)
        user = self.model(
                username = username,
                email = self.normalize_email(email),
                team_num = team_num,
                password = CustomUser.objects.make_random_password(),
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, 810, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = False
        user.is_active = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    team_num = models.IntegerField(verbose_name="Team Number")
    email = models.EmailField(unique=True)

    date_joined = models.DateTimeField(default=timezone.now())

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_team_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_absolute_url(self):
        return '/users/%s/' % urlquote(self.email)

    #def get_short_name(self):
    #    return self.first_name

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        else:
            return False

    def has_module_perms(self, app_label):
        return True

    def get_team_name(self): #? is this even used!!!
        '''returns name of team'''
        names = []
        tba = tbapy.TBA('PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw')
        response = requests.get('https://www.thebluealliance.com/api/v3/team/frc' + str(self.team_num) + '/simple', {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"})
        print(response)
        response = response.json()
        for name in response:
            n = name['name']
            names.append(n)
        return names

        

#Profile model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile-pics')
    first_name = models.CharField(verbose_name="First Name", max_length=254, blank=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=254, blank=True)
    viewPitResubmit = models.BooleanField(default=False)
    canEditStats = models.BooleanField(default=True)
    relativeScoring = models.BooleanField(default=False)
    search = models.CharField(max_length=1, blank=True, default='s')
    
    def __str__(self):
       return f'{self.user.username}'
   



#!PUT NEW SETTINGS INTO NEW MODEL
#class UserSetting(models.Model):
#    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#
#    def __str__(self):
#       return f'{self.profile}'