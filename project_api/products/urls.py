from rest_framework import routers

from . import views


products_router = routers.SimpleRouter()
products_router.register(r'categories', views.CategoryViewSet)
products_router.register(r'products', views.ProductViewSet)
