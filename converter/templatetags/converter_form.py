from django import template

from converter.models import Currency

register = template.Library()


@register.inclusion_tag("converter/converter_form.html")
def get_converter_form(currency_from=None, currency_to=None, amount=None):
    return {
        "currencies": Currency.objects.order_by('code'),
        "from": currency_from,
        "to": currency_to,
        "amount": amount
        }