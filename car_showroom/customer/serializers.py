from rest_framework import serializers
from customer.models import Customer, CustomerOrder, User



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']



'''class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'''
