from django.db import models
from shop.models import Shop

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return self.title
