import yahoo_fin.stock_info as sto


Amount = 5000

WSB = [ 
    'SPCE',
    'PLTR',
    'TSLA',
    'LCID',
    'IRNT',
    'GOEV'
]


DOG = [
    'AAPL',
    'BAC',
    'KO',
    'WFC',
    'AXP',
    'KHC',
]


def myround(x, prec=2, base=.05):
  return round(base * round(float(x)/base),prec)

def dogequity():
    prices = [(stock, myround(sto.get_live_price(stock))) for stock in DOG] # RETURNS STOCKS IN FORM OF ('TICKER', PRICE)
    print(prices)

def wsbequity():
    prices = [(stock, myround(sto.get_live_price(stock))) for stock in WSB]
    print(prices)

def btcprice():
    return myround(sto.get_live_price('ETH-USD'))