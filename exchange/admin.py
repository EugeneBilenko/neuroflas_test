from django.contrib import admin
from exchange.models import ExchangeCourse, CurrencyCode

# Register your models here.


admin.site.register(ExchangeCourse)
admin.site.register(CurrencyCode)