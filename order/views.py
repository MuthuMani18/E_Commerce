from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

from order.models import Orders
from order.serializer import OrderSerializer

# Create your views here.


class OrderView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        queryset = Orders.objects.filter(user=request.user)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
