'''
Test Franfurt Stock Exchange downloader.
'''
from finance_quote_python import Quote


exchange = 'FWB'
source = 'boerse_frankfurt'


def test_fetch_vuke():
    '''
    basic fetching and parsing functionality 
    https://www.boerse-frankfurt.de/etp/IE00B810Q511
    '''
    symbols = ['VUKE']
    q = Quote()
    q.set_source(source)

    actual = q.fetch(exchange, symbols)

    assert actual is not None
