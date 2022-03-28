from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from customer.tasks import customer_buys_car
from customer.models import Customer, CustomerOrder
from customer.serializers import CustomerSerializer, UserSerializer, CustomerOrderSerializer


class CustomerViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class UserViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = Customer.objects.all()


class CustomerOrderViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CustomerOrderSerializer
    queryset = CustomerOrder.objects.all()

    #customer_buys_car is called here and finds car to just created customer order
    def perform_create(self, serializer):
        order = serializer.save()
        customer_buys_car(order=order)
