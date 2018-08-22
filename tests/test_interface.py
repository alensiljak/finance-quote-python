"""
Test the original F::Q interfaces.
See https://github.com/finance-quote/finance-quote for the list.
Used as the base for TDD.
"""
from finance_quote_python import Quote


def test_new():
    """ just create a new object without new() """
    q = Quote()
    assert q is not None

def test_fetch():
    """ test for fetch method """
    q = Quote()
    q.set_source("vanguard_au")
    actual = q.fetch("vanguard", ["BOND"])
    
    assert actual is not None
    assert actual

def test_sources():
    """ Fetch the list of available sources / agents """
    from finance_quote_python.finance import DownloadSources
    q = Quote()
    sources = q.sources

    assert sources is not None
    assert sources
    assert len(sources) == len(DownloadSources)

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
