from rest_framework import serializers
from showroom.models import Showroom, ShowroomDiscount, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('country', 'city', 'street')


class ShowroomListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ('name', 'location', 'balance', 'cars', 'customers', 'features')


class ShowroomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ('name', 'location', 'balance', 'features')


class ShowroomUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ('name', 'location', 'features')


class ShowroomDiscountListRetrieveSerializer(serializers.ModelSerializer):
    showroom = ShowroomListRetrieveSerializer()

    class Meta:
        model = ShowroomDiscount
        fields = '__all__'


class ShowroomDiscountCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomDiscount
        fields = ('name', 'start_at', 'end_at', 'percent', 'showroom')


