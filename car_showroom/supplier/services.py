from django_filters import rest_framework as filters
from supplier.models import Supplier


class SupplierFilter(filters.FilterSet):
    class Meta:
        model = Supplier
        fields = ['cars']