from django.conf.urls import patterns, url
import views
import serializers

urlpatterns = patterns('apps.member.views',
    url(r'^login/', 'member_login', name='member-login'),
    url(r'^logout/', 'member_logout', name='member-logout'),
    url(r'^home/$', 'member_home', name="member-home"),
    url(r'^agent/$', views.AgentView.as_view(), name="member-agent"),
    url(r'^profile/$', views.Profile.as_view(), name="member-profile"),
    url(r'^users/$', 'seller_index', name="seller-index"),
    url(r'^user/add/$', views.CreateUser.as_view(), name="seller-add"),
    url(r'^user/edit/(?P<pk>[\d]+)/$', views.Profile.as_view(), name="admin-user-edit"),
    url(r'^user/delete/(?P<pk>[-\d]+)/$', 'user_delete', name="user-delete"),
    url(r'^user/password/(?P<pk>[-\d]+)/$', 'user_password_reset', name="user-password"),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^password_change/$', 'password_change', {'template_name': 'member/password_change_form.html'}),
    url(r'^password_change/done/$', 'password_change_done', {'template_name': 'member/password_change_done.html'}),
    url(r'^password/reset/$', 'password_reset', {'template_name': 'registration/password_reset_form.html', 'email_template_name':'email/password_reset_email_txt.html'}),
    url(r'^password/reset/done/$', 'password_reset_done', {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', 'password_reset_confirm', {'template_name': 'registration/password_reset_confirm.html'}),
    url(r'^password/reset/complete/$', 'password_reset_complete', {'template_name': 'registration/password_reset_complete.html'}, name='password_reset_complete'),
)