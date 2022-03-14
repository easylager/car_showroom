from django.contrib import admin
from .models import Supplier, SupplierDiscount


@admin.register(SupplierDiscount)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class PersonAdmin(admin.ModelAdmin):
    exclude = ('foundation_year', )


