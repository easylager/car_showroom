from django.db import models
from django_countries.fields import CountryField
from car.models import Car
from core.models import abstract_models
import random



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
    cars = models.ManyToManyField(Car, null=True, blank=True, through='ShowroomCar')
    customers = models.ManyToManyField('customer.Customer', null=True, blank=True)

    def __str__(self):
        return self.name


def random_price():
    return random.randint(10, 300)


class ShowroomCar(models.Model):
    showroom = models.ForeignKey('showroom.Showroom', on_delete=models.CASCADE)
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=random_price)
    discount_price = models.FloatField(default=0)

    #property counts discount price of the car according to the best current promotion in the showroom
    @property
    def discount_price(self):
        percent = ShowroomDiscount.objects.filter(
            showroom=self.showroom).filter(
            cars=self.car,
        ).order_by('percent')[0].percent
        if percent:
            return self.price - (self.price * percent / 100)
        else:
            return self.price

    def __str__(self):
        return f'{self.car}-{self.price}'

    '''def save(self, *args, **kwargs):
        if not self.discount_price:
            percent = ShowroomDiscount.objects.get(
                showroom=self.showroom,
                cars=self.car).order_by('percent').percent
            if percent:
                self.discount_price = (self.price * percent / 100) + self.price
            else:
                self.discount_price = self.price
        super(ShowroomCar, self).save(*args, **kwargs)'''

    '''def random_price(self):
        discount_model = ShowroomDiscount.objects.get(showroom=self.showroom, cars_in=self.car)
        percent = discount_model.percent
        self.price = random.randint(10, 300) * percent/100
        return self.price'''


class ShowroomOrder(abstract_models.AbstractOrder):
    showroom = models.ForeignKey('showroom.Showroom', on_delete=models.CASCADE)


class ShowroomDiscount(abstract_models.AbstractDiscount):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)


class ShowroomHistory(abstract_models.AbstractHistory):
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE)
