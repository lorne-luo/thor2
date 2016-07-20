# coding=utf-8
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from braces.views import MultiplePermissionsRequiredMixin, PermissionRequiredMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from core.adminlte.views import CommonContextMixin, CommonViewSet
from models import MonthlyReport
import serializers
import forms


class MonthlyReportListView(MultiplePermissionsRequiredMixin, CommonContextMixin, ListView):
    """ List views for MonthlyReport """
    model = MonthlyReport
    template_name_suffix = '_list'  # report/monthlyreport_list.html
    permissions = {
        "all": ("report.view_monthlyreport",)
    }


class MonthlyReportAddView(MultiplePermissionsRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for MonthlyReport """
    model = MonthlyReport
    form_class = forms.MonthlyReportAddForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("monthlyreport.add_monthlyreport",)
    }

    def get_success_url(self):
        return reverse('report:monthlyreport-list')


class MonthlyReportUpdateView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for MonthlyReport """
    model = MonthlyReport
    form_class = forms.MonthlyReportUpdateForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("monthlyreport.change_monthlyreport",)
    }

    def get_success_url(self):
        return reverse('report:monthlyreport-list')


class MonthlyReportDetailView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for MonthlyReport """
    model = MonthlyReport
    form_class = forms.MonthlyReportDetailForm
    template_name = 'adminlte/common_detail_new.html'
    permissions = {
        "all": ("monthlyreport.view_monthlyreport",)
    }


class MonthlyReportViewSet(CommonViewSet):
    """ API views for MonthlyReport """
    queryset = MonthlyReport.objects.all()
    serializer_class = serializers.MonthlyReportSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    filter_fields = ['month', 'order_count', 'parcel_count', 'cost_aud', 'cost_rmb', 'shipping_fee', 'sell_price_rmb', 'profit_rmb']
    search_fields = ['month', 'order_count', 'parcel_count', 'cost_aud', 'cost_rmb', 'shipping_fee', 'sell_price_rmb', 'profit_rmb']

