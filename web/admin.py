from django.contrib import admin
from .models import *

class Userprofileadmin(admin.ModelAdmin):
    list_display = ('id','name','home_phone','father')
    search_fields = ('name','nin','home_phone')


admin.site.register(Userprofile,Userprofileadmin)