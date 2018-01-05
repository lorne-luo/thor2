# coding=utf-8
from braces.views import MultiplePermissionsRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView

from core.django.views import CommonContextMixin
from .models import DealSubscribe
from . import forms


class DealSubscribeListView(MultiplePermissionsRequiredMixin, CommonContextMixin, ListView):
    """ List views for DealSubscribe """
    model = DealSubscribe
    template_name_suffix = '_list'  # schedule/dealsubscribe_list.html
    permissions = {
        "all": ("schedule.view_dealsubscribe",)
    }


class DealSubscribeAddView(MultiplePermissionsRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for DealSubscribe """
    model = DealSubscribe
    form_class = forms.DealSubscribeAddForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("schedule.add_dealsubscribe",)
    }


class DealSubscribeUpdateView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for DealSubscribe """
    model = DealSubscribe
    form_class = forms.DealSubscribeUpdateForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("schedule.change_dealsubscribe",)
    }


class DealSubscribeDetailView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for DealSubscribe """
    model = DealSubscribe
    form_class = forms.DealSubscribeDetailForm
    template_name = 'adminlte/common_detail_new.html'
    permissions = {
        "all": ("schedule.view_dealsubscribe",)
    }
