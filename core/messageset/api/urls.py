from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:notification-list'),reverse('api:notification-detail', kwargs={'pk': 1})
router.register(r'notification', views.NotificationViewSet, basename='notification')
# router.register(r'notificationcontent', views.NotificationContentViewSet, basename='notificationcontent')
router.register(r'sitemailcontent', views.SiteMailContentViewSet, basename='sitemailcontent')
router.register(r'sitemailreceive', views.SiteMailReceiveViewSet, basename='sitemailreceive')
router.register(r'sitemailsend', views.SiteMailSendViewSet, basename='sitemailsend')
router.register(r'task', views.TaskViewSet, basename='task')

urlpatterns = [
    url(r'sitemail/receive/markall', views.sitemail_markall, name='sitemail_markall'),
    url(r'notification/markall', views.notification_markall, name='notification_markall'),
]

urlpatterns += router.urls
