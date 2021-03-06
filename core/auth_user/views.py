# coding=utf-8
from django.contrib.auth.views import password_change
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from core.django.views import CommonPageViewMixin


class OwnerViewSetMixin(object):
    def get_queryset(self):
        qs = super(OwnerViewSetMixin, self).get_queryset()
        if self.request.user.is_seller:
            return qs.filter(seller=self.request.profile)
        elif self.request.user.is_customer:
            return qs.filter(customer=self.request.profile)
        else:
            return qs.none()

class ChangePasswordView(CommonPageViewMixin, TemplateView):
    def post(self, request, **kwargs):
        self.request = request
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        return self.render_to_response(context)

    def render_to_response(self, context, **response_kwargs):
        context['page_title'] = '修改密码'
        template_response = password_change(
            self.request,
            template_name='adminlte/change-password.html',
            extra_context=context
        )
        return template_response


class ChangePasswordDoneView(CommonPageViewMixin, TemplateView):
    template_name = 'adminlte/change-password-done.html'
