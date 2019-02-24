from __future__ import absolute_import, unicode_literals
from celery import shared_task
from converter.models import Currency

@shared_task
def update_rates_from_api():
    Currency.objects.update_rates_from_api()

@shared_task
def add(x,y):
    return x+y