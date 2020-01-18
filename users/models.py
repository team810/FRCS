from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail
from django.utils.http import urlquote
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .templates import users
import random
import string
import smtplib

#Custom user model
class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, team_num, password=None):
        if not email:
            raise ValueError("Email must be present")

        email = self.normalize_email(email)
        user = self.model(
                username = username,
                email = self.normalize_email(email),
                team_num = team_num,
            )
        user.set_password(password)
        self.create_VID()
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

    def create_VID(self):
        n = 7
        self.VID = str(''.join(random.choices(string.ascii_uppercase + string.digits, k = n)))

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=254, unique=True)
    #first_name = models.CharField(verbose_name="First Name", max_length=254)
    #last_name = models.CharField(verbose_name="Last Name", max_length=254, blank=True)
    #team_name = models.CharField(verbose_name="Team Name", max_length=254)
    team_num = models.IntegerField(verbose_name="Team Number")
    email = models.EmailField(unique=True)
    VID = models.CharField(max_length = 254, unique=True, null=True)

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

    def create_VID(self):
        n = 7
        return str(''.join(random.choices(string.ascii_uppercase + string.digits, k = n)))

    def email_verify(self):
        template = """<!DOCTYPE html>
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <link href="https://fonts.googleapis.com/css?family=Poppins:100,200,300,400,500,600,700,800,900&display=swap" rel="stylesheet">
        <style type="text/css" rel="stylesheet" media="all">
            body {
            width: 100% !important;
            height: 100%;
            margin: 0;
            line-height: 1.4;
            background-color: #F5F7F9;
            color: #839197;
            -webkit-text-size-adjust: none;
            font-family: 'poppins', 'sans-serif'
            }
            a {
            color: #414EF9;
            }
            /* Layout ------------------------------ */
            .email-wrapper {
            width: 100%;
            margin: 0;
            padding: 0;
            background-color: #F5F7F9;
            }
            .email-content {
            width: 100%;
            margin: 0;
            padding: 0;
            }
            /* Masthead ----------------------- */
            .email-masthead {
            padding: 25px 0;
            text-align: center;
            }
            .email-masthead_logo {
            max-width: 400px;
            border: 0;
            }
            .email-masthead_name {
            font-size: 16px;
            font-weight: bold;
            color: #839197;
            text-decoration: none;
            text-shadow: 0 1px 0 white;
            }
            /* Body ------------------------------ */
            .email-body {
            width: 100%;
            margin: 0;
            padding: 0;
            border-top: 1px solid #E7EAEC;
            border-bottom: 1px solid #E7EAEC;
            background-color: #FFFFFF;
            }
            .email-body_inner {
            width: 570px;
            margin: 0 auto;
            padding: 0;
            }
            .email-footer {
            width: 570px;
            margin: 0 auto;
            padding: 0;
            text-align: center;
            }
            .email-footer p {
            color: #839197;
            }
            .body-action {
            width: 100%;
            margin: 30px auto;
            padding: 0;
            text-align: center;
            }
            .body-sub {
            margin-top: 25px;
            padding-top: 25px;
            border-top: 1px solid #E7EAEC;
            }
            .content-cell {
            padding: 35px;
            }
            .align-right {
            text-align: right;
            }
            /* Type ------------------------------ */
            h1 {
            margin-top: 0;
            color: #292E31;
            font-size: 19px;
            font-weight: bold;
            text-align: left;
            }
            h2 {
            margin-top: 0;
            color: #292E31;
            font-size: 16px;
            font-weight: bold;
            text-align: left;
            }
            h3 {
            margin-top: 0;
            color: #292E31;
            font-size: 14px;
            font-weight: bold;
            text-align: left;
            }
            p {
            margin-top: 0;
            color: #839197;
            font-size: 16px;
            line-height: 1.5em;
            text-align: left;
            }
            p.sub {
            font-size: 12px;
            }
            p.center {
            text-align: center;
            }
            /* Buttons ------------------------------ */
            .button {
            display: inline-block;
            width: 200px;
            background-color: lightblue;
            border-radius: 5px;
            color: #ffffff;
            font-size: 15px;
            line-height: 45px;
            text-align: center;
            font-weight: bold;
            text-decoration: none;
            -webkit-text-size-adjust: none;
            mso-hide: all;
            border-color: transparent;
            }
            /*Media Queries ------------------------------ */
            @media only screen and (max-width: 600px) {
            .email-body_inner,
            .email-footer {
                width: 100% !important;
            }
            }
            @media only screen and (max-width: 500px) {
            .button {
                width: 100% !important;
            }
            }
            #title{
                font-size: 40px;
            }
        </style>
        </head>
        <body>

        <table class="email-wrapper" width="100%" cellpadding="0" cellspacing="0">
            <tr>
            <td align="center">
                <table class="email-content" width="100%" cellpadding="0" cellspacing="0">
                <!-- Logo -->
                <tr>
                    <td class="email-masthead">
                    </td>
                </tr>
                <!-- Email Body -->
                <tr>
                    <td class="email-body" width="100%">
                    <table class="email-body_inner" align="center" width="570" cellpadding="0" cellspacing="0">
                        <!-- Body content -->
                        <tr>
                        <td class="content-cell">
                        <h1 id="title"><strong>FRCS</strong></h1>
                            <h1>Verify your email address</h1>
                            <p>Thanks for signing up for FRCS! We're excited to have you as a user.</p>
                            <!-- Action -->
                            <table class="body-action" align="center" width="100%" cellpadding="0" cellspacing="0">
                            <tr>
                                <td align="center">
                                <div>
                                    <form action="frcs.online/verify">
                                    <button class="button" type="submit">Click me</button>
                                    </form>
                                </div>
                                </td>
                            </tr>
                            </table>
                            <p>Thanks,<br>The FRCS Team</p>
                            <!-- Sub copy -->
                            <table class="body-sub">
                            <tr>
                                <td>
                                <p class="sub">If you’re having trouble clicking the button, copy and paste the URL below into your web browser.
                                </p>
                                </td>
                            </tr>
                            </table>
                        </td>
                        </tr>
                    
            </td>
            </tr>
        </table>
        </body>
        </html>"""
        msg = MIMEMultipart('alternative')
        htmly = MIMEText(template, 'html')
        msg.attach(htmly)       
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login("frcsassistant@gmail.com", "zikpniouyggoqfmk")
            smtp.sendmail('frcsassistant@gmail.com','frcsassistant@gmail.com', msg.as_string())

#Profile model
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile-pics')

    def __str__(self):
       return f'{self.user.username} Profile'
    