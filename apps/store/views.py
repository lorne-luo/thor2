# coding=utf-8
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse
from braces.views import MultiplePermissionsRequiredMixin, PermissionRequiredMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from core.adminlte.views import CommonContextMixin, CommonViewSet
from models import Page, Store
import serializers
import forms


# views for Page

class PageListView(MultiplePermissionsRequiredMixin, CommonContextMixin, ListView):
    model = Page
    template_name_suffix = '_list'  # store/page_list.html
    permissions = {
        "all": ("store.view_page",)
    }


class PageAddView(MultiplePermissionsRequiredMixin, CommonContextMixin, CreateView):
    model = Page
    form_class = forms.PageAddForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("page.add_page",)
    }


class PageUpdateView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    model = Page
    form_class = forms.PageUpdateForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("page.change_page",)
    }


class PageDetailView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    model = Page
    form_class = forms.PageDetailForm
    template_name = 'adminlte/common_detail_new.html'
    permissions = {
        "all": ("page.view_page",)
    }


# api views for Page

class PageViewSet(CommonViewSet):
    queryset = Page.objects.all()
    serializer_class = serializers.PageSerializer
    filter_fields = ['id']
    search_fields = ['title', 'url', 'store', 'price', 'original_price']


# views for Store

class StoreListView(MultiplePermissionsRequiredMixin, CommonContextMixin, ListView):
    model = Store
    template_name_suffix = '_list'  # store/store_list.html
    permissions = {
        "all": ("store.view_store",)
    }


class StoreAddView(MultiplePermissionsRequiredMixin, CommonContextMixin, CreateView):
    model = Store
    form_class = forms.StoreAddForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("store.add_store",)
    }


class StoreUpdateView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    model = Store
    form_class = forms.StoreUpdateForm
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("store.change_store",)
    }


class StoreDetailView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    model = Store
    form_class = forms.StoreDetailForm
    template_name = 'adminlte/common_detail_new.html'
    permissions = {
        "all": ("store.view_store",)
    }


# api views for Store

class StoreViewSet(CommonViewSet):
    queryset = Store.objects.all()
    serializer_class = serializers.StoreSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    filter_fields = ['id']
    search_fields = ['name', 'short_name', 'address', 'domain', 'search_url', 'shipping_rate']
