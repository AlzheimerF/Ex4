from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from . import models, serializers
from checker.models import CheckerForSelling, CheckerForBuying

class ProductViewSet(viewsets.ModelViewSet):

    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductsSerializer
    permission_classes = [AllowAny, ]

    @action(detail=False, methods=['post'])
    def sell(self, request):
        product = models.Product.objects.get(id=request.data.get('id'))
        if product.quantity < int(request.data.get('quantity')):
            return Response(f'В данный момент продукта на складе не достаточно. ' 
                            f'Если вы хотите совершить покупку измените количество ' 
                            f'продукта в следующем диапазоне: 0 - {product.quantity} !')
        product.quantity = product.quantity - int(request.data.get('quantity'))
        product.save()
        checker_s = CheckerForSelling.objects.create(
            title=product.title,
            quantity=int(request.data.get('quantity')),
            product=product,
        )
        checker_s.save()
        return Response('Покупка совершенна!')

    @action(detail=False, methods=['get'])
    def buy(self):
        all_products = models.Product.objects.all()
        for product in all_products:
            quantity_buying = 100 - int(product.quantity)
            product.quantity += quantity_buying
            product.save()
            statistic = CheckerForBuying.objects.create(
                title=product.title,
                quantity=quantity_buying,
                product=product
            )
            statistic.save()
        return Response(
            'Пополнение товаров на складе завершенно!'
        )