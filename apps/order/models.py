# coding=utf-8
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.utils.crypto import get_random_string

from utils.enum import enum
from settings.settings import rate
from ..product.models import Product
from ..customer.models import Customer, Address
from ..store.models import Store

ORDER_STATUS = enum('CREATED', 'SHIPPING', 'DELIVERED', 'FINISHED')

ORDER_STATUS_CHOICES = (
    (ORDER_STATUS.CREATED, u'创建'),
    (ORDER_STATUS.SHIPPING, u'在途'),
    (ORDER_STATUS.DELIVERED, u'寄达'),
    (ORDER_STATUS.FINISHED, u'完成'),
)


@python_2_unicode_compatible
class Order(models.Model):
    customer = models.ForeignKey(Customer, blank=False, null=False, verbose_name=_('customer'))
    address = models.ForeignKey(Address, blank=True, null=True, verbose_name=_('address'))
    is_paid = models.BooleanField(default=False, verbose_name=_('paid'))
    paid_time = models.DateTimeField(auto_now_add=False, editable=True, blank=True, null=True,
                                     verbose_name=_(u'Paid Time'))
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS.CREATED,
                              verbose_name=_('status'))
    total_amount = models.IntegerField(_(u'Amount'), default=0, blank=False, null=False)
    product_cost_aud = models.DecimalField(_(u'Product Cost AUD'), max_digits=8, decimal_places=2, blank=True,
                                           null=True)
    product_cost_rmb = models.DecimalField(_(u'Product Cost RMB'), max_digits=8,
                                           decimal_places=2, blank=True, null=True)
    shipping_fee = models.DecimalField(_(u'Shipping Fee'), max_digits=8, decimal_places=2, blank=True, null=True)
    ship_time = models.DateTimeField(auto_now_add=False, editable=True, blank=True, null=True,
                                     verbose_name=_(u'Ship Time'))
    total_cost_aud = models.DecimalField(_(u'Total Cost AUD'), max_digits=8, decimal_places=2, blank=True, null=True)
    total_cost_rmb = models.DecimalField(_(u'Total Cost RMB'), max_digits=8, decimal_places=2, blank=True, null=True)
    origin_sell_rmb = models.DecimalField(_(u'Origin Sell RMB'), max_digits=8, decimal_places=2, blank=True,
                                          null=True)
    sell_price_rmb = models.DecimalField(_(u'Final RMB'), max_digits=8, decimal_places=2, blank=True, null=True)
    profit_rmb = models.DecimalField(_(u'Profit RMB'), max_digits=8, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField(_(u'Create Time'), auto_now_add=True, editable=False)
    finish_time = models.DateTimeField(_(u'Finish Time'), editable=True, blank=True, null=True)

    def __str__(self):

        return '[%s]%s' % (self.id or 'New', self.customer.name)

    def get_product_summary(self):
        result = ''
        for product in self.products.all():
            result += u'%s <br/>' % product.get_summary()
        return result

    def get_summary(self):
        """ plain text summary for order """
        if self.customer:
            url = reverse('admin:%s_%s_change' % ('customer', 'customer'), args=[self.customer.id])
            result = '<br/><a href="%s">%s</a>' % (url, unicode(self.address))
        else:
            result = 'None'

        if self.address:
            if self.address.id_number:
                result += u'<br/><br/>  <span>%s %s</span>' % (self.address.name, self.address.id_number)
        result += '<br/><br/>'

        if self.products.count():
            result += self.get_product_summary()
            result += u'总计: %d<br/>' % self.sell_price_rmb
            result = '%s<br/><br/><br/>' % result
        return result

    def set_paid(self):
        self.is_paid = True
        self.paid_time = datetime.datetime.now()
        self.save(update_fields=['is_paid', 'paid_time'])
        self.update_monthly_report()

    def set_status(self, status_value):
        self.status = status_value
        if status_value == ORDER_STATUS.FINISHED:
            if self.is_paid:
                self.finish_time = datetime.datetime.now()
                self.save(update_fields=['status', 'finish_time'])
                customer = self.customer
                customer.last_order_time = self.create_time
                customer.order_count = customer.order_set.count()
                customer.save()
        else:
            self.save(update_fields=['status'])

        self.update_monthly_report()

    def update_monthly_report(self):
        if self.is_paid and not self.status == ORDER_STATUS.CREATED:
            from ..report.models import MonthlyReport

            if self.paid_time:
                year = self.paid_time.year
                month = self.paid_time.month
                MonthlyReport.stat(year, month)
            else:
                self.paid_time = datetime.datetime.now()
                self.save(update_fields=['paid_time'])
                MonthlyReport.stat_current_month()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.address and self.customer.primary_address:
            self.address = self.customer.primary_address

        return super(Order, self).save()

    def get_link(self):
        url = reverse('admin:%s_%s_change' % ('order', 'order'), args=[self.id])
        name = '[#%s]%s' % (self.id, self.customer.name)
        return u'<a href="%s">%s</a>' % (url, name)

    def get_public_link(self):
        return reverse('order:order-detail-short', args=[self.customer.id, self.id])

    def get_id_link(self):
        return u'<a target="_blank" href="%s">%s@%s</a>' % (self.get_public_link(), self.customer_id, self.pk)

    get_id_link.allow_tags = True
    get_id_link.short_description = 'ID'

    def update_price(self):
        self.total_amount = 0
        self.product_cost_aud = 0
        self.product_cost_rmb = 0
        self.origin_sell_rmb = 0
        self.shipping_fee = 0
        self.profit_rmb = 0

        products = self.products.all()
        for p in products:
            self.total_amount += p.amount
            self.product_cost_aud += p.amount * p.cost_price_aud
            self.origin_sell_rmb += p.sell_price_rmb * p.amount
        self.product_cost_rmb = self.product_cost_aud * rate.aud_rmb_rate

        express_orders = self.express_orders.all()
        for ex_order in express_orders:
            self.ship_time = ex_order.create_time
            if ex_order.fee:
                self.shipping_fee += ex_order.fee

        self.total_cost_aud = self.product_cost_aud + self.shipping_fee
        self.total_cost_rmb = self.total_cost_aud * rate.aud_rmb_rate

        if not self.sell_price_rmb or self.sell_price_rmb < self.total_cost_rmb:
            self.sell_price_rmb = self.origin_sell_rmb
        if self.sell_price_rmb and self.total_cost_rmb:
            self.profit_rmb = self.sell_price_rmb - self.total_cost_rmb

        self.save()
        self.update_monthly_report()

    def get_paid_button(self):
        if not self.is_paid:
            url = reverse('order:change-order-paid', kwargs={'order_id': self.id})
            return '<a href="%s"><b>UNPAID</b></a>' % url
        return 'PAID'

    get_paid_button.allow_tags = True
    get_paid_button.short_description = 'Paid'

    def get_status_button(self):
        current_status = self.get_shipping_orders()
        if self.status in [ORDER_STATUS.CREATED, ORDER_STATUS.DELIVERED]:
            current_status += '<b>%s</b>' % self.status
        else:
            current_status += self.status

        next_status = self.next_status

        if not next_status:
            return ORDER_STATUS.FINISHED

        url = self.get_next_status_url()
        btn = '%s => <a href="%s">%s</a>' % (current_status, url, next_status)
        return btn

    def get_next_status_url(self):
        url = reverse('order:change-order-status', kwargs={'order_id': self.id, 'status_value': self.next_status})
        return url

    @property
    def next_status(self):
        if self.status == ORDER_STATUS.CREATED:
            return ORDER_STATUS.SHIPPING
        elif self.status == ORDER_STATUS.SHIPPING:
            return ORDER_STATUS.DELIVERED
        elif self.status == ORDER_STATUS.DELIVERED:
            return ORDER_STATUS.FINISHED
        else:
            return None

    def get_shipping_orders(self):
        result = ''
        for ex in self.express_orders.all():
            result += ex.get_tracking_link() + '<br/>'
        return result

    get_status_button.allow_tags = True
    get_status_button.short_description = 'Shipping Status'

    def get_id_upload(self):
        express_orders = self.express_orders.all()

        for ex_order in express_orders:
            if not ex_order.id_upload:
                return '<a target="_blank" href="%s"><b>UPLOAD</b></a>' % ex_order.carrier.website
        if not express_orders.count():
            return 'No Shipping'
        return 'DONE'

    get_id_upload.short_description = 'ID Upload'
    get_id_upload.allow_tags = True

    def get_customer_link(self):
        return self.customer.get_link()

    get_customer_link.allow_tags = True
    get_customer_link.short_description = 'Customer'


@python_2_unicode_compatible
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, blank=False, null=False, verbose_name=_('Order'), related_name='products')
    product = models.ForeignKey(Product, blank=True, null=True, verbose_name=_('Product'))
    name = models.CharField(_('Name'), max_length=128, null=True, blank=True)
    amount = models.IntegerField(_('Amount'), default=0, blank=False, null=False, )
    sell_price_rmb = models.DecimalField(_('Sell Price RMB'), max_digits=8, decimal_places=2, blank=True, null=True)
    total_price_rmb = models.DecimalField(_('Total RMB'), max_digits=8, decimal_places=2, blank=True, null=True)
    cost_price_aud = models.DecimalField(_('Cost Price AUD'), max_digits=8, decimal_places=2, blank=True, null=True)
    total_price_aud = models.DecimalField(_('Total AUD'), max_digits=8, decimal_places=2, blank=True, null=True)
    store = models.ForeignKey(Store, blank=True, null=True, verbose_name=_('Store'))
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True, editable=True)

    def __str__(self):
        return '%s X %s' % (self.name, self.amount)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.cost_price_aud:
            self.cost_price_aud = self.product.normal_price
        self.total_price_aud = self.cost_price_aud * self.amount

        if not self.sell_price_rmb:
            self.sell_price_rmb = self.product.safe_sell_price
        self.total_price_rmb = self.sell_price_rmb * self.amount

        if self.product and not self.name:
            self.name = self.product.get_name_cn()

        return super(OrderProduct, self).save()

    def get_summary(self):
        if self.product:
            product_name = '%s %s' % (self.product.brand.name_en, self.product.name_cn)
        else:
            product_name = self.name
        return '%s = %d x %s' % (product_name, self.sell_price_rmb, self.amount)

    def get_link(self):
        if self.product:
            return reverse('product:product-detail', args=[self.product.pk])
        else:
            return None


@receiver(post_save, sender=Order)
def update_price_from_order(sender, instance=None, created=False, update_fields=None, **kwargs):
    if update_fields:
        if 'status' in update_fields or 'is_paid' in update_fields or 'paid_time' in update_fields:
            instance.update_monthly_report()
    elif instance.id:
        post_save.disconnect(update_price_from_order, sender=Order)
        instance.update_price()
        post_save.connect(update_price_from_order, sender=Order)


@receiver(post_save, sender=OrderProduct)
def update_price_from_orderproduct(sender, instance=None, created=False, update_fields=None, **kwargs):
    if instance.order and instance.order.id:
        instance.order.update_price()


@receiver(post_delete, sender=OrderProduct)
def order_product_deleted(sender, **kwargs):
    order_product = kwargs['instance']
    order_product.order.update_price()
