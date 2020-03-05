# -*- coding: utf-8 -*-
import logging

from celery.task import task

from apps.order.models import Order, ORDER_STATUS

log = logging.getLogger(__name__)


# @periodic_task(run_every=crontab(minute=7, hour='9,12,15,18,21,0'))
@task
def update_delivery_tracking():
    for order in Order.objects.filter(status__in=[ORDER_STATUS.SHIPPING, ORDER_STATUS.CREATED]):
        order.update_track()


# @periodic_task(run_every=crontab(minute=5, hour='11,14,17,19,23'))
@task
def send_delivery_sms():
    for order in Order.objects.filter(status=ORDER_STATUS.DELIVERED):
        if not order.delivery_msg_sent:
            order.sms_delivered()
        order.set_status(ORDER_STATUS.FINISHED)

    for order in Order.objects.filter(status=ORDER_STATUS.SHIPPING):
        order.sms_delivered()
        if order.is_all_delivered:
            order.set_status(ORDER_STATUS.FINISHED)
            order.express_orders.update(delivery_sms_sent=True)
