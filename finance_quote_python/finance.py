""" The main module """
from typing import List
import logging
from enum import Enum, auto

from pricedb import SecuritySymbol

from .alphavantage import AlphaVantageDownloader
from .morningstar import MorningstarDownloader
from .vanguard_au import VanguardAuDownloader
from .fixerio import Fixerio


class DownloadAgents(Enum):
    """ Available agents for price download """
    alphavantage = auto(),
    fixerio = auto(),
    morningstar = auto(),
    vanguard_au = auto()


class Quote:
    symbol = None

    """ The main application object """
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def fetch(self, exchange: str, symbols: List[str]):
        """ The main method to fetch prices.
        exchange = the name of the exchange, also the module used to fetch the prices, namespace;
        symbols = the list of symbols to fetch;
        """
        assert isinstance(exchange, str)
        #assert isinstance(symbols, List[str])
        #assert symbols

        if not symbols:
            raise ValueError("The symbols are missing.")
        
        # fetch the prices using the given module.
        result = []
        return result

    def currency(self):
        pass

    def __download_price(self, exchange: str, symbol: str):
        """ Download single price """
        # todo Instantiate the appropriate agent from exchange.
        exchange = exchange.lower()
        
        pass

    def __download(self, symbol: str, currency: str = None, agent: str = None):
        """ Download single latest price """
        assert agent is not None
        assert isinstance(agent, str)

        symbol = symbol.upper()
        currency = currency.upper()
        agent = agent.lower()
        actor = None
        price = None

        security_symbol = SecuritySymbol("", "")
        security_symbol.parse(symbol)

        if agent == DownloadAgents.morningstar.name:
            actor = MorningstarDownloader()
        elif agent == DownloadAgents.vanguard_au.name:
            actor = VanguardAuDownloader()
        elif agent == DownloadAgents.alphavantage.name:
            actor = AlphaVantageDownloader()
        elif agent == DownloadAgents.fixerio.name:
            actor = Fixerio()
        else:
            raise ValueError("No agent specified for price download.")

        if actor:
            actor.logger = self.logger
            try:
                price = actor.download(security_symbol, currency)
            except AttributeError as e:
                self.logger.error(str(e))

        return price
