
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path(r'', include('supplier.urls')),
    path(r'', include('car.urls')),
    path(r'', include('showroom.urls')),
    path(r'', include('customer.urls')),
    path('__debug__/', include('debug_toolbar.urls'))
]
