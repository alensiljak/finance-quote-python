""" Various tests for fetching the prices """
import pytest
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
    """ The result is a hash.
    """
    assert False