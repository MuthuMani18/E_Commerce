

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from . models import CartItems
from .serializers import *
from product.models import Product

from my_cart.serializers import CartItemsSerializer

from my_cart.models import CartItems


class CartView(APIView):
    # authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        print(user)
        cart = Cart.objects.filter(user=user, ordered=False).first()

        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        user = request.user
        quantity = data.get('quantity')
        print('data---', data)
        cart, _ = Cart.objects.get_or_create(user=user, ordered=False)
        print(cart)
        product = Product.objects.get(id=data['product'])
        print(product)
        price = product.price
        cart_items = CartItems(cart=cart, user=user,
                               product=product, price=price, quantity=quantity)
        cart_items.save()

        total_price = 0
        cart_items = CartItems.objects.filter(user=user, cart=cart.id)
        for items in cart_items:
            total_price += items.price
        cart.total_price = total_price
        cart.save()
        return Response({'success': "Items added your carts"})

    def put(self, request):
        data = request.data
        cart_item = CartItems.objects.get(id=data['id'])
        quantity = data.get('quantity')
        cart_item.quantity += quantity
        cart_item.save()
        return Response({'success': 'items updated'})

    def delete(self, request):
        user = request.user
        data = request.data

        cart_item = CartItems.objects.get(id=data['id'])
        cart_item.delete()
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItems.objects.filter(cart=cart)
        serializer = CartItemsSerializer(queryset, many=True)
        return Response(serializer.data)
