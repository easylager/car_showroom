from rest_framework import viewsets, mixins
from customer.models import Customer
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