from django.contrib import admin
from .models import Supplier, SupplierDiscount, SupplierHistory


@admin.register(Supplier, SupplierDiscount, SupplierHistory)
class PersonAdmin(admin.ModelAdmin):
    pass
