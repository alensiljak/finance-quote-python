"""
Test the original F::Q interfaces.
See https://github.com/finance-quote/finance-quote for the list.
Used as the base for TDD.
"""
from finance_quote_python import Quote


def test_new():
    """ just create a new object without new() """
    obj = Quote()
    assert obj is not None

def test_fetch():
    """ test for fetch method """
    assert False

def test_sources():
    assert False

def test_currency_lookup():
    assert False

def test_currency():
    assert False

def test_set_currency():
    assert False

def test_failover():
    assert False

# user_agent
# scale_field
# isotTime
