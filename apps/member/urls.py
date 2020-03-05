from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^login/', views.member_login, name='member-login'),
    url(r'^logout/', views.member_logout, name='member-logout'),
    url(r'^register/', views.RegisterView.as_view(), name='member-register'),
)
