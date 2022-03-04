from rest_framework import routers
from customer.views import CustomerViewSet


router = routers.SimpleRouter()
router.register(r'api/customer', CustomerViewSet, basename='customer')

urlpatterns = router.urls
