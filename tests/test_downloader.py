'''
Test downloaders
'''
#from finance_quote_python.boerse_frankfurt import FwbDownloader
from finance_quote_python.morningstar import MorningstarDownloader
from pricedb import SecuritySymbol


# def test_fwb():
#     ''' fwb download '''
#     dl = FwbDownloader()
#     symbol = SecuritySymbol("FWB", "VGOV")
#     actual = dl.download(symbol, "EUR")

#     assert actual is not None

def test_xfra_morningstar():
    ''' Test dowloading Boerse Frankfurt prices through Morningstar '''
    dl = MorningstarDownloader()
    symbol = SecuritySymbol("FWB", "VGOV")
    actual = dl.download(symbol, "EUR")

    assert actual is not None
    assert actual > 0

def test_fwb_vmid():
    ''' try to download the price for FTSE 250 ETF '''
    dl = MorningstarDownloader()
    symbol = SecuritySymbol("FWB", "VMID")
    actual = dl.download(symbol, "EUR")

    assert actual is not None
    assert actual > 0
