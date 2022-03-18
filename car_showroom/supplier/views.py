from rest_framework import viewsets, mixins, status
from supplier.serializers import SupplierCreateUpdateSerializer, SupplierListRetrieveSerializer, \
    SupplierDiscountListRetrieveSerializer, SupplierDiscountCreateUpdateSerializer
from supplier.models import Supplier, SupplierDiscount


class SupplierViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializers = {
        'list': SupplierListRetrieveSerializer,
        'retrieve': SupplierListRetrieveSerializer,
    }
    default_serializer_class = SupplierCreateUpdateSerializer
    queryset = Supplier.objects.prefetch_related('cars', 'showrooms').all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)


class SupplierDiscountViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    default_serializer_class = SupplierDiscountCreateUpdateSerializer
    serializers = {
        'list': SupplierDiscountListRetrieveSerializer,
        'retrieve': SupplierDiscountListRetrieveSerializer,
    }
    queryset = SupplierDiscount.objects.select_related('supplier').prefetch_related('cars').all()

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer_class)

    
