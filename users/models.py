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
#Custom user model
class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, team_num, password=None, **kwargs):
        if not email:
            raise ValueError("Email must be present")

        email = self.normalize_email(email)
        user = self.model(
                username = username,
                email = self.normalize_email(email),
                team_num = team_num,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, 810, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    #first_name = models.CharField(verbose_name="First Name", max_length=254)
    #last_name = models.CharField(verbose_name="Last Name", max_length=254, blank=True)
    #team_name = models.CharField(verbose_name="Team Name", max_length=254)
    team_num = models.IntegerField(verbose_name="Team Number")
    email = models.EmailField(unique=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_team_admin = models.BooleanField(default=False)

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

   # def create_VID(self):
   #     n = 7
   #     return str(''.join(random.choices(string.ascii_uppercase + string.digits, k = n)))

    def email_verify(self):
        msg_html = render_to_string('users/emailTemplate.html', {'username': self.username, 'VID': self.VID})

        send_mail(
            'Verify Your Email: FRCS',
            msg_html,
            'frcsassistant@gmail.com',
            ['frcsassistant@gmail.com'],
        )
        #template = get_template('emailTemplate.html')
        #msg = MIMEMultipart('alternative')
        #htmly = MIMEText(template, 'html')
        #msg.attach(htmly)       
        #with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        #    smtp.ehlo()
        #    smtp.starttls()
        #    smtp.ehlo()
        #    smtp.login("frcsassistant@gmail.com", "zikpniouyggoqfmk")
        #    smtp.sendmail('frcsassistant@gmail.com','frcsassistant@gmail.com', msg.as_string())
    def get_competitions(self):
        '''returns name of competitions team has signed up for in 2020'''
        names = []
        tba = tbapy.TBA('PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw')
        response = requests.get('https://www.thebluealliance.com/api/v3/team/frc' + str(self.team_num) + '/events/2020', {"X-TBA-Auth-Key": "PzOW8s1DYGlVkgAsikwVlhy5wZ5Tm85fKSjd0DfiUJFQOGhsReyZEf88EEoAU1Cw"})
        response = response.json()
        for name in response:
            n = name['name']
            names.append(n)
        return names

#Profile model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile-pics')

    def __str__(self):
       return f'{self.user.username} Profile'
    