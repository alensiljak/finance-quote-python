""" The main module """
from typing import List

class Quote:
    symbol = None

    """ The main application object """
    def __init__(self):
        pass

    def fetch(self, exchange, symbols):
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