# coding=utf-8
import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy, reverse
from django.db import models
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from tinymce import HTMLField

from core.django.constants import ReadStatus, TaskStatus, MailStatus, UsableStatus, DICT_NULL_BLANK_TRUE


class AbstractMessageContent(models.Model, UsableStatus):
    title = models.CharField(
        verbose_name='标题', max_length=200
    )
    contents = HTMLField(
        verbose_name='内容',
        blank=True
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='状态',
        choices=UsableStatus.STATUS,
        default=UsableStatus.USABLE,
        db_index=True
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="数据创建人",
        # editable=False,
        **DICT_NULL_BLANK_TRUE
    )
    created_at = models.DateTimeField(
        verbose_name="数据创建时间",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="数据更新时间",
        auto_now=True
    )
    deleted_at = models.DateTimeField(
        verbose_name="数据删除时间",
        **DICT_NULL_BLANK_TRUE
    )

    class Meta:
        abstract = True


class SiteMailContent(AbstractMessageContent):
    receivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True,
        related_name='sitemail_receivers',
        verbose_name='收件人',
    )

    class Meta:
        verbose_name_plural = verbose_name = '站内邮件内容'

    def __str__(self):
        return self.title

    class Config:
        success_url = reverse_lazy(
            'adminlte:common_list_page',
            kwargs={
                'app_name': 'messageset',
                'model_name': 'sitemailreceive'
            }
        )
        list_form_fields = (
            'title', 'contents', 'receivers'
        )

    def send(self):
        kwargs = {
            'title': self.title,
            'content': self,
            'sender': self.creator,
            'creator': self.creator
        }

        # if no receivers filed, send to all
        if not self.receivers.count():
            if self.creator.is_superuser:
                self.receivers = get_user_model().objects.all()
            else:
                self.receivers = get_user_model().objects.filter(is_superuser=True)
            self.save()

        SiteMailSend(**kwargs).save()
        for user in self.receivers.all():
            tmp_kwargs = {'receiver': user}
            tmp_kwargs.update(kwargs)
            SiteMailReceive(**tmp_kwargs).save()


class AbstractSiteMail(models.Model, MailStatus):
    title = models.CharField(
        verbose_name='主题',
        max_length=200
    )
    content = models.ForeignKey(
        SiteMailContent,
        verbose_name='内容'
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        verbose_name='发件人',
        **DICT_NULL_BLANK_TRUE
    )
    send_time = models.DateTimeField(
        verbose_name='发送时间',
        auto_now_add=True,
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='读取状态',
        choices=MailStatus.STATUS,
        default=MailStatus.UNREAD,
        db_index=True
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="数据创建人",
        **DICT_NULL_BLANK_TRUE
    )
    created_at = models.DateTimeField(
        verbose_name="数据创建时间",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="数据更新时间",
        auto_now=True
    )
    deleted_at = models.DateTimeField(
        verbose_name="数据删除时间",
        **DICT_NULL_BLANK_TRUE
    )

    class Meta:
        abstract = True


class SiteMailSend(AbstractSiteMail):
    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name_plural = verbose_name = '发件箱'

    class Config:
        detail_template_name = 'messageset/sitemail_detail.html'
        list_display_fields = (
            'title', 'send_time', 'pk'
        )
        list_form_fields = (
            'title',
            'content.contents',
            'send_time',
        )
        filter_fields = ('status',)
        search_fields = ('title',)

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(sender=request.user).exclude(
                status=SiteMailSend.DELETED
            )


class SiteMailReceive(AbstractSiteMail):
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='sitemailreceive_receive',
        verbose_name='收件人',
        **DICT_NULL_BLANK_TRUE
    )
    read_time = models.DateTimeField(
        verbose_name='读取时间',
        **DICT_NULL_BLANK_TRUE
    )

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name_plural = verbose_name = '收件箱'

    class Config:
        list_template_name = 'messageset/sitemail_list.html'
        form_template_name = 'messageset/sitemail_form.html'
        detail_template_name = 'messageset/sitemail_detail.html'
        list_display_fields = (
            'title', 'sender', 'status', 'send_time', 'pk'
        )
        list_form_fields = (
            'title', 'sender'
        )
        filter_fields = ('status',)
        search_fields = ('title',)

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(receiver=request.user).exclude(
                status=SiteMailReceive.DELETED
            )

        @classmethod
        def get_object_hook(cls, request, obj):
            save_flag = False
            if obj.status != ReadStatus.READ:
                obj.status = ReadStatus.READ
                save_flag = True
            if not obj.read_time:
                obj.read_time = datetime.datetime.now()
                save_flag = True
            if save_flag:
                obj.save()


class NotificationContent(AbstractMessageContent):
    receivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True,
        related_name='notification_receivers',
        verbose_name='收件人',
        help_text='不选则发送给全体用户'
    )

    class Meta:
        verbose_name_plural = verbose_name = '系统通知内容'

    def __str__(self):
        return self.title

    class Config:
        success_url = reverse_lazy(
            'adminlte:common_list_page',
            kwargs={
                'app_name': 'messageset',
                'model_name': 'notification'
            }
        )
        list_form_fields = (
            'title', 'contents', 'receivers'
        )

    def send(self):
        # if no receivers filed, send to all
        if not self.receivers.count():
            self.receivers = get_user_model().objects.all()
            self.save()

        for user in self.receivers.all():
            if not Notification.objects.filter(receiver=user, content=self).exists():
                nf = Notification()
                nf.title = self.title
                nf.content = self
                nf.receiver = user
                nf.creator = self.creator
                nf.status = Notification.UNREAD
                nf.save()


class Notification(models.Model, ReadStatus):
    title = models.CharField(
        verbose_name='标题',
        max_length=200,
        default='',
        **DICT_NULL_BLANK_TRUE
    )
    content = models.ForeignKey(
        NotificationContent,
        verbose_name='内容',
        **DICT_NULL_BLANK_TRUE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        verbose_name='收件人',
        **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='读取状态',
        choices=ReadStatus.STATUS,
        default=ReadStatus.UNREAD,
        db_index=True
    )
    send_time = models.DateTimeField(
        verbose_name='发送时间',
        auto_now_add=True,
        **DICT_NULL_BLANK_TRUE
    )
    read_time = models.DateTimeField(
        verbose_name='读取时间',
        **DICT_NULL_BLANK_TRUE
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="数据创建人",
        **DICT_NULL_BLANK_TRUE
    )
    created_at = models.DateTimeField(
        verbose_name="数据创建时间",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="数据更新时间",
        auto_now=True
    )
    deleted_at = models.DateTimeField(
        verbose_name="数据删除时间",
        **DICT_NULL_BLANK_TRUE
    )

    def __str__(self):
        return '%s' % self.content.title

    class Meta:
        verbose_name_plural = verbose_name = '系统通知'

    class Config:
        list_template_name = 'messageset/notification_list.html'
        list_display_fields = (
            'title', 'status', 'send_time', 'pk'
        )
        list_form_fields = (
            'title', 'content.contents', 'send_time'
        )
        filter_fields = ('status',)
        search_fields = ('title',)

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.exclude(status=Notification.DELETED).filter(
                receiver=request.user
            )

        @classmethod
        def get_object_hook(cls, request, obj):
            obj.status = ReadStatus.READ
            if not obj.read_time:
                obj.read_time = datetime.datetime.now()
            obj.save()


class Task(models.Model, TaskStatus):
    name = models.CharField(
        verbose_name='任务名称', max_length=200
    )
    percent = models.PositiveIntegerField(
        verbose_name='进度', default=0
    )
    start_app = models.CharField(
        verbose_name='发起app', max_length=255, **DICT_NULL_BLANK_TRUE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='状态',
        choices=TaskStatus.TASK_STATUS,
        default=TaskStatus.NORMAL,
        db_index=True
    )
    start_time = models.DateTimeField(
        verbose_name='开始时间', auto_now_add=True, **DICT_NULL_BLANK_TRUE
    )
    end_time = models.DateTimeField(
        verbose_name='结束时间', **DICT_NULL_BLANK_TRUE
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="数据创建人",
        **DICT_NULL_BLANK_TRUE
    )
    created_at = models.DateTimeField(
        verbose_name="数据创建时间",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="数据更新时间",
        auto_now=True
    )
    deleted_at = models.DateTimeField(
        verbose_name="数据删除时间",
        **DICT_NULL_BLANK_TRUE
    )

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse(
            'adminlte:common_detail_page',
            kwargs={
                'app_name': self._meta.app_label,
                'model_name': self._meta.model_name,
                'pk': self.pk
            }
        )

    class Meta:
        verbose_name_plural = verbose_name = '后台任务'

    class Config:
        # 列表页模板
        list_template_name = 'messageset/task_list.html'
        # 列表页展现的字段
        list_display_fields = (
            'name', 'percent', 'start_app', 'status',
            'start_time', 'end_time', 'pk'
        )
        # 表单页需要填写的字段
        list_form_fields = (
            'name', 'percent', 'start_app', 'status'
        )
        # 数据过滤
        filter_fields = ('status',)
        # 模糊搜索
        search_fields = ('name', 'start_app')

        @classmethod
        def filter_queryset(cls, request, queryset):
            return queryset.filter(creator=request.user).exclude(
                status=TaskStatus.DELETED
            )

# @receiver(post_save, sender=SiteMailContent)
# def create_sitemail_datas(sender, instance, created, **kwargs):
#     """
#     发送邮件时，向收件箱和发件箱添加数据，
#     这里将来可以替换为异步消息队列
#     :param sender:
#     :param instance:
#     :param kwargs:
#     """
#     if created:
#         kwargs = {
#             'title': instance.title,
#             'content': instance,
#             'sender': instance.creator,
#             'creator': instance.creator
#         }
#
#         # if no receivers filed, send to all
#         if not instance.receivers.count():
#             instance.receivers = get_user_model().objects.all()
#             instance.save()
#
#         SiteMailSend(**kwargs).save()
#         for user in instance.receivers.all():
#             tmp_kwargs = {
#                 'receiver': user,
#             }
#             tmp_kwargs.update(kwargs)
#             SiteMailReceive(**tmp_kwargs).save()

# @receiver(m2m_changed, sender=NotificationContent.receivers.through)
# def create_notification_datas(sender, instance, **kwargs):
#     """
#     保存系统通知时，给所选用户发送通知，
#     目前是向Notification表添加数据
#     这里将来可以替换为异步消息队列
#     :param sender:
#     :param instance:
#     :param kwargs:
#     """
#     instance.send()
