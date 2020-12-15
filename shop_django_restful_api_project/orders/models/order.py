import random
import string
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


def set_order_number() -> str:
    str_random = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
    return str_random + '-' + str(int(datetime.datetime.utcnow().timestamp()))


class Order(models.Model):

    REGISTERED_STATUS = '1'
    DELIVERED_STATUS = '2'
    LOADING_STATUS = '3'
    SENDING_STATUS = '4'
    CLEARED_STATUS = '5'

    ORDER_STATUS = (
        (REGISTERED_STATUS, _('Order is begin registered')),
        (DELIVERED_STATUS, _('Delivered to the sales unit')),
        (LOADING_STATUS, _('Loading')),
        (SENDING_STATUS, _('Sending')),
        (CLEARED_STATUS, _('Cleared')),
    )

    order_number    = models.CharField(max_length=100, default=set_order_number, verbose_name=_("Order number"))
    order_status    = models.CharField(choices=ORDER_STATUS, max_length=1, default=REGISTERED_STATUS, verbose_name=_('Order status'))
    total_cost      = models.PositiveIntegerField(verbose_name=_("Total cost"))
    off             = models.PositiveIntegerField(verbose_name=_("Off"))
    phone_number    = PhoneNumberField(verbose_name=_("Phone number"), null=True, blank=True)
    first_name      = models.CharField(max_length=100, verbose_name=_("First name"))
    last_name       = models.CharField(max_length=100, verbose_name=_("last name"))
    created_at      = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at      = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.order_number



