from django.contrib import admin
from .models import *

class Userprofileadmin(admin.ModelAdmin):
    list_display = ('id','name','last_name','home_phone','father_name')
    search_fields = ('name','nin','home_phone')


admin.site.register(Userprofile,Userprofileadmin)