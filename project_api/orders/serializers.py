from rest_framework import serializers

from .models import Order, OrderItem


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    created = serializers.DateTimeField(
        format='%Y-%m-%d',
        required=False,
        read_only=True
    )

    class Meta:
        model = Order
        fields = ('pk', 'created', 'status')


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    # def create(self, validated_data):
    #     print(validated_data)
    #     # order = Order.object.create(user=self.request.user)
        # OrderItem.object.create_many()
