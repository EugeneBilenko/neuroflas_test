import urllib3
from bs4 import BeautifulSoup


class CurrencyParser:
    def __init__(self, debug=False):
        self.url = "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html"
        self.debug_file = "test_scrapped_data.txt.txt"
        self.debug = debug
        self.source_page = None

    def run(self) -> list:
        self.source_page = self.get_source_info()
        return self.prepare_codes()

    def get_source_info(self) -> bytes:
        if self.debug:
            with open(self.debug_file, "rb") as f:
                data = f.read()
        else:
            http = urllib3.PoolManager()
            page = http.request('GET', self.url)
            if int(page.status) != 200:
                print("error occured")
            data = page.data
        return data

    def prepare_codes(self) -> list:
        soup = BeautifulSoup(self.source_page, 'html.parser')
        rows = soup.find('table', attrs={'class': 'ecb-forexTable fullWidth'}).find("tbody").find_all("tr")
        currency_data = []
        for row in rows:
            tmp = {}
            tmp['code'] = row.find("td", attrs={'class': 'currency'}).text
            tmp['value'] = float(row.find("span", attrs={'class': 'rate'}).text)
            currency_data.append(tmp)

        return currency_data


