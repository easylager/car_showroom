from django.shortcuts import render
from car.serializers import CarManufacturerSerializer, CarSerializer, CarCreateSerializer
from car.models import Car, CarManufacturer
from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from car.services import CarFilter


class CarManufacturerViewSet(
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                viewsets.GenericViewSet, ):
    serializer_class = CarManufacturerSerializer
    queryset = CarManufacturer.objects.all()


class CarViewSet(
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                viewsets.GenericViewSet,
                ):
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = CarFilter
    search_fields = ['car_type']
    ordering_fields = ['car_type', 'manufacturer']

    default_serializer_class = CarSerializer
    serializers = {
        'create': CarCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    queryset = Car.objects.select_related('manufacturer').all()


