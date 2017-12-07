
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter
from core.api.routers import PostHackedRouter
import views

router = PostHackedRouter()
router.include_root_view = False

urlpatterns = [
    url(r'^order/(?P<order_id>\d+)/status/(?P<status_value>\w+)/$', views.change_order_status, name='change-order-status'),
    url(r'^order/paid/(?P<order_id>\d+)/$', views.change_order_paid, name="change-order-paid"),

    url(r'^order/index/$', views.OrderIndex.as_view(), name="order-index"),
	# url(r'^add/$', views.OrderAddEdit.as_view(), name="order-add"),
	# url(r'^order/edit/(?P<pk>\d+)/$', views.OrderAddEdit.as_view(), name="order-edit"),
    url(r'^order/(?P<customer_id>\d+)/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='order-detail'),
    url(r'^(?P<customer_id>\d+)/(?P<pk>\d+)/$', views.OrderDetailView.as_view(), name='order-detail-short'),
    url(r'^order/(?P<pk>\d+)/edit/$', login_required(views.OrderUpdateView.as_view()), name='order-update'),
    url(r'^order/add/$', views.OrderAddView.as_view(), name='order-add'),
    url(r'^order/add/(?P<customer_id>\d+)/$', views.OrderAddDetailView.as_view(), name='order-add-detail'),
    url(r'^order/list/$', login_required(views.OrderListView.as_view()), name='order-list'),
    url(r'^order/$', login_required(views.OrderListView.as_view()), name='order-list-short'),
    url(r'^order/(?P<username>\w+)/$', views.OrderMemberListView.as_view(), name='order-member'),

    # payment
    url(r'^order/(?P<pk>\d+)/pay/$', login_required(views.OrderPayView.as_view()), name='order-pay'),
]


# reverse('order:api-order-list'), reverse('order:api-order-detail', kwargs={'pk': 1})
router.register(r'api/order/order', views.OrderViewSet, base_name='api-order')

# urls for orderproduct
urlpatterns += [
    # url(r'^order/orderproduct/add/$', login_required(views.OrderProductAddView.as_view()), name='orderproduct-add'),
    url(r'^order/orderproduct/list/$', login_required(views.OrderProductListView.as_view()), name='orderproduct-list'),
    url(r'^order/orderproduct/(?P<pk>\d+)/$', login_required(views.OrderProductDetailView.as_view()), name='orderproduct-detail'),
    # url(r'^order/orderproduct/(?P<pk>\d+)/edit/$', login_required(views.OrderProductUpdateView.as_view()), name='orderproduct-update'),
]

router.register(r'api/order/orderproduct', views.OrderProductViewSet, base_name='api-orderproduct')


urlpatterns += router.urls