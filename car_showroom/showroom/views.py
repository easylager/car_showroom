from rest_framework import viewsets, mixins
from showroom.serializers import ShowroomCreateSerializer, ShowroomUpdateSerializer, ShowroomListRetrieveSerializer
from showroom.serializers import LocationSerializer, ShowroomDiscountListRetrieveSerializer, ShowroomDiscountCreateUpdateSerializer
from showroom.models import Showroom, ShowroomDiscount, Location


class LocationViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class ShowroomViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializers = {
        'create': ShowroomCreateSerializer,
        'update': ShowroomUpdateSerializer
    }
    default_serializer_class = ShowroomListRetrieveSerializer
    queryset = Showroom.objects.prefetch_related('cars', 'customers').all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    


class ShowroomDiscountViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializers = {
        'list': ShowroomDiscountListRetrieveSerializer,
        'retrieve': ShowroomDiscountListRetrieveSerializer
    }
    default_serializer_class = ShowroomDiscountCreateUpdateSerializer
    queryset = ShowroomDiscount.objects.select_related('showroom').all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)


