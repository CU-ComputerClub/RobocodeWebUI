from django.db import models

# Create your models here.

class Signup(models.Model):
    robot_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    date = models.DateTimeField(auto_now_add=True)