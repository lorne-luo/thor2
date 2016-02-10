# coding=utf-8
from rest_framework import serializers
from django.core.urlresolvers import reverse
from models import Notification, NotificationContent, SiteMailContent, SiteMailReceive, SiteMailSend, Task



class SiteMailReceiveSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username')
    status = serializers.SerializerMethodField()
    status_value = serializers.IntegerField(source='status')

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = SiteMailReceive
        fields = SiteMailReceive.Config.list_display_fields + (
            'status_value',
        )
        read_only_fields = (
            'id', 'send_time', 'status_value'
        )


class SiteMailSendSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = SiteMailSend
        fields = ['title', 'sender', 'status', 'send_time', 'id']
        read_only_fields = (
            'id', 'send_time', 'sender', 'status'
        )


class NotificationSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source='content.contents')
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Notification
        fields = (
            'id', 'title', 'content', 'status', 'send_time', 'read_time',
            'creator', 'created_at'
        )
        read_only_fields = (
            'id', 'created_at'
        )


class TaskSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_percent(self, obj):
        return '%s%%' % obj.percent

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Task
        fields = (
            'id', 'name', 'percent', 'start_app', 'status',
            'start_time', 'end_time',
            'creator', 'created_at'
        )
        read_only_fields = (
            'id', 'created_at', 'status'
        )


# Serializer for notificationcontent
class NotificationContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = NotificationContent
        fields = ['title', 'contents', 'status', 'creator', 'created_at', 'updated_at', 'deleted_at'] + ['id']
        read_only_fields = ['id']

    def get_link(self, obj):
        request = self.context.get('request', None)

        change_perm_str = '%s.change_%s' % (self.Meta.model._meta.app_label, self.Meta.model._meta.model_name)
        view_perm_str = '%s.view_%s' % (self.Meta.model._meta.app_label, self.Meta.model._meta.model_name)
        if request.user.has_perm(change_perm_str):
            url = reverse('messageset:notificationcontent-update', args=[obj.id])
            return '<a href="%s">%s</a>' % (url, 'Update Link')
        elif request.user.has_perm(view_perm_str):
            url = reverse('messageset:notificationcontent-detail', args=[obj.id])
            return '<a href="%s">%s</a>' % (url, 'Detail Link')
        return None


# Serializer for sitemailcontent
class SiteMailContentSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    sender = serializers.CharField(source='creator.username')
    send_time = serializers.DateTimeField(source='created_at')

    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model = SiteMailContent
        fields = ['link'] + ['title', 'contents', 'status', 'sender', 'send_time', 'updated_at', 'deleted_at'] + ['id']
        read_only_fields = ['id']

    def get_link(self, obj):
        request = self.context.get('request', None)

        change_perm_str = '%s.change_%s' % (self.Meta.model._meta.app_label, self.Meta.model._meta.model_name)
        view_perm_str = '%s.view_%s' % (self.Meta.model._meta.app_label, self.Meta.model._meta.model_name)
        if request.user.has_perm(change_perm_str):
            url = reverse('messageset:sitemailcontent-update', args=[obj.id])
            return '<a href="%s">%s</a>' % (url, 'Update Link')
        elif request.user.has_perm(view_perm_str):
            url = reverse('messageset:sitemailcontent-detail', args=[obj.id])
            return '<a href="%s">%s</a>' % (url, 'Detail Link')
        return None
