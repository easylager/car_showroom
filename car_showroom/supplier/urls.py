from rest_framework import routers
from supplier.views import SupplierViewSet, SupplierDiscountViewSet


router = routers.SimpleRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'supplier_discount', SupplierDiscountViewSet, basename='supplier_discount')


urlpatterns = router.urls