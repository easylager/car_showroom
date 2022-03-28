from rest_framework import routers
from car.views import CarManufacturerViewSet, CarViewSet

router = routers.SimpleRouter()

router.register(r'api/car_manufacturer', CarManufacturerViewSet, basename='car_manufacturer')
router.register(r'api/car', CarViewSet, basename='car')


urlpatterns = router.urls
