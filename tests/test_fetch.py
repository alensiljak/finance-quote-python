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
    """ The result is a Price Model object
    """
    from pricedb import PriceModel

    q = Quote()
    q.set_source("vanguard_au")
    actual = q.fetch("vanguard", ["BOND"])

    assert actual
    assert isinstance(actual[0], PriceModel)
