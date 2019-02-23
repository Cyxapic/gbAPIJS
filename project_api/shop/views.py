from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import AboutShop, PaymentMethod
from .serializers import AboutShopSerializer, PaymentMethodSerializer


class ShopDescriptionViewSet(ReadOnlyModelViewSet):
    queryset = AboutShop.objects.filter(show=True)
    serializer_class = AboutShopSerializer


class PaymentMethodsViewSet(ReadOnlyModelViewSet):
    queryset = PaymentMethod.objects.filter(is_active=True)
    serializer_class = PaymentMethodSerializer
