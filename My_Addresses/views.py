from django.shortcuts import render
from .serialializers import AddressSerializer
from .models import Address
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['user_id']
    filter_backends = [SearchFilter]
    search_fields = ['city']
    #filter_backends = [OrderingFilter]
    #ordering_fields = ['name', 'city']
