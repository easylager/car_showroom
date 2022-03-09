from rest_framework import routers
from customer.views import CustomerViewSet, UserViewSet


router = routers.SimpleRouter()
router.register(r'api/customer', CustomerViewSet, basename='customer')
router.register(r'api/registration', UserViewSet, basename='registration')

urlpatterns = router.urls
