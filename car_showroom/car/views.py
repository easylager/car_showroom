from django.shortcuts import render
from car.serializers import CarManufacturerSerializer, CarSerializer, CarCreateSerializer
from car.models import Car, CarManufacturer
from rest_framework import viewsets, mixins


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
    default_serializer_class = CarSerializer
    serializers = {
        'create': CarCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    queryset = Car.objects.select_related('manufacturer').all()


