from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CarManufacturer)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class PersonAdmin(admin.ModelAdmin):
    list_select_related = [
        'manufacturer',
    ]