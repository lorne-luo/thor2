from django.conf.urls import url
from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:order-list'), reverse('api:order-detail', kwargs={'pk': 1})
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'orderproduct', views.OrderProductViewSet, basename='orderproduct')

urlpatterns = [

]

urlpatterns += router.urls
