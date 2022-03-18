from django.contrib import admin
from car.models import Car, CarManufacturer


@admin.register(CarManufacturer)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class PersonAdmin(admin.ModelAdmin):
    list_select_related = [
        'manufacturer',
    ]