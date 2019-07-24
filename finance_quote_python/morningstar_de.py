"""
Morningstar.de price downloader
"""
import logging
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pydatum import Datum

from pricedb.model import PriceModel, SecuritySymbol


class MorningstarDeDownloader:
    """ Fetches prices from Morningstar site """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def download(self, symbol: SecuritySymbol, currency: str) -> PriceModel:
        """ Download the given symbol """
        import urllib.parse
        import urllib.request

        if not symbol.namespace:
            raise ValueError(f"Namespace not sent for {symbol}")

        codes = {
            "FWB:VUKE": "0P0001BVG4"
        }
        code = codes[str(symbol)]

        url = f"http://www.morningstar.de/de/etf/snapshot/snapshot.aspx?id={code}"
        self.logger.debug(f"fetching price from {url}")

        with urllib.request.urlopen(url) as response:
            html = response.read()

        if not html:
            return None

        # parse HTML
        price = self.parse_price(html)
        if price:
            price.symbol = symbol
        # compare currency
        if price.currency != currency:
            raise ValueError(f"Requested currency ({currency}) does not match the {symbol} -> {currency}.")

        return price

    def parse_price(self, html: str) -> PriceModel:
        """ parse html to get the price """
        from bs4 import BeautifulSoup

        result = PriceModel()
        soup = BeautifulSoup(html, 'html.parser')

        overview = soup.find(id='overviewQuickstatsDiv')

        # Price
        price_el = overview.find('table').find_all('tr')[1].find_all('td')[2]
        if not price_el:
            logging.debug(f"Received from mstar: {html}")
            raise ValueError("No price info found in returned HTML.")

        value = price_el.get_text().strip()
        
        # Currency
        currency = value[:3]
        result.currency = currency

        value = value[3:].strip()
        # decimal separator
        value = value.replace(',', '.')
        # parse
        try:
            result.value = Decimal(value)
        except InvalidOperation:
            message = f"Could not parse price value {value}"
            print(message)
            self.logger.error(message)
            return None

        # Date
        date_el = overview.find('table').find_all('tr')[1].find_all('td')[0].find('span')
        #date_str = soup.find(id="asOfDate").get_text().strip()
        date_str = date_el.get_text().strip()
        date_val = datetime.strptime(date_str, "%d.%m.%Y")
        result.datum = Datum()
        result.datum.from_datetime(date_val)

        return result
