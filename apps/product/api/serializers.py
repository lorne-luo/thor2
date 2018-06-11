from rest_framework import serializers
from core.api.serializers import BaseSerializer, SellerOwnerSerializerMixin
from ..models import Product, Brand


class ProductSerializer(SellerOwnerSerializerMixin, BaseSerializer):
    """Serializer for product"""
    brand_display = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'edit_url', 'detail_url', 'is_owner', 'name_en', 'name_cn', 'pic', 'brand_cn', 'brand_en',
                  'brand_display', 'spec', 'max_cost', 'last_sell_price', 'avg_sell_price', 'min_sell_price',
                  'max_sell_price', 'avg_cost', 'min_cost', 'thumbnail']
        read_only_fields = ['id']

    def get_thumbnail(self, obj):
        return obj.pic.thumbnail.url if obj.pic else None

    def get_brand_display(self, obj):
        return unicode(obj.brand)


class BrandSerializer(BaseSerializer):
    """ Serializer for Brand """

    class Meta:
        model = Brand
        fields = ['id', 'edit_url', 'detail_url'] + \
                 ['name_en', 'name_cn', 'short_name', 'remarks']
        read_only_fields = ['id']
