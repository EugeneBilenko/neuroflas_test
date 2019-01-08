from django.db import models

# Create your models here.


class CurrencyCode(models.Model):
    alphabetic_code = models.CharField(max_length=3)
    numeric_code = models.IntegerField()
    currency = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)

    def __str__(self):
        return self.alphabetic_code


class ExchangeCourse(models.Model):
    from_currency = models.ForeignKey(CurrencyCode, on_delete=models.CASCADE, related_name="exchange_from")
    to_currency = models.ForeignKey(CurrencyCode, on_delete=models.CASCADE, related_name="exchange_to")
    course = models.FloatField()

    def __str__(self):
        return "%s - %s" % (self.from_currency, self.to_currency,)
