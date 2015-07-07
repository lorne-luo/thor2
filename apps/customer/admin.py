from django.contrib import admin
from models import Customer, Address, InterestTag
from form import CustomerAddForm
# Register your models here.

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    can_delete = True
    # max_num = 1
    verbose_name_plural = 'Address'


class InterestTagInline(admin.TabularInline):
    model = InterestTag
    extra = 1
    can_delete = True
    # max_num = 1
    verbose_name_plural = 'Tag'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile')
    search_fields = ('name', 'mobile')

    def add_view(self, request, form_url='', extra_context=None):
        self.exclude = ['password', 'groups', 'user_permissions', 'last_login', 'primary_address']
        self.inlines = [AddressInline, ]
        self.form = CustomerAddForm

        return super(CustomerAdmin, self).add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.exclude = ['password', 'groups', 'user_permissions', 'last_login']
        self.inlines = [AddressInline, ]
        self.form = CustomerAddForm
        return super(CustomerAdmin, self).change_view(request, object_id, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.save()


admin.site.register(Customer, CustomerAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'address', 'customer', 'id_photo_link')


admin.site.register(Address, AddressAdmin)

admin.site.register(InterestTag)
