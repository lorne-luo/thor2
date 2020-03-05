from braces.views import StaffuserRequiredMixin, SuperuserRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView

from core.django.views import CommonContextMixin
from . import forms
from .models import MonthlyReport


class MonthlyReportListView(StaffuserRequiredMixin, CommonContextMixin, ListView):
    """ List views for MonthlyReport """
    model = MonthlyReport
    template_name_suffix = '_list'  # report/monthlyreport_list.html

    def get_context_data(self, **kwargs):
        context = super(MonthlyReportListView, self).get_context_data(**kwargs)
        data = MonthlyReport.stat_user_total()
        context.update(data)
        return context


class MonthlyReportAddView(SuperuserRequiredMixin, CommonContextMixin, CreateView):
    """ Add views for MonthlyReport """
    model = MonthlyReport
    form_class = forms.MonthlyReportAddForm
    template_name = 'adminlte/common_form.html'


class MonthlyReportUpdateView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Update views for MonthlyReport """
    model = MonthlyReport
    form_class = forms.MonthlyReportUpdateForm
    template_name = 'adminlte/common_form.html'


class MonthlyReportDetailView(SuperuserRequiredMixin, CommonContextMixin, UpdateView):
    """ Detail views for MonthlyReport """
    model = MonthlyReport
    form_class = forms.MonthlyReportDetailForm
    template_name = 'adminlte/common_detail_new.html'
