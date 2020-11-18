from django.db import models


class Product(models.Model):
    tags        = models.ManyToManyField(to="products.Tag")
    category    = models.ForeignKey(to="products.Category", on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    description = models.TextField()
    price       = models.PositiveIntegerField()
    off         = models.PositiveIntegerField()
    quantity    = models.PositiveIntegerField()

    def __str__(self):
        return self.name