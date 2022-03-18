from rest_framework import routers
from showroom.views import ShowroomViewSet, LocationViewSet, ShowroomDiscountViewSet


router = routers.DefaultRouter()
router.register(r'showroom', ShowroomViewSet, basename='showroom')
router.register(r'location', LocationViewSet, basename='location')
router.register(r'showroom_discount', ShowroomDiscountViewSet, basename='showroom_discount')


urlpatterns = router.urls