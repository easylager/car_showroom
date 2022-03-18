from django.contrib import admin
from .models import Showroom, ShowroomDiscount, ShowroomHistory, Location


@admin.register(ShowroomDiscount, ShowroomHistory)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Showroom)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ('location', 'balance')
    empty_value_display = '-empty-;'
    list_display = ('name', 'location', 'features')


@admin.register(Location)
class PersonalAdmin(admin.ModelAdmin):
    list_filter = ('country',)
