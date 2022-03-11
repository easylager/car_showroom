from django.contrib import admin
from .models import *

@admin.register(CustomerHistory)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name', 'email', 'phone_number')
    list_filter = ('balance', )
    list_editable = ('email', 'phone_number')
    exclude = ('balance',)

    @admin.display(description='name')
    def upper_case_name(self, obj):
        return f'{obj.name.upper()}'
