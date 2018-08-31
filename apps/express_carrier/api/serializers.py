# coding=utf-8
from rest_framework import serializers
from core.api.serializers import BaseSerializer, SellerOwnerSerializerMixin
from ..models import ExpressCarrier


# Serializer for expresscarrier
class ExpressCarrierSerializer(SellerOwnerSerializerMixin, BaseSerializer):
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = ExpressCarrier
        fields = ['id', 'edit_url', 'detail_url', 'is_owner', 'name_cn', 'name_en', 'website', 'search_url',
                  'id_upload_url', 'track_id_regex', 'is_default']
        read_only_fields = ['id']
