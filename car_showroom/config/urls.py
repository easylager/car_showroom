
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'api/supplier/', include('supplier.urls')),
    path(r'api/car/', include('car.urls')),
    path(r'api/showroom/', include('showroom.urls')),
    path(r'api/customer/', include('customer.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
]
