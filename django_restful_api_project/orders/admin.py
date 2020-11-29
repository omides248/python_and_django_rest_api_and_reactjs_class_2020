from django.contrib import admin

from orders.models.order import Order
from orders.models.order_item import OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)
