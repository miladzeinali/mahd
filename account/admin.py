from django.contrib import admin
from .models import *


class ValidationsCodeadmin(admin.ModelAdmin):
    list_display = ('id','mobile')
    search_fields = ('name',)

class Yearadmin(admin.ModelAdmin):
    list_display = ('year',)
    search_fields = ('year',)

admin.site.register(ValidationCode,ValidationsCodeadmin)
admin.site.register(Year,Yearadmin)