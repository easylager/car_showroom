from django.contrib.auth import get_user_model
from django.db import models
from core.models import abstract_models
from core.validators.car import phone_belarus_validator
from car.models import Car
from showroom.models import Showroom

User = get_user_model()


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField()
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone_number = models.CharField(validators=[phone_belarus_validator],
                                    max_length=17,
                                    blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class CustomerHistory(abstract_models.AbstractHistory):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
