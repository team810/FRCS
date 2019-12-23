from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Custom user model

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, team_num, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an username")
        if not team_num:
            raise ValueError("Users must have a team")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            team_num = team_num,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, team_num):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            team_num = team_num,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    team_name = models.CharField(verbose_name='team name', max_length=50, unique=False)
    #Required fields
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'team_name',]

    objects = MyUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, ap_label):
        return True