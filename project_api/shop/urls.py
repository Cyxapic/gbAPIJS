from rest_framework import routers

from . import views


shop_router = routers.SimpleRouter()
shop_router.register(r'description', views.ShopDescriptionViewSet)
shop_router.register(r'payment-methods', views.PaymentMethodsViewSet)
