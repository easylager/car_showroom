from django_filters import rest_framework as filters
from car.models import Car



class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CarFilter(filters.FilterSet):
    manufacturer = CharFilterInFilter(field_name='manufacturer__name', lookup_expr='in')
    car_type = filters.CharFilter(lookup_expr='iexact')
    color = filters.CharFilter(
        method='color_filter')

    class Meta:
        model = Car
        fields = ['manufacturer', 'car_type', 'color']

    def color_filter(self, queryset, name, value):
        return queryset.filter(features__color__iexact=value)
