from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    name        = models.CharField(max_length=100, verbose_name=_("Name"))
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at  = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name