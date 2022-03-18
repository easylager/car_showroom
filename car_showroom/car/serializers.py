from car.models import Car, CarManufacturer
from rest_framework import serializers


class CarManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarManufacturer
        fields = ('name',)


class CarSerializer(serializers.ModelSerializer):
    manufacturer = CarManufacturerSerializer()

    class Meta:
        model = Car
        fields = '__all__'


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'




