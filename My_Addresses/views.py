from django.shortcuts import render
from .serialializers import AddressSerializer
from .models import Address
from rest_framework import viewsets


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer
   