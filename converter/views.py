from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Currency
from django.urls import reverse
from decimal import Decimal, InvalidOperation

# Create your views here.

def show(request):
    return render(request, 'converter/index.html')


def convert(request, from_code, to_code, method):
    if request.method == 'GET':
        amount = request.GET['amount']
    else:
        amount = request.POST['amount']

    # Treat negative numbers as positive
    amount = amount.lstrip('-')

    # Convert number to python-readable way
    amount = amount.replace(',', '.')

    try:
        from_ = Currency.objects.get(code=from_code.upper())
        to = Currency.objects.get(code=to_code.upper())
        rate = Currency.objects.get_rate_from_to(from_code, to_code)
        THREEPLACES = Decimal(10) ** -3
        result = (Decimal(amount) * rate).quantize(THREEPLACES)

    except InvalidOperation:
        success = False
        error_message = "Amount should be a number"
    except Currency.DoesNotExist:
        success = False
        error_message = "Invalid currency code"
    else:
        success = True

    if method == 'html':
        if success:
            context_dict = {
                'from_': from_, 'to': to,
                # str(Decimal(...)) to remove leading zeroes
                'amount': str(Decimal(amount)),
                'result': result,
                'success': True}
        else:
            context_dict = {
                'error': True,
                'error_message': error_message
                }

        return render(request, 'converter/convert.html', context_dict)

    elif method == 'json':
        response_data = {'success': success}
        if success:
            response_data['result'] = result
        else:
            response_data['error'] = error_message
        return JsonResponse(response_data)

    elif method == 'text':
        if success:
            return HttpResponse(result)
        else:
            return HttpResponse(error_message)


def convert_redirector(request):
    if request.method == 'POST':
        from_code = request.POST['from']
        to_code = request.POST['to']
        amount = request.POST['amount']

        return redirect(reverse('convert', kwargs={
            'from_code':from_code,
            'to_code':to_code,
            'method':'html'
            }) + '?amount='+amount)

