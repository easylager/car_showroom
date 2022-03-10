from django.contrib import admin
from .models import *

@admin.register(Customer, CustomerHistory)
class PersonAdmin(admin.ModelAdmin):
    pass
