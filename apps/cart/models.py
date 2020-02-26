import logging

from django.db import models
from django.utils.translation import ugettext_lazy as _

log = logging.getLogger(__name__)

class Cart(models.Model):
    customer = models.ForeignKey(
        'customer.Customer',
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("customer"))
