from django.core.management.base import BaseCommand
import pandas as pd
from exchange.models import CurrencyCode


class Command(BaseCommand):
    help = "Fill Currency Code form file"

    def handle(self, *args, **options):
        data = pd.read_excel("list_one.xls", sheet_name="Active", header=3)
        data = data.drop_duplicates(subset='Alphabetic Code', keep="last")
        data = data.fillna(0)
        data = data.to_dict('records')
        codes_to_save = []
        for row in data:
            codes_to_save.append(CurrencyCode(
                alphabetic_code=row.get('Alphabetic Code'),
                numeric_code=row.get('Numeric Code', 0),
                currency=row.get('Currency'),
                entity=row.get('ENTITY')
            ))
        CurrencyCode.objects.bulk_create(codes_to_save)
        print("Successfully added currency codes")
