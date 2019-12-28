from django.db import models

# Create your models here.
class Feedback(models.Model):
    first_name = models.CharField(verbose_name="First Name")
    last_name = models.CharField(verbose_name="Last Name")
    message = models.TextField(verbose_name="Message", max_length=100)
