from django.db import models
from .openexchangerates import currencies_names, get_rates
from decimal import Decimal
from django.core.cache import cache

# Create your models here.

class CurrencyManager(models.Manager):
    def get_rate_from_to(self, from_code, to_code):
        from_inst = Currency.objects.get(code=from_code)
        to_inst = Currency.objects.get(code=to_code)
        result = to_inst.usd_rate / from_inst.usd_rate
        return result

    def update_rates_from_api(self):
        def add_currency(full_name, code, usd_rate):
            try:
                c = Currency.objects.get(code=code)
            except Currency.DoesNotExist:
                c = Currency(code=code)

            c.full_name = full_name
            c.usd_rate = usd_rate
            c.save()

        currencies = currencies_names()
        usd_rates = get_rates()
        for code, full_name in currencies.items():
            add_currency(full_name=full_name, code=code, usd_rate=usd_rates[code])



class Currency(models.Model):

    objects = CurrencyManager()
    class Meta:
        verbose_name_plural = 'Currencies'

    full_name = models.CharField(max_length=200)
    code = models.CharField(max_length=3, unique=True)
    usd_rate = models.DecimalField(
        decimal_places=10, max_digits=20, blank=True, verbose_name="USD rate")

    def __unicode__(self):
        return self.code


