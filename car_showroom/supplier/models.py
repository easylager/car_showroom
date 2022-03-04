from django.db import models
from car.models import Car
from showroom.models import Showroom
from core.models import abstract_models


class Supplier(abstract_models.IsActive, abstract_models.CreatedAt):
    name = models.CharField(max_length=100)
    foundation_year = models.DateField()
    cars = models.ManyToManyField(Car, null=True, blank=True)
    showrooms = models.ManyToManyField(Showroom, null=True, blank=True)

    def __str__(self):
        return self.name


class SupplierDiscount(abstract_models.AbstractDiscount):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)


class SupplierHistory(abstract_models.AbstractHistory):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

