from django.core.management.base import BaseCommand

from exchange.currency_parser import CurrencyParser
from exchange.models import CurrencyCode, ExchangeCourse


class Command(BaseCommand):
    help = "Scrape data from source"

    def handle(self, *args, **options):
        parser = CurrencyParser()
        data = parser.run()
        currencies = dict(CurrencyCode.objects.values_list('alphabetic_code', 'pk'))
        records_to_save = []
        from_currency = CurrencyCode.objects.filter(alphabetic_code='EUR').first()
        for row in data:
            records_to_save.append(ExchangeCourse(
                from_currency=from_currency,
                to_currency_id=currencies.get(row.get('code')),
                course=row.get('value')
            ))
        ExchangeCourse.objects.bulk_create(records_to_save)
