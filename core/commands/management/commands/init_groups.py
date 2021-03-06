'''
 Create initial groups + their default permissions
 Run 'manage.py validate_permissions' prior to this one if you just added new permissions.
'''
from django.conf import settings
from django.contrib.auth.models import Permission, Group
from django.core import management
from django.core.management.base import BaseCommand
from tenant_schemas.utils import get_public_schema_name

from apps.tenant.models import Tenant
from core.auth_user.constant import ADMIN_GROUP, MEMBER_GROUP, CUSTOMER_GROUP, PREMIUM_MEMBER_GROUP, FREE_PREMIUM_GROUP


class Command(BaseCommand):
    help = '''Create initial groups + their default permissions '''

    permissions = {
        # Group name
        ADMIN_GROUP: [
            # view add chg del    app        model
            ('y', 'y', 'y', 'y', 'customer', 'address'),
        ],
        MEMBER_GROUP: [
            ('y', 'y', 'y', 'n', 'member', 'seller'),
            ('y', 'y', 'y', 'y', 'order', 'order'),
            ('y', 'y', 'y', 'y', 'order', 'orderproduct'),
            ('y', 'y', 'y', 'y', 'customer', 'customer'),
            ('y', 'y', 'y', 'y', 'customer', 'address'),
            ('y', 'y', 'y', 'y', 'product', 'product'),
            ('y', 'n', 'n', 'n', 'report', 'monthlyreport'),
            ('n', 'n', 'n', 'n', 'store', 'store'),
            ('y', 'y', 'y', 'y', 'express', 'expresscarrier'),
            ('y', 'y', 'y', 'y', 'express', 'expressorder'),
        ],
        CUSTOMER_GROUP: [
            ('y', 'y', 'y', 'n', 'customer', 'customer'),
            ('y', 'y', 'y', 'y', 'customer', 'address'),
        ],

    }

    permissions.update({PREMIUM_MEMBER_GROUP: permissions[MEMBER_GROUP]})
    permissions.update({FREE_PREMIUM_GROUP: permissions[MEMBER_GROUP]})

    def create_public_tenant(self):
        public_schema = get_public_schema_name()
        if not Tenant.objects.filter(schema_name=public_schema).exists():
            tenant = Tenant(domain_url=settings.DOMAIN_NAME, schema_name=public_schema)
            tenant.save()

    def create_super_tenant(self):
        super_schema = settings.SUPER_SCHEMA_NAME
        if super_schema and not Tenant.objects.filter(schema_name=super_schema).exists():
            tenant = Tenant(domain_url='%s/%s' % (settings.DOMAIN_NAME, super_schema), schema_name=super_schema)
            tenant.save()

    def handle(self, *args, **options):
        self.create_public_tenant()
        self.create_super_tenant()

        management.call_command('validate_permissions')
        not_found = []

        for group_name, permission_set in list(self.permissions.items()):
            group, _created = Group.objects.get_or_create(name=group_name)

            permissions = []
            for view, add, change, delete, app_label, model_name in permission_set:
                perm_list = self.get_perm_list(view, add, change, delete, app_label, model_name)
                for perm_code in perm_list:
                    try:
                        p = Permission.objects.get(
                            codename=perm_code, content_type__app_label=app_label,
                            content_type__model=model_name)
                        permissions.append(p)
                    except Permission.DoesNotExist:
                        not_found.append(perm_code)

            print(("\nGroup '%s', adding permissions: \n%s\n" % (
                group_name, '\t' + '\n\t'.join([p.codename for p in permissions]))))

            group.permissions.clear()
            group.permissions.add(*permissions)

        if not_found:
            print(("Warning: Unable to find these permissions: %s" % ', '.join(not_found)))

    def get_perm_list(self, view, add, change, delete, app_label, model_name):
        perm_list = []
        if view.lower() == 'y':
            perm_list.append('view_%s' % model_name)
        if add.lower() == 'y':
            perm_list.append('add_%s' % model_name)
        if change.lower() == 'y':
            perm_list.append('change_%s' % model_name)
        if delete.lower() == 'y':
            perm_list.append('delete_%s' % model_name)
        return perm_list
