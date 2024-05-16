from django.db import models

# Create your models here.

class Client(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)  
    user_address = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
