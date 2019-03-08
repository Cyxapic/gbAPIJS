from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated', 'status')
    list_filter = ('user', 'created', 'status')


admin.site.register(OrderItem)
