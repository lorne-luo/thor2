from django.conf.urls import url
from django.urls import include

from core.api.routers import PostHackedRouter
from . import views

router = PostHackedRouter()
router.include_root_view = False

# reverse('api:customer-list'), reverse('api:customer-detail', kwargs={'pk': 1})
router.register(r'customer', views.CustomerViewSet, basename='customer')
router.register(r'address', views.AddressViewSet, basename='address')

urlpatterns = [
    url(r'^customer/autocomplete/$', views.CustomerAutocomplete.as_view(), name='customer-autocomplete'),
    url(r'^address/autocomplete/$', views.AddressAutocomplete.as_view(), name='address-autocomplete'),
    url(r'^', include(router.urls)),
]

# urlpatterns = router.urls + urlpatterns
