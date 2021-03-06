from rest_framework import serializers

from .models import AboutShop, PaymentMethod


class AboutShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutShop
        fields = ('title', 'description', )


class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ('id', 'method', )
