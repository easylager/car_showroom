from django.contrib import admin
from .models import Customer, CustomerHistory, CustomerOrder

@admin.register(Customer, CustomerHistory, CusotmerOrder)
class PersonAdmin(admin.ModelAdmin):
    pass
