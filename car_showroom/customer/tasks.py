from config.celery import app
from customer.models import Customer, CustomerOrder, CustomerHistory
from showroom.models import Showroom, ShowroomCar


#this function runs in moment of creating instance of CustomerOrder model
#customer finds cheapest needed car buys it and transfer added to CustomerModel table
def customer_buys_car(order):
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


#if car was not found at the time of purchase this task find try to make transaction again
@app.task
def customers_buy_cars():
    for order in CustomerOrder.objects.all():
        customer_buys_car(order=order)








