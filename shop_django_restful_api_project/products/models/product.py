from django.db import models


class Product(models.Model):
    tags        = models.ManyToManyField(to="products.Tag")
    category    = models.ForeignKey(to="products.Category", on_delete=models.SET_NULL, null=True, blank=True)
    name        = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price       = models.PositiveIntegerField()
    off         = models.PositiveIntegerField(null=True, blank=True)
    quantity    = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name