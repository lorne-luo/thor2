# coding=utf-8
from django.contrib import messages
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from core.django.views import CommonContextMixin
from . import forms
from .models import ExpressCarrier


class CarrierInfoRequiredMixin(object):
    def prompt_incomplete_carrier(self, **kwargs):
        incomplete_carrier = ExpressCarrier.get_incomplete_carrier()
        if incomplete_carrier:
            msg = '物流公司信息不完整，<a href="%s">更新完整信息</a>程序员哥哥才能提供更好帮助.' % reverse(
                'express:expresscarrier-update', args=[incomplete_carrier.pk])
            messages.warning(self.request, msg)


# views for ExpressCarrier

class ExpressCarrierListView(CarrierInfoRequiredMixin, CommonContextMixin, ListView):
    model = ExpressCarrier
    template_name_suffix = '_list'  # express/expresscarrier_list.html

    def get_context_data(self, **kwargs):
        self.prompt_incomplete_carrier()
        return super(ExpressCarrierListView, self).get_context_data(**kwargs)


class ExpressCarrierAddView(CommonContextMixin, CreateView):
    model = ExpressCarrier
    template_name = 'adminlte/common_form.html'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return forms.ExpressCarrierAdminForm
        else:
            return forms.ExpressCarrierAddForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(ExpressCarrierAddView, self).form_valid(form)


class ExpressCarrierUpdateView(CommonContextMixin,
                               UpdateView):
    model = ExpressCarrier
    template_name = 'adminlte/common_form.html'

    def get_form_class(self):
        if self.request.user.is_superuser:
            return forms.ExpressCarrierAdminForm
        else:
            return forms.ExpressCarrierUpdateForm


class ExpressCarrierDetailView(CommonContextMixin, UpdateView):
    model = ExpressCarrier
    form_class = forms.ExpressCarrierDetailForm
    template_name = 'adminlte/common_detail_new.html'
