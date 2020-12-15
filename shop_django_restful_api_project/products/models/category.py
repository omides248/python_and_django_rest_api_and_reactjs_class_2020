from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _


class CategoryManager(models.Manager):

    def is_active(self):
        return self.get_queryset().filter(active=True)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    image = models.ImageField(upload_to="img/public/products", null=True, blank=True, verbose_name=_("Image"))
    active = models.BooleanField(default=False, verbose_name=_("Active"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    objects = CategoryManager()
    active_objects = CategoryManager()


@receiver(post_save, sender=Category)
def my_signal_1(sender, instance, created, **kwargs):
    print("After save")
    print(instance)
    if created:
        if not instance.active:
            instance.active = True
            instance.save()


@receiver(pre_save, sender=Category)
def my_signal_2(sender, instance, **kwargs):
    print("Before save")
    # print(instance)
