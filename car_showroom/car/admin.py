from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Car, CarManufacturer)
class PersonAdmin(admin.ModelAdmin):
    pass