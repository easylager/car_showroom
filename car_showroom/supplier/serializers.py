from rest_framework import serializers
from supplier.models import Supplier, SupplierDiscount

class SupplierListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'foundation_year', 'cars', 'showrooms']


class SupplierCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'foundation_year']


class SupplierDiscountListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierDiscount
        fields = ['name', 'start_at', 'end_at', 'percent', 'supplier', 'cars']


class SupplierDiscountCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierDiscount
        fields = ['name', 'start_at', 'end_at', 'percent', 'supplier']
