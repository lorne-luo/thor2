from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^product/product/add/$', login_required(views.ProductAddView.as_view()), name="product-add"),
    url(r'^product/$', views.ProductListView.as_view(), name="product-list"),
    url(r'^product/product/(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name="product-detail"),
    url(r'^product/product/(?P<pk>\d+)/edit/$', login_required(views.ProductUpdateView.as_view()), name="product-update"),
]

# urls for brand
urlpatterns += [
    url(r'^product/brand/add/$', login_required(views.BrandAddView.as_view()), name='brand-add'),
    url(r'^product/brand/list/$', login_required(views.BrandListView.as_view()), name='brand-list'),
    url(r'^product/brand/(?P<pk>\d+)/$', views.BrandDetailView.as_view(), name='brand-detail'),
    url(r'^product/brand/(?P<pk>\d+)/edit/$', login_required(views.BrandUpdateView.as_view()), name='brand-update'),
]
