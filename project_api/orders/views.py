from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Order
from .serializers import OrderSerializer
from .permissions import IsOrderOwner


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.none()
    serializer_class = OrderSerializer
    permission_classes = (IsOrderOwner, )

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
