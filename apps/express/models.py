from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save

from ..order.models import Order
from ..customer.models import Address


@python_2_unicode_compatible
class ExpressCarrier(models.Model):
    name_cn = models.CharField(_('name_cn'), max_length=50, null=False, blank=False)
    name_en = models.CharField(_('name_en'), max_length=50, null=True, blank=True)
    website = models.URLField(_('Website'), blank=True, null=True)
    search_url = models.URLField(_('Search url'), blank=True, null=True)
    rate = models.DecimalField(_('Rate'), max_digits=6, decimal_places=2, blank=True, null=True)
    is_default = models.BooleanField('Default', default=False)

    class Meta:
        verbose_name_plural = _('Express Carrier')
        verbose_name = _('Express Carrier')

    def __str__(self):
        return '%s' % self.name_cn


@python_2_unicode_compatible
class ExpressOrder(models.Model):
    carrier = models.ForeignKey(ExpressCarrier, blank=True, null=True, verbose_name=_('carrier'))
    track_id = models.CharField(_('Track ID'), max_length=30, null=False, blank=False)
    order = models.ForeignKey(Order, blank=False, null=False, verbose_name=_('order'), related_name='express_orders')
    address = models.ForeignKey(Address, blank=True, null=True, verbose_name=_('address'))
    fee = models.DecimalField(_('Shipping Fee'), max_digits=8, decimal_places=2,
                              blank=True, null=True)
    weight = models.DecimalField(_('Weight'), max_digits=8, decimal_places=2, blank=True,
                                 null=True)
    id_upload = models.BooleanField(_('ID uploaded'), default=False, null=False, blank=False)
    remarks = models.CharField(_('Remarks'), max_length=128, null=True, blank=True)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True, editable=True)

    class Meta:
        verbose_name_plural = _('Express Order')
        verbose_name = _('Express Order')
        unique_together = ('carrier', 'track_id')

    def __str__(self):
        return '[%s]%s' % (self.carrier.name_cn, self.track_id)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.carrier:
            self.carrier = ExpressCarrier.objects.filter(is_default=True).first()

        if not self.address and self.order and self.order.address:
            self.address = self.order.address
        return super(ExpressOrder, self).save()

    def get_track_url(self):
        if self.remarks and self.remarks.startswith('http'):
            return self.remarks
        elif '%s' in self.carrier.search_url:
            return self.carrier.search_url % self.track_id
        else:
            return None

    def get_tracking_link(self):
        if self.id_upload:
            return '<a target="_blank" href="%s">%s</a>' % (self.get_track_url(), self.track_id)
        else:
            return '<a target="_blank" href="%s"><i><b>%s</b></i></a>' % (self.get_track_url(), self.track_id)

    get_tracking_link.allow_tags = True
    get_tracking_link.short_description = 'Express Track'

    def get_order_link(self):
        return self.order.get_link()

    get_order_link.allow_tags = True
    get_order_link.short_description = 'Order'

    def get_address(self):
        return self.order.address


@receiver(post_save, sender=ExpressOrder)
def update_order_price(sender, instance=None, created=False, **kwargs):
    if instance.order and instance.order.id:
        instance.order.update_price()


@receiver(pre_save, sender=ExpressCarrier)
def update_default_carrier(sender, instance=None, created=False, **kwargs):
    if instance.is_default:
        ExpressCarrier.objects.all().update(is_default=False)
