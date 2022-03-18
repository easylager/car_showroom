from django.contrib import admin
from .models import Showroom, ShowroomOrder, ShowroomDiscount, ShowroomHistory, Location


@admin.register(Showroom, ShowroomOrder, ShowroomDiscount, ShowroomHistory, Location)
class PersonAdmin(admin.ModelAdmin):
    pass
