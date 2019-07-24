'''
Price downloader for Boerse Frankfurt (FWB)

The site is using Server-Side Events to send price updates.
See https://pypi.org/project/sseclient/

The new boerse-frankfurt.de
https://www.boerse-frankfurt.de/etp/IE00B810Q511
https://api.boerse-frankfurt.de/data/price_information?isin=IE00B810Q511&mic=XETR
https://api.boerse-frankfurt.de/data/quote_box?isin=IE00BKX55Q28&mic=XFRA
'''
import logging
from pricedb import SecuritySymbol, PriceModel


class FwbDownloader:
    ''' FWB '''
    def __init__(self):
        self.namespace = "FWB"
        self.currency = "EUR"
        self.logger = logging.getLogger(__name__)

    def download(self, symbol: SecuritySymbol, currency: str) -> PriceModel:
        ''' download the price '''
        import urllib.parse
        import urllib.request
        from sseclient import SSEClient

        if not symbol.namespace:
            raise ValueError(f"Namespace not sent for {symbol}")

        self.logger.debug(f"fetching price from FWB.")

        url = self.get_security_url(symbol)

        # download
        messages = SSEClient(url)

        if not messages:
            return None

        data = None
        for msg in messages:
            if msg.data:
                data = msg.data
                if "EMPTY" not in data:
                    break

        # parse
        price = self.parse_price(data)

        price.symbol = symbol

        return price

    def get_security_url(self, security: SecuritySymbol) -> str:
        ''' Mapping the security to the price URL '''
        if security.namespace != self.namespace:
            raise ValueError("Wrong exchange requested!")

        sec_codes = {
            "VGOV": "IE00B42WWV65",
            "VMID": "IE00BKX55Q28",
            "VUKE": "IE00B810Q511"
        }
        isin = sec_codes[security.mnemonic]

        #url = f"https://www.boerse-frankfurt.de/etp/{isin}"
        url = f"https://api.boerse-frankfurt.de/data/quote_box?isin={isin}&mic=XFRA"

        return url

    def parse_price(self, json_str: str) -> PriceModel:
        ''' Get the price from HTML '''
        import json
        from decimal import Decimal
        from datetime import datetime
        from pydatum import Datum

        content = json.loads(json_str)

        result = PriceModel()
        price_str = str(content['lastPrice'])
        result.value = Decimal(price_str)
        result.currency = self.currency

        date_str = content['timestampLastPrice']
        date_val = datetime.fromisoformat(date_str)
        result.datum = Datum()
        result.datum.from_datetime(date_val)

        return result
