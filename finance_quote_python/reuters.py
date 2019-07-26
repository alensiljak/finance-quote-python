'''
https://www.reuters.com/finance/stocks/overview/VUKE.F
'''
import logging
from pricedb import SecuritySymbol, PriceModel


class Reuters:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def download(self, symbol: SecuritySymbol, currency: str) -> PriceModel:
        import urllib.request

        url = self.get_security_url(symbol)
        # download
        with urllib.request.urlopen(url) as response:
            html = response.read()
        if not html:
            return None

        price = self.parse_price(html)
        price.symbol = symbol

        return price

    def get_security_url(self, security: SecuritySymbol) -> str:
        base = "https://www.reuters.com/finance/stocks/overview/"

        exchange_dict = {
            'FWB': 'F'
        }

        namespace = exchange_dict[security.namespace]

        return f"{base}{security.mnemonic}.{namespace}"
    
    def parse_price(self, html: str) -> PriceModel:
        from decimal import Decimal, InvalidOperation
        from bs4 import BeautifulSoup

        result = PriceModel()
        soup = BeautifulSoup(html, 'html.parser')

        price_el = (soup.find(id='headerQuoteContainer')
            .find('div', class_='sectionQuoteDetail')
            .find_all('span'))

        # price value
        price_text = price_el[1]
        value = price_text.get_text().strip()
        try:
            result.value = Decimal(value)
        except InvalidOperation:
            message = f"Could not parse price value {value}"
            print(message)
            self.logger.error(message)
            return None

        # currency
        cur_text = price_el[2].get_text().strip()
        result.currency = cur_text

        # date / time
        date_str = price_el[3].get_text().strip()
        result.datum = self.parse_date(date_str)
        
        return result

    def parse_date(self, date_str: str):
        ''' parse date/time '''
        from dateutil.parser import parse
        from dateutil import tz
        from pydatum import Datum

        # Can be "19 Jul 2019" or "6:06am EDT".

        if "EDT" in date_str:
            # the format is "6:06am EDT"
            from_zone = tz.gettz('US/Eastern')
            #est = tz.gettz('EST')
            to_zone = tz.tzlocal()
            parsed_date = parse(date_str)
            date_val = parsed_date.replace(tzinfo=from_zone).astimezone(tz=to_zone)
        else:
            # the date format is "19 Jul 2019"
            #date_val = datetime.strptime(date_str, "%d %b %Y")
            date_val = parse(date_str)

        datum = Datum()
        result = datum.from_datetime(date_val)
        return result