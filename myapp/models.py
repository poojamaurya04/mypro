from django.db import models

# Create your models here.
class pooja(models.Model):
    ID=models.CharField(max_length=10,primary_key=True)
    FULL_NAME=models.CharField(max_length=30)
    EMAIL_ADDRESS=models.CharField(max_length=30)
    MOBILE_NUMBER=models.CharField(max_length=10)
    DOB=models.CharField(max_length=20)
    ADDRESS=models.CharField(max_length=40)
