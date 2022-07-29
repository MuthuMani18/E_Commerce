from pickletools import read_long1
from . models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = ('id', 'user_id', 'name', 'category', 'price',
                  'stock', 'image', 'color', )
