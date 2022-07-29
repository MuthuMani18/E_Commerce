from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

# Create your views here


class ProdectViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        product = Product.objects.all()
        return product
