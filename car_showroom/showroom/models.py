from django.db import models
from django_countries.fields import CountryField
from car.models import Car

from core.models import abstract_models


class Location(models.Model):
    country = CountryField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.country}-{self.city}-{self.street}'


class Showroom(models.Model):
    name = models.CharField(max_length=80)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=5)
    features = models.JSONField()
    cars = models.ManyToManyField(Car, null=True, blank=True)
    customers = models.ManyToManyField('customer.Customer', null=True, blank=True)

    def __str__(self):
        return self.name


class ShowroomDiscount(abstract_models.AbstractDiscount):
    showroom = models.ForeignKey(Showroom,
                                 on_delete=models.CASCADE)


class ShowroomHistory(abstract_models.AbstractHistory):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
