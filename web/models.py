from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    name = models.CharField(max_length=80,null=True,blank=True)
    last_name = models.CharField(max_length=80,null=True,blank=True)
    father = models.CharField(max_length=30,null=True,blank=True)
    birthday = models.CharField(max_length=20,null=True,blank=True)
    birth_place = models.CharField(max_length=35,null=True,blank=True)
    create_card_place = models.CharField(max_length=35,null=True,blank=True)
    Sericard = models.CharField(max_length=35,null=True,blank=True)
    Serialcard = models.CharField(max_length=35,null=True,blank=True)
    Fatherseri = models.CharField(max_length=35,null=True,blank=True)
    Fatherserial = models.CharField(max_length=35,null=True,blank=True)
    Motherseri = models.CharField(max_length=35,null=True,blank=True)
    Motherserial = models.CharField(max_length=35,null=True,blank=True)
    nin = models.CharField(max_length=12,null=True,blank=True)
    home_phone = models.CharField(max_length=35,null=True,blank=True)
    home_code = models.CharField(max_length=35,null=True,blank=True)
    city = models.CharField(max_length=35,null=True,blank=True)
    province = models.CharField(max_length=35,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    # father_name_lastname = models.CharField(max_length=50,null=True,blank=True)
    father_father_name = models.CharField(max_length=50,null=True,blank=True)
    father_nin = models.CharField(max_length=12,null=True,blank=True)
    father_education = models.CharField(max_length=35,null=True,blank=True)
    father_phone = models.CharField(max_length=35,null=True,blank=True)
    father_work = models.CharField(max_length=35,null=True,blank=True)
    father_birth = models.CharField(max_length=20,null=True,blank=True)
    mother_name = models.CharField(max_length=50,null=True,blank=True)
    mother_father_name = models.CharField(max_length=50,null=True,blank=True)
    mother_nin = models.CharField(max_length=12,null=True,blank=True)
    # mother_create_card_place = models.CharField(max_length=35,null=True,blank=True)
    mother_education = models.CharField(max_length=35,null=True,blank=True)
    mother_phone = models.CharField(max_length=35,null=True,blank=True)
    mother_work = models.CharField(max_length=35,null=True,blank=True)
    mother_phone = models.CharField(max_length=35,null=True,blank=True)
    mother_birth = models.CharField(max_length=20,null=True,blank=True)
    telegram_phone = models.CharField(max_length=35,null=True,blank=True)
    e_place_choices = (
        ('مهد شکوفه','مهد شکوفه'),
        ('پیش دبستانی بهاران','پیش دبستانی بهاران')
    )
    e_place = models.CharField(choices=e_place_choices,max_length=30,null=True,blank=True)
    Hand = models.CharField(max_length=35,null=True,blank=True)
    Talagh = models.CharField(max_length=35,null=True,blank=True)
    Shahid = models.CharField(max_length=35,null=True,blank=True)
    Bimeh = models.CharField(max_length=35,null=True,blank=True)
    Farhangi = models.CharField(max_length=35,null=True,blank=True)
    Children = models.CharField(max_length=35,null=True,blank=True)
    Child = models.CharField(max_length=35,null=True,blank=True)
    credit = models.PositiveIntegerField(default=0,null=True,blank=True)
    pay = models.BooleanField(default=False,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    yearadded = models.CharField(max_length=6,null=True,blank=True,default='1401')


    



