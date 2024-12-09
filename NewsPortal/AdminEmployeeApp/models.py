from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.


class AdminEmployeeCredentials(models.Model):
    
    profilePhoto=models.ImageField(upload_to='Images/Admin/',null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    phoneNumber=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(blank=True,null=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    role=models.CharField(max_length=50,null=True,blank=True)
    
    
    
   