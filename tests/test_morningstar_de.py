'''
Morningstar.de downloader.
'''
from finance_quote_python import Quote


exchange = 'FWB'
source = 'morningstar_de'


def test_fetch_vuke():
    '''
    basic fetching and parsing functionality 
    '''
    symbols = ['VUKE']
    q = Quote()
    q.set_source(source)
    q.set_currency('EUR')

    actual = q.fetch(exchange, symbols)

    assert actual is not None
