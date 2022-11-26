from django.db import models
from products.models import Product

class CheckerForSelling(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date_selling = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


    def __str__(self):
        return self.title

class CheckerForBuying(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date_buying = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

