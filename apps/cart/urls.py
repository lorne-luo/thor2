from django.conf.urls import url
from . import views

# urls for cart

urlpatterns = [
    url(r'^add_cart', views.AddCart.as_view(), name='add-cart'),
    # url(r'^cart/autocomplete/$', views.CartAutocomplete.as_view(), name='cart-autocomplete'),
]
