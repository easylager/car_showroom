from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from customer.models import Customer, CustomerOrder, User
from rest_framework.generics import GenericAPIView
from customer.serializers import CustomerSerializer, UserSerializer, CustomerOrderSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from customer.utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class CustomerViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class RegisterViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse('verify')

        absurl = 'http//' + current_site + relativeLink + '?token=' + str(token)
        email_body = 'Hi ' + user.username + 'Use link below to verify your email \n' + absurl
        data = {
            'email_body': email_body,
            'to_email': user.email,
            'email_subject': 'Verify your email'}
        Util.send_email(data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


'''class VerifyEmailSet(GenericAPIView):
    def get(self):
        pass'''


'''class UserViewSet(mixins.ListModedlMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = Customer.objects.all()'''


class CustomerOrderViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = CustomerOrderSerializer
    queryset = CustomerOrder.objects.all()
