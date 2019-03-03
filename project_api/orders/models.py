from django.db import models
from django.conf import settings

from products.models import Product


class Order(models.Model):
    CR, PAID, END, CANCEL = range(4)
    STATUS = (
        (CR, 'В обработке'),
        (PAID, 'Оплачен'),
        (END, 'Исполнен'),
        (CANCEL, 'Отменен'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='обновлен'
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=CR,
        verbose_name='Статус заказа'
    )

    class Meta:
        ordering = ('created', )
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='продукт',
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='количество'
    )

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def __str__(self):
        return self.order.__str__()
