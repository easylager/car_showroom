from django.contrib import admin
from .models import Supplier, SupplierDiscount, SupplierHistory


@admin.register(SupplierDiscount, SupplierHistory)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class PersonAdmin(admin.ModelAdmin):
    exclude = ('foundation_year', )


