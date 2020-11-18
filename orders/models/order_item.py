from django.db import models


class OrderItem(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, null=True, blank=True)
    name    = models.CharField(max_length=100)
    price   = models.PositiveIntegerField()
    off     = models.PositiveIntegerField()