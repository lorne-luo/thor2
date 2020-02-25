# -*- coding: utf-8 -*-
import logging
import time

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db import models, connection
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from apps.tenant.models import Tenant
from core.auth_user.constant import MEMBER_GROUP, PREMIUM_MEMBER_GROUP, FREE_PREMIUM_GROUP
from core.auth_user.models import AuthUser, UserProfileMixin
from core.django.constants import COUNTRIES_CHOICES, CURRENCY_CHOICES
from core.django.models import TenantModelMixin

log = logging.getLogger(__name__)

MONTHLY_FREE_ORDER = 10
SELLER_MEMBER_PLAN_ID = 'Seller_Member_1'


class Seller(UserProfileMixin, models.Model):
    auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name='seller', null=True, blank=True)
    name = models.CharField(_('姓名'), max_length=30, blank=True)
    country = models.CharField(_('国家'), max_length=128, choices=COUNTRIES_CHOICES, default='AU', blank=True)
    expire_at = models.DateField(_('member expire at'), auto_now_add=False, editable=True, null=True, blank=True)
    start_at = models.DateField(_('member start at'), auto_now_add=False, editable=True, null=True, blank=True)
    primary_currency = models.CharField(_('首选货币'), max_length=128, choices=CURRENCY_CHOICES, default='AUDCNH',
                                        blank=True)
    create_at = models.DateTimeField(_('create at'), auto_now_add=True, null=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return '%s' % self.name

    @cached_property
    def email(self):
        return self.auth_user.email

    @cached_property
    def mobile(self):
        return self.auth_user.mobile

    def set_email(self, email):
        self.auth_user.email = email
        self.auth_user.save(update_fields=['email'])

    def set_mobile(self, mobile):
        self.auth_user.mobile = mobile
        self.auth_user.save(update_fields=['mobile'])

    def send_email(self, subject, message):
        self.auth_user.email_user(subject, message)

    def send_au_sms(self, content, app_name=None):
        self.auth_user.send_au_sms(content, app_name)

    def send_notification(self, title, content, sender=None):
        self.auth_user.send_notification(title, content, sender)

    def send_sitemail(self, title, content, sender=None):
        self.auth_user.send_sitemail(title, content, sender)

    def get_name(self):
        return self.name or self.auth_user.get_username()


    def enable(self, month):
        self.auth_user.is_active = True
        self.start_at = timezone.now().date()
        self.expire_at = self.start_at + relativedelta(months=month)
        self.auth_user.save(update_fields=['is_active'])
        self.save(update_fields=['start_at', 'expire_at'])

    def disable(self):
        self.auth_user.is_active = False
        self.auth_user.save(update_fields=['is_active'])

    @cached_property
    def tenant(self):
        return Tenant.objects.filter(pk=self.tenant_id).first()

    @staticmethod
    def create_seller(mobile, email, password, premium_account=False):
        user = AuthUser.objects.create_user(mobile=mobile, email=email, password=password)

        member_group = Group.objects.get(name=MEMBER_GROUP)
        user.groups.add(member_group)
        if premium_account:
            premium_member_group = Group.objects.get(name=PREMIUM_MEMBER_GROUP)
            user.groups.add(premium_member_group)
        user.save()

        seller = Seller(auth_user=user,
                        name=mobile or email)
        seller.set_schema()
        seller.save()
        return seller

    def set_schema(self):
        schema_name = self.schema_name or self.tenant.schema_name
        if schema_name:
            connection.set_schema(schema_name)


class MembershipOrder(models.Model):
    seller = models.ForeignKey(Seller, blank=True, null=True)
    start_at = models.DateField(_('membership start at'), auto_now_add=False, editable=True, null=True, blank=True)
    end_at = models.DateField(_('membership expire at'), auto_now_add=False, editable=True, null=True, blank=True)
    amount = models.DecimalField(_('membership payment'), max_digits=5, decimal_places=2, null=True)
    create_at = models.DateTimeField(_('create at'), auto_now_add=True, null=True)
