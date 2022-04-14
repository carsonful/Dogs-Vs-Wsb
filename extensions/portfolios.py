import yahoo_fin.stock_info as sto


Amount = 10000

WSB = [ 
    'SPY', # 4.5
    'GME', # 13.2
    'TSLA', # 2
    'AMD', # 20.4
    'WEBR', # 192.3
]
wsbShares = [
    4.5,
    13.2,
    2,
    20.4,
    192.3
]


DOG = [
    'DIS',
    'UBER',
    'QUASX',
    'IAC',
    'DXC',
]
dogShares = [
    15,
    62.5,
    35,
    20,
    65
]

def myround(x, prec=2, base=.05):
  return round(base * round(float(x)/base),prec)

def dogequity():
    prices = [(stock, myround(sto.get_live_price(stock))) for stock in DOG] # RETURNS STOCKS IN FORM OF ('TICKER', PRICE)
    total = 0 
    for i, value in enumerate(prices):
        total+= myround(value[1] * dogShares[i])
    print(total, 'DOG PROFIT / LOSS')
    return total - 10012.7 # added 12.7 because of uneven start


def wsbequity():
    prices = [(stock, myround(sto.get_live_price(stock))) for stock in WSB]
    total = 0
    for i, value in enumerate(prices):
        total += myround(value[1] * wsbShares[i])
    print(total, 'WSB PROFIT / LOSS')
    return total - 10000





