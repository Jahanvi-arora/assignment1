from django.db import models

# Create your models here.

class UserRegistrationModel(models.Model):
    user_name = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=50)
