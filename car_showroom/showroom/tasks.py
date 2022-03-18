from config.celery import app
from celery.task import periodic_task, task

from celery.schedules import crontab
from showroom.models import Showroom, ShowroomOrder
from supplier.models import Supplier


#@periodic_task(run_every=(crontab(minute=('*/1'))), name='my_task')
#@task(name='check_cars_task')
@app.task
def check_cars():

    for showroom in Showroom.objects.all():
        for supplier in Supplier.objects.all():
            for car in supplier.cars.all():
                if showroom.features == car.features:
                    showroom.cars.add(car)
                    supplier.showrooms.add(showroom)
            supplier.save()
        showroom.save()
        print(showroom, showroom.cars.all())



def make_offer(querydict):
    if len(querydict) != 0:
        for key, value in querydict.items():
            ShowroomOrder.objects.create(showroom=key, cars=value)

