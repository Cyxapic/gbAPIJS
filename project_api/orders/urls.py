from django.urls import path
# from rest_framework import routers

from . import views


# orders_router = routers.SimpleRouter()
# orders_router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', views.OrderList.as_view()),
    path('create/', views.CreateOrder.as_view()),
]
