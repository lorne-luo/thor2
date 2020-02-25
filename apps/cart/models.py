# coding=utf-8
import logging
import re
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from apps.carrier_tracker.models import CarrierTracker
from core.aliyun.sms.service import send_cn_sms
from core.django.models import PinYinFieldModelMixin, TenantModelMixin

log = logging.getLogger(__name__)

