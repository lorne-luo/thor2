from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from django.views.generic import TemplateView

from core.django.views import CommonPageViewMixin


class OwnerViewSetMixin(object):
    def get_queryset(self):
        qs = super(OwnerViewSetMixin, self).get_queryset()
        if self.request.user.is_staff or self.request.user.is_superuser :
            return qs
        elif self.request.user.is_customer:
            return qs.filter(customer=self.request.profile)
        else:
            return qs.none()


class ChangePasswordView(CommonPageViewMixin, PasswordChangeView):
    template_name = 'adminlte/change-password.html'
    title = '修改密码'


class ChangePasswordDoneView(CommonPageViewMixin, TemplateView):
    template_name = 'adminlte/change-password-done.html'
