from rest_framework import routers

from . import views


orders_router = routers.SimpleRouter()
orders_router.register(r'orders', views.OrderViewSet)
