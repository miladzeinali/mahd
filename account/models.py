from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user.name)

class ValidationCode(models.Model):
    mobile = models.CharField(max_length=11,null=True,blank=True)
    validation_code = models.CharField(max_length=6,null=True,blank=True)

class Year(models.Model):
    year = models.CharField(max_length=6,null=True,blank=True)
