from django.db import models
from core.enums.car import CarType


class CarManufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(CarManufacturer, on_delete=models.CASCADE)
    car_type = models.CharField(max_length=100, choices=CarType.choices())
    model = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, null=True)
    features = models.JSONField()

    def __str__(self):
        return f'{self.manufacturer}{self.model}'




