from django.shortcuts import render
from django.http import HttpResponse
from .openexchangerates import get_rates, currencies_names
from .models import Currency

# Create your views here.

def show(request):
    return render(request, 'index.html')


def update(request):

    for curr in get_rates().keys():
        Currency(full_name=currencies_names()[curr], code= curr, usd_rate=get_rates()[curr]).save()
    return HttpResponse('База данных обновлена!')