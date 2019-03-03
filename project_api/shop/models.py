from django.db import models


class AboutShop(models.Model):
    title = models.CharField(
        max_length=50,
        default='',
        verbose_name='Заголоков статьи'
    )
    description = models.TextField(
        verbose_name='Статья'
    )
    show = models.BooleanField(
        default=True,
        verbose_name='Показать'
    )

    class Meta:
        verbose_name = 'О магазине'
        verbose_name_plural = 'О магазине'

    def __str__(self):
        return self.title


class PaymentMethod(models.Model):
    method = models.CharField(
        max_length=50,
        verbose_name='Описание метода'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный'
    )

    class Meta:
        verbose_name = 'Методы оплаты'
        verbose_name_plural = 'Методы оплаты'

    def __str__(self):
        return self.method
