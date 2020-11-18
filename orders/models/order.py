from django.db import models


class Order(models.Model):
    order_number    = models.CharField(max_length=100)
    total_cost      = models.PositiveIntegerField()
    off             = models.PositiveIntegerField()
    username        = models.CharField(max_length=100)
    first_name      = models.CharField(max_length=100)
    last_name       = models.CharField(max_length=100)
