from rest_framework import routers
from showroom.views import ShowroomViewSet, LocationViewSet, ShowroomDiscountViewSet


router = routers.DefaultRouter()
router.register(r'api/showroom', ShowroomViewSet, basename='showroom')
router.register(r'api/location', LocationViewSet, basename='location')
router.register(r'api/showroom_discount', ShowroomDiscountViewSet, basename='showroom_discount')


urlpatterns = router.urls