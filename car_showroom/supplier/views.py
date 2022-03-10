from rest_framework import viewsets, mixins, filters
from supplier.serializers import SupplierCreateUpdateSerializer, SupplierListRetrieveSerializer, \
    SupplierDiscountListRetrieveSerializer, SupplierDiscountCreateUpdateSerializer
from supplier.models import Supplier, SupplierDiscount
from supplier.services import SupplierFilter
from django_filters.rest_framework import DjangoFilterBackend


class SupplierViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):
    serializers = {
        'list': SupplierListRetrieveSerializer,
        'retrieve': SupplierListRetrieveSerializer,
    }
    default_serializer_class = SupplierCreateUpdateSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = SupplierFilter
    search_fields = ['cars']


    queryset = Supplier.objects.all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)


class SupplierDiscountViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              viewsets.GenericViewSet):
    default_serializer_class = SupplierDiscountCreateUpdateSerializer
    serializers = {
        'list': SupplierDiscountListRetrieveSerializer,
        'retrieve': SupplierDiscountListRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    queryset = SupplierDiscount.objects.select_related('supplier').prefetch_related('cars').all()
