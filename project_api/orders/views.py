from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from products.models import Product

from .models import Order
from .serializers import OrderSerializer, OrderCreateSerializer
from .permissions import IsOrderOwner


class OrderList(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, IsOrderOwner, )

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class CreateOrder(APIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        order = Order.objects.create(user=request.user)
        data_order = request.data
        errors = []
        for data in data_order:
            product = Product.objects.filter(pk=data['id'])
            product = product.values_list('pk').last()
            data_ = {
                'order': order.pk,
                'product': product[0],
                'quantity': data.get('quantity', 1)
            }
            serializer = OrderCreateSerializer(data=data_)
            if serializer.is_valid():
                serializer.save()
            else:
                errors.append(serializer.errors)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data, status=status.HTTP_201_CREATED)
