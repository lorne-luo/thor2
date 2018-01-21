# coding=utf-8
from braces.views import MultiplePermissionsRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView

from core.django.views import CommonContextMixin, FormAccessRequestViewMixin
from models import ExpressCarrier
from . import forms


class CarrierInfoRequiredMixin(object):
    def prompt_incomplete_carrier(self, **kwargs):
        from apps.member.models import Seller
        if isinstance(self.request.profile, Seller):
            incomplete_carrier = ExpressCarrier.get_incomplete_carrier_by_user(self.request.profile)
            if incomplete_carrier:
                msg = u'物流公司信息不完整，<a href="%s">更新完整信息</a>程序员哥哥才能提供更好帮助.' % reverse(
                    'express:expresscarrier-update', args=[incomplete_carrier.id])
                messages.warning(self.request, msg)


# views for ExpressCarrier

class ExpressCarrierListView(CarrierInfoRequiredMixin, MultiplePermissionsRequiredMixin, CommonContextMixin, ListView):
    model = ExpressCarrier
    template_name_suffix = '_list'  # express/expresscarrier_list.html
    permissions = {
        "all": ("express.view_expresscarrier",)
    }

    def get_context_data(self, **kwargs):
        self.prompt_incomplete_carrier()
        return super(ExpressCarrierListView, self).get_context_data(**kwargs)


class ExpressCarrierAddView(FormAccessRequestViewMixin, MultiplePermissionsRequiredMixin, CommonContextMixin, CreateView):
    model = ExpressCarrier
    form_class = forms.ExpressCarrierAddForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("express.add_expresscarrier",)
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.seller = self.request.profile
        return super(ExpressCarrierAddView, self).form_valid(form)


class ExpressCarrierUpdateView(FormAccessRequestViewMixin, MultiplePermissionsRequiredMixin, CommonContextMixin,
                               UpdateView):
    model = ExpressCarrier
    form_class = forms.ExpressCarrierUpdateForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("express.change_expresscarrier",)
    }


class ExpressCarrierDetailView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    model = ExpressCarrier
    form_class = forms.ExpressCarrierDetailForm
    template_name = 'adminlte/common_detail_new.html'
    permissions = {
        "all": ("express.view_expresscarrier",)
    }
