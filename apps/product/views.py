from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from braces.views import MultiplePermissionsRequiredMixin, PermissionRequiredMixin
from apps.adminlte.views import CommonContextMixin

from models import Product
from forms import ProductForm


class ProductList(MultiplePermissionsRequiredMixin, TemplateView):
    ''' List of products. '''
    template_name = 'product/product-list.html'
    permissions = {
        "any": ("product.add_product", "product.view_product")
    }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return self.render_to_response(context)


class ProductAddEdit(MultiplePermissionsRequiredMixin, TemplateView):
    ''' Add/Edit a product. '''
    template_name = 'product/product-edit.html'
    permissions = {
        "any": ("product.add_product", "product.view_product")
    }

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', '')
        context = {'form': ProductForm(), }
        if pk:
            product = get_object_or_404(Product, id=pk)
            context['product'] = product

        return self.render_to_response(context)


class ProductListView(MultiplePermissionsRequiredMixin, CommonContextMixin, ListView):
    model = Product
    template_name_suffix = '_list'
    template_name = 'product_list.html'
    permissions = {
        "all": ("product.view_product",)
    }

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', 'Normal Price', 'Bargain Price', 'Sell Price', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'normal_price', 'bargain_price', 'safe_sell_price', 'id']
        return context


class ProductUpdateView(MultiplePermissionsRequiredMixin, CommonContextMixin, UpdateView):
    model = Product
    # template_name_suffix = '_form'
    template_name = 'adminlte/common_form.html'
    permissions = {
        "all": ("product.change_product",)
    }
    fields = ['name_en', 'name_cn', 'pic', 'brand', 'spec1', 'category', 'normal_price', 'bargain_price',
              'safe_sell_price']

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['table_titles'] = ['Pic', 'Name', 'Brand', 'Normal Price', 'Bargain Price', 'Sell Price', '']
        context['table_fields'] = ['pic', 'link', 'brand', 'normal_price', 'bargain_price', 'safe_sell_price', 'id']
        return context