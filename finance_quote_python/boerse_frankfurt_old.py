'''
Price downloader for Boerse Frankfurt (FWB)

*** Incomplete, not needed ***

VGOV
http://proxy.boerse-frankfurt.de/cst/BoerseFrankfurt/Share/chart.json?instruments=1600000012,18575515,13,814&period=OneYear
http://proxy.boerse-frankfurt.de/cst/BoerseFrankfurt/Share/chart.json?instruments=1000000012,18575515,13,814&period=Intraday
VMID
http://proxy.boerse-frankfurt.de/cst/BoerseFrankfurt/Share/chart.json?instruments=1000000012,25116447,13,814&period=Intraday
'''
import logging
from pricedb import SecuritySymbol, PriceModel


class FwbDownloader:
    ''' FWB '''
    def __init__(self):
        #self.url = "http://quotes.morningstar.com/stockq/c-header"
        self.namespace = "FWB"
        self.logger = logging.getLogger(__name__)

    def download(self, symbol: SecuritySymbol, currency: str) -> PriceModel:
        ''' download the price '''
        #import urllib.parse
        import urllib.request

        if not symbol.namespace:
            raise ValueError(f"Namespace not sent for {symbol}")

        self.logger.debug(f"fetching price from FWB.")

        url = self.get_security_url(symbol)

        # download
        with urllib.request.urlopen(url) as response:
            html = response.read()

        if not html:
            return None

        # parse
        price = self.parse_price(html)

        return price

    def get_security_url(self, security: SecuritySymbol) -> str:
        ''' Mapping the security to the price URL '''
        if security.namespace != self.namespace:
            raise ValueError("Wrong exchange requested!")

        sec_codes = {
            "VGOV": "18575515",
            "VMID": "25116447"
        }
        sec_code = sec_codes[security.mnemonic]

        instrument = "1000000012" # ETF
        period = "Intraday"

        url = f"http://proxy.boerse-frankfurt.de/cst/BoerseFrankfurt/Share/chart.json?instruments={instrument},{sec_code},13,814&period={period}"

        return url

    def parse_price(self, html: str) -> PriceModel:
        ''' Get the price from HTML '''
        from bs4 import BeautifulSoup

        result = PriceModel()
        #soup = BeautifulSoup(html, 'html.parser')

        #price_el = soup.find(id='last-price-value')

        return result
