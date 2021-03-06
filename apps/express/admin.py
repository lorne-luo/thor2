from django.contrib import admin
from .models import ExpressOrder, ExpressCarrier


class ExpressOrderAdmin(admin.ModelAdmin):
    list_display = ('carrier', 'get_tracking_link', 'get_order_link', 'address', 'fee', 'weight', 'create_time')
    ordering = ['-create_time']
    list_display_links = ['address', 'carrier']
    search_fields = ('order__customer__name', 'address__name', 'address__address', 'track_id')
    list_filter = ['carrier__name_cn']


admin.site.register(ExpressOrder, ExpressOrderAdmin)

admin.site.register(ExpressCarrier)
