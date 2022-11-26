from django.test import TestCase
from .models import Shop, Product
from .views import ProductViewSet

class ProductTest(TestCase):

    def setUp(self):
        for i in range(1, 11):
            shop = Shop.objects.create(
                title='hello, from testing !',
                description='jflsdjflsdj',
            )
            product = Product.objects.create(
                title='hello, from testing !',
                description='jflsdjflsdj',
                quantity=12,
                shop=shop
            )

    def test_quaryset_exists(self):
        quaryset = Shop.objects.all()
        self.assertTrue(quaryset.exists())

    def test_count_product(self):
        self.assertEqual(Shop.objects.count(), 10)

    def test_check_id(self):
        self.assertEqual(Shop.objects.first().id, 1)
        self.assertEqual(Shop.objects.last().id, 10)

    def test(self):
        a = ProductViewSet()
        self.assertEqual(str(a.buy()), '<Response status_code=200, "text/html; charset=utf-8">' )
