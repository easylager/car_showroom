from django.contrib import admin
from .models import Showroom, ShowroomDiscount, ShowroomHistory, Location


@admin.register(Showroom, ShowroomDiscount, ShowroomHistory, Location)
class PersonAdmin(admin.ModelAdmin):
    pass
