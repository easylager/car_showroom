from django.contrib import admin
from .models import Showroom, ShowroomCar, ShowroomOrder, ShowroomDiscount, ShowroomHistory, Location


@admin.register(Showroom, ShowroomCar, ShowroomOrder, ShowroomDiscount, ShowroomHistory, Location)
class PersonAdmin(admin.ModelAdmin):
    pass
