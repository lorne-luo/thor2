from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from apps.member.forms import CustomPasswordResetForm, CustomSetPasswordForm
from apps.member.views import member_login, member_logout
from apps.order.views import OrderDetailView
from core import auth_user
from core.api.views import GitCommitInfoView
from core.auth_user.views import ChangePasswordView


def if_installed(appname, *args, **kwargs):
    ret = url(*args, **kwargs)
    if appname not in settings.INSTALLED_APPS:
        ret.resolve = lambda *args: None
    return ret


apps_urlpatterns = [
    url(r'^$', member_login, name='member-login'),
    url(r'^logout/$', member_logout, name='member-logout'),
    # url(r'^djadmin/', include(admin.site.urls)),
    url(r'^customer/', include(('apps.customer.urls','customer'), namespace='customer')),
    url(r'^member/', include(('apps.member.urls','member'), namespace='member')),
    url(r'^product/', include(('apps.product.urls','product'), namespace='product')),
    url(r'^order/', include(('apps.order.urls','order'), namespace='order')),
    url(r'^express/', include(('apps.express.urls','express'), namespace='express')),
    url(r'^carrier_tracker/', include(('apps.carrier_tracker.urls','carrier_tracker'), namespace='carrier_tracker')),
    url(r'^report/', include(('apps.report.urls','report'), namespace='report')),
    url(r'^wx/', include(('apps.weixin.urls','weixin'), namespace='weixin')),
    url(r'^schedule/', include(('apps.schedule.urls','schedule'), namespace='schedule')),
    url(r'^messageset/', include(('core.messageset.urls','messageset'), namespace='messageset')),
    # url(r'^payments/', include('core.payments.stripe.urls', namespace='payments')),
    # url(r'^(?P<schema_id>[-\w]+)/(?P<uid>[-\w]+)/$', OrderDetailView.as_view(), name='order-detail-short'),
]

# REST API
api_urlpatterns = [
    url(r'^customer/', include('apps.customer.api.urls')),
    url(r'^carrier_tracker/', include('apps.carrier_tracker.api.urls')),
    url(r'^express/', include('apps.express.api.urls')),
    url(r'^member/', include('apps.member.api.urls')),
    url(r'^order/', include('apps.order.api.urls')),
    url(r'^product/', include('apps.product.api.urls')),
    url(r'^report/', include('apps.report.api.urls')),
    url(r'^schedule/', include('apps.schedule.api.urls')),
    url(r'^messageset/', include('core.messageset.api.urls')),
    url(r'^sms/', include('core.sms.urls')),
    url(r'^version/$', GitCommitInfoView.as_view(), name='api_version'),
]

urlpatterns = apps_urlpatterns + [
    # REST API
    url(r'^api/', include((api_urlpatterns,'api'), namespace='api')),

    # auth
    url('^auth/change-password/$', ChangePasswordView.as_view(), name='change_password'),
    url('^auth/change-password-done/$', auth_user.views.ChangePasswordDoneView.as_view(), name='password_change_done'),

    # password reset
    # url(r'^password/reset/$', auth_views.password_reset, {'template_name': 'adminlte/password_reset_form.html',
    #                                                       'email_template_name': 'adminlte/password_reset_email.html',
    #                                                       'password_reset_form': CustomPasswordResetForm},
    #     name='password_reset'),
    # url(r'^password/reset/done/$', auth_views.password_reset_done,
    #     {'template_name': 'adminlte/password_reset_done.html'},
    #     name='password_reset_done'),
    # url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
    #     {'template_name': 'adminlte/password_reset_confirm.html',
    #      'set_password_form': CustomSetPasswordForm},
    #     name='password_reset_confirm'),
    # url(r'^password/reset/complete/$', auth_views.password_reset_complete,
    #     {'template_name': 'adminlte/password_reset_complete.html'},
    #     name='password_reset_complete'),

    # dbsettings
    url(r'^djadmin/settings/', include('dbsettings.urls')),

    # django-tinymce
    url(r'^tinymce/', include('tinymce.urls')),

]

if settings.DEBUG:
    from rest_framework_swagger.views import get_swagger_view
    from django.conf.urls.static import static

    urlpatterns += [
        url(r'^api/docs/$', get_swagger_view(title='OZSales API'))
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
