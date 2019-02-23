from django.db import models


class AboutShop(models.Model):
    title = models.CharField(max_length=50, default='')
    description = models.TextField()
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PaymentMethod(models.Model):
    method = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.method
