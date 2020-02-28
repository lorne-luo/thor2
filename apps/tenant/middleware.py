import threading

from tenant_schemas.middleware import DefaultTenantMiddleware
from tenant_schemas.utils import get_public_schema_name

THREADING_LOCAL = threading.local()


class ProfileTenantMiddleware(DefaultTenantMiddleware):
    """
    Selects the proper database schema using the request host. E.g. <my_tenant>.<my_domain>
    """
    DEFAULT_SCHEMA_NAME = get_public_schema_name()

    def get_tenant(self, model, hostname, request):
        tenant = None
        if request.user.is_authenticated():
            domain = request.META.get('HTTP_HOST')
            tenant = model.objects.filter(domain_url=domain).first()

            if not tenant and request.user.tenant_id:
                tenant = model.objects.filter(pk=request.user.tenant_id).first()

            if not tenant:
                tenant = model.objects.get(schema_name=self.DEFAULT_SCHEMA_NAME)

        return tenant

    def process_request(self, request):
        super(ProfileTenantMiddleware, self).process_request(request)

        if request.user.is_authenticated():
            profile = getattr(request.user, 'profile', None)
            setattr(request, 'profile', profile)

            if profile:
                if request.user.is_seller:
                    setattr(request, 'seller', profile)
                if request.user.is_customer:
                    setattr(request, 'customer', profile)
        else:
            setattr(request, 'profile', None)
