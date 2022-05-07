from django.db import models

class Userprofile(models.Model):
    name = models.CharField(max_length=80)
    father = models.CharField(max_length=30)
    birthday = models.CharField(max_length=20)
    birth_place = models.CharField(max_length=35)
    create_card_place = models.CharField(max_length=35)
    Sericard = models.CharField(max_length=35,null=True,blank=True)
    Serialcard = models.CharField(max_length=35,null=True,blank=True)
    Fatherseri = models.CharField(max_length=35,null=True,blank=True)
    Fatherserial = models.CharField(max_length=35,null=True,blank=True)
    Motherseri = models.CharField(max_length=35,null=True,blank=True)
    Motherserial = models.CharField(max_length=35,null=True,blank=True)
    nin = models.CharField(max_length=12)
    home_phone = models.CharField(max_length=35)
    home_code = models.CharField(max_length=35)
    city = models.CharField(max_length=35)
    province = models.CharField(max_length=35)
    address = models.CharField(max_length=100)
    father_name_lastname = models.CharField(max_length=50)
    father_father_name = models.CharField(max_length=50)
    father_nin = models.CharField(max_length=12)
    # father_serial_card = models.CharField(max_length=20)
    # father_create_card_place = models.CharField(max_length=35)
    father_education = models.CharField(max_length=35)
    father_phone = models.CharField(max_length=35)
    father_work = models.CharField(max_length=35)
    father_birth = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=50)
    mother_father_name = models.CharField(max_length=50)
    mother_nin = models.CharField(max_length=12)
    # mother_serial_card = models.CharField(max_length=20)
    mother_create_card_place = models.CharField(max_length=35)
    mother_education = models.CharField(max_length=35)
    mother_phone = models.CharField(max_length=35)
    mother_work = models.CharField(max_length=35)
    mother_phone = models.CharField(max_length=35)
    mother_birth = models.CharField(max_length=20)
    telegram_phone = models.CharField(max_length=35)
    e_place_choices = (
        ('مهد دردانه','مهد دردانه'),
        ('پیش دبستانی یگانه','پیش دبستانی یگانه')
    )
    e_place = models.CharField(choices=e_place_choices,max_length=30,default='مهد دردانه')
    Hand = models.CharField(max_length=35,null=True,blank=True)
    Talagh = models.CharField(max_length=35,null=True,blank=True)
    Shahid = models.CharField(max_length=35,null=True,blank=True)
    Bimeh = models.CharField(max_length=35,null=True,blank=True)
    Farhangi = models.CharField(max_length=35,null=True,blank=True)
    Children = models.CharField(max_length=35,null=True,blank=True)
    Child = models.CharField(max_length=35,null=True,blank=True)
    pay = models.BooleanField(default=False,null=True,blank=True)


    



