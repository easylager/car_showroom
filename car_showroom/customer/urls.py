from rest_framework import routers
from customer.views import CustomerViewSet, CustomerOrderViewSet
from customer.views import RegisterViewSet

router = routers.SimpleRouter()
router.register(r'api/customer', CustomerViewSet, basename='customer')
router.register(r'api/registration', RegisterViewSet, basename='registration')
router.register(r'api/customer_order', CustomerOrderViewSet, basename='customer_order')
#router.register(r'api/email_verify', VerifyEmailSet, basename='verify')

urlpatterns = router.urls
