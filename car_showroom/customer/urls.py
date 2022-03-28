from rest_framework import routers
from customer.views import CustomerViewSet, UserViewSet, CustomerOrderViewSet


router = routers.SimpleRouter()
router.register(r'api/customer', CustomerViewSet, basename='customer')
router.register(r'api/registration', UserViewSet, basename='registration')
router.register(r'api/customer_order', CustomerOrderViewSet, basename='customer_order')

urlpatterns = router.urls
