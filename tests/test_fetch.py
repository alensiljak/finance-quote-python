""" Various tests for fetching the prices """
import pytest
from typing import List

from finance_quote_python import Quote


def test_no_symbols():
    """ handle empty symbol list """
    q = Quote()
    symbols = []
    actual = None

    with pytest.raises(Exception) as ex:
        actual = q.fetch("yo", symbols)

    assert ex is not None
    assert ex.typename == 'ValueError'
    assert ex.value.args[0] == "The symbols are missing."
   

def test_result_hash():
    """ The result is a Price Model object.
    Also tests connectivity and parsing.
    """
    from pricedb import PriceModel

    q = Quote()
    q.set_source("vanguard_au")
    actual = q.fetch("vanguard", ["BOND"])

    assert actual
    assert isinstance(actual[0], PriceModel)


def test_parsing():
    """ Test that the expected schema is retrieved """
    from decimal import Decimal

    q = Quote()
    q.set_source("vanguard_au")
    actual = q.fetch("vanguard", ["BOND"])

    assert actual
    # test that the source schema has not changed.
    price = actual[0]
    assert price.currency
    assert price.datum
    assert price.symbol
    assert price.symbol.namespace == "vanguard".upper()
    assert price.value
    assert isinstance(price.value, Decimal)
