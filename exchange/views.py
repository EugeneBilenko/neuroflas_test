import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from exchange.models import CurrencyCode, ExchangeCourse


def calculate_exchange(request):
    from_currency = CurrencyCode.objects.filter(alphabetic_code=request.GET.get("from"))
    to_currency = CurrencyCode.objects.filter(alphabetic_code=request.GET.get("to"))
    amount = float(request.GET.get("amount"))

    response = {
        "status": 200,
        "computed_amount": 0.0
    }

    if not from_currency.exists():
        response = {
            "status": 400,
            "msg": "Wrong 'From currency' code"
        }
        return HttpResponse(json.dumps(response), content_type="application/json", status=400)
    if not to_currency.exists():
        response = {
            "status": 400,
            "msg": "Wrong 'To currency' code"
        }
        return HttpResponse(json.dumps(response), content_type="application/json", status=400)

    exchange_course = ExchangeCourse.objects.filter(from_currency=from_currency.first(), to_currency=to_currency.first())
    if not exchange_course.exists():
        response = {
            "status": 400,
            "msg": "We have no course information about this currencies"
        }
        return HttpResponse(json.dumps(response), content_type="application/json", status=400)
    else:
        response["computed_amount"] = amount * exchange_course.last().course

    return HttpResponse(json.dumps(response), content_type="application/json")

