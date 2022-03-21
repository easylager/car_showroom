from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from core.models import abstract_models
from car.models import Car
from showroom.models import Showroom
from core.models.abstract_models import AbstractOrder

User = get_user_model()


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone_regex = RegexValidator(regex='^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class CustomerOrder(models.Model):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    #customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    required_price = models.DecimalField(decimal_places=2, max_digits=5)


class CustomerHistory(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=5)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
