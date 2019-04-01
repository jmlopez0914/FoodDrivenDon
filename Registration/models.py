from django.db import models
from datetime import datetime, timedelta
# Create your models here.

#Class - Registrant
#variables - name, email, address, pickup time, pickup date

class Registrant(models.Model):
    full_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    home_Address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 20)
    pickup_date = models.CharField(max_length = 15)

    def __str__(self):
        return self.full_name

class Question(models.Model):
    question = models.CharField(max_length = 1000)
    email = models.CharField(max_length = 255)
    def __str__(self):
        return self.question
