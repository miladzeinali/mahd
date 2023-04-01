from django.contrib import admin
from .models import *

class Userprofileadmin(admin.ModelAdmin):
    list_display = ('id','name','home_phone','father')
    search_fields = ('name','nin','home_phone')

class ValidationsCodeadmin(admin.ModelAdmin):
    list_display = ('id','mobile')
    search_fields = ('name',)


admin.site.register(Userprofile,Userprofileadmin)
admin.site.register(ValidationCode,ValidationsCodeadmin)