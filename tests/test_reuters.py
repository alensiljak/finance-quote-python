'''
Test Reuters download
'''
from finance_quote_python import Quote


source = 'reuters'


def test_download():
    symbols = ['VUKE']
    # , 'VMID', 'VGOV'
    q = Quote()
    q.set_source(source)

    actual = q.fetch('FWB', symbols)

    assert actual is not None
