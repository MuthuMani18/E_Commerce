import imp
from rest_framework import serializers
from order.models import Orders
from my_cart.serializers import CartSerializer


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer

    class Meta:
        model = Orders
        fields = '__all__'
