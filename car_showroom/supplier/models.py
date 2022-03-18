from django.db import models
from core.models import abstract_models


class Supplier(abstract_models.CreatedAt):
    name = models.CharField(max_length=100)
    foundation_year = models.DateField()
    cars = models.ManyToManyField('car.Car', null=True, blank=True)
    showrooms = models.ManyToManyField('showroom.Showroom', null=True, blank=True)


class SupplierDiscount(abstract_models.AbstractDiscount):
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE)




