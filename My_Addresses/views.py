from warnings import filters
from django.shortcuts import render
from .serialializers import AddressSerializer
from .models import Address
from rest_framework import viewsets
#from rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import permissions
from user import authentication


class AddressViewSet(viewsets.ModelViewSet):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['user_id']
    filter_backends = [SearchFilter]
    search_fields = ['city']
    #filter_backends = [OrderingFilter]
    #ordering_fields = ['name', 'city']
