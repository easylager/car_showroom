from django_filters import rest_framework as filters
from showroom.models import Showroom



class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShowroomFilter(filters.FilterSet):
    location = CharFilterInFilter(field_name='location__city', lookup_expr='in')
    balance = filters.RangeFilter()
    color = filters.CharFilter(
        method='color_filter')

    class Meta:
        model = Showroom
        fields = ['location', 'balance', 'color']

    def color_filter(self, queryset, name, value):
        return queryset.filter(features__color__iexact=value)
