from rest_framework import serializers
from . import models

class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Shop
        fields = '__all__'

