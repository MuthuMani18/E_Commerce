from rest_framework import serializers
from . models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'user_id', 'name', 'phone_no', 'pincode',
                  'state', 'city', 'house_no', 'street_name')
