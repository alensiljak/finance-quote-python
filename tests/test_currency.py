""" Test fetching the currency exchange rates """
from decimal import Decimal
from pricedb import PriceModel
from finance_quote_python import Quote


def test_aud_eur_fixerio():
    """ a basic test.
    Use the default provider (fixerio) and fetch a rate.
    """
    q = Quote()
    actual = q.currency("AUD", "EUR")

    assert actual is not None
    assert isinstance(actual, PriceModel)
    assert actual.value != Decimal(0)


def test_parameters_case_insensitive():
    """ parameters must be case insensitive """
    q = Quote()
    # the default provider should be used
    #q.set_source("fixerio")
    actual = q.currency("AuD", "eur")

    assert actual is not None
    assert actual.value != Decimal(0)
    assert isinstance(actual, PriceModel)
