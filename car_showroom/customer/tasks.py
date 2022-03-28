from config.celery import app
from customer.models import Customer, CustomerOrder, CustomerHistory
from showroom.models import Showroom, ShowroomCar



#customers finds cheapest needed cars, buy it and transfer added to CustomerHistory table
@app.task
def customers_buy_cars():
    for order in CustomerOrder.objects.all():
        result_car = order.find_car
        if isinstance(result_car, ShowroomCar):
            customer = order.customer
            if customer.balance >= result_car.discount_price:
                customer.balance -= result_car.price
                history = CustomerHistory.objects.create(car=result_car.car,
                                                         customer=customer,
                                                         showroom=result_car.showroom,
                                                         price=result_car.discount_price)
                history.save()
                customer.save()
                order.delete()








