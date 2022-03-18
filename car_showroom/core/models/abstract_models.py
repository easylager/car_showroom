from django.db import models



class IsActive(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CreatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True


'''class UpdatedAt(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True'''


class AbstractDiscount(models.Model):
    name = models.CharField(max_length=100)
    start_at = models.DateTimeField(auto_now_add=True, blank=True)
    end_at = models.DateTimeField(blank=True)
    percent = models.DecimalField(decimal_places=2, max_digits=4)
    cars = models.ManyToManyField('car.Car')

    class Meta:
        abstract = True


class AbstractHistory(models.Model):
    car = models.ForeignKey('car.Car', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        abstract = True