from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models, serializers
from products.serializers import ProductsSerializer
from products.models import Product


class ShopViewSet(viewsets.ModelViewSet):

    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    permission_classes = [AllowAny, ]

    @action(detail=True, methods=['get'])
    def about_shop(self, request, *args, **kwargs):
        serializer1 = serializers.ShopSerializer(models.Shop.objects.get(id=kwargs.get('pk')))
        serializer2 = ProductsSerializer(Product.objects.filter(shop_id=kwargs.get('pk')), many=True)
        return Response([serializer1.data, serializer2.data])

