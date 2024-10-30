from django.db import models
from django.utils import timezone


class CurrencyRate(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)


class RateRequestLog(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
