from config.celery import app
from showroom.models import Showroom, ShowroomOrder
from supplier.models import Supplier


#celery task in which each showroom finds and buys needed cars from suppliers according to the features
@app.task
def showroom_buy_car():

    for showroom in Showroom.objects.all():
        for supplier in Supplier.objects.all():
            for car in supplier.cars.all():
                if showroom.features == car.features:
                    showroom.cars.add(car)
                    supplier.showrooms.add(showroom)
            supplier.save()
        showroom.save()
        print(showroom, showroom.cars.all())





