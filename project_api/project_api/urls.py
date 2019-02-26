from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework import routers

from shop.urls import shop_router
from products.urls import products_router


router = routers.SimpleRouter()
router.registry.extend(shop_router.registry)
router.registry.extend(products_router.registry)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
