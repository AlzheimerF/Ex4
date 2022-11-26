from rest_framework import serializers
from . import models

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Product
        fields = '__all__'


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Ca
#         fields = '__all__'