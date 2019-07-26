'''
Test Reuters download
'''
from finance_quote_python import Quote


#exchange = 'FWB'
source = 'reuters'


def test_download():
    symbols = ['VUKE']
    q = Quote()
    q.set_source(source)

    actual = q.fetch('FWB', symbols)

    assert actual is not None
