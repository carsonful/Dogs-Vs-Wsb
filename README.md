
# WSBvsDOGS

<img src="https://cdn.discordapp.com/attachments/951616423745167370/964639145156825178/c98340_3ce9a3dfc6da439bb3083b224c3f2b3a_mv2.jpeg" data-canonical-src="https://cdn.discordapp.com/attachments/951616423745167370/964639145156825178/c98340_3ce9a3dfc6da439bb3083b224c3f2b3a_mv2.jpeg" width="550" height="400" />


> If you'd like to contact me please looked at my [ReadMe](https://github.com/carsonful/carsonful) on how to reach me.

---

### Table of Contents
All sections regarding this repository.
- [Tutorial](#tutorial)
- [Description](#description)
- [How To Use](#how-to-use)
- [References](#References)
- [License](#license)
- [Author Info](#author-info)

---

## Tutorial

If you'd like to recreate this program, you can change the **portfolio.py** folder and put 
in your own stock tickers. This will then change the output of the equity 


```py
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
```

Change what your subtracting from the total, to whatever the amount of money your giving each portfolio, and the names. DOG and WSB both are lists of stock tickers.

---

## Description

This program allows for a stock portfolio comparison that allows two portfolios to be 
compared live when the stock market is open. Currently updates every 2 minutes and 30 seconds (yahoo finance updates around that interval).
This allows for data to be readable and not a line that goes up and down every couple of minutes.



For example:


<img src="https://cdn.discordapp.com/attachments/951616423745167370/964650352827826246/snapchat.png" data-canonical-src="https://cdn.discordapp.com/attachments/951616423745167370/964650352827826246/snapchat.png" width="700" height="400"/>

The market was closed during the time of this snapshot the currency wouldn't change but, here is just an example of the interface.

#### Resources

- Yahoo Finance
- Highchart.js
- Jquery
- Ajax
- Flask


[Back To The Top](#WSBvsDOGS)

---

## How To Use

#### Installation
To be able to execute this code you will need **these** modules:
**SEE REQUIREMENTS.TXT FOR MODULES**
1. Make sure `requirements.txt` is in your environment.
2. cd to your directory where the file is.
3. run the command `pip install -r requirements.txt` in your shell.

#### Yahoo Finance API Reference

```py
import yahoo_fin.stock_info as sto

DOG = [
    'DIS',
    'UBER',
    'QUASX',
    'IAC',
    'DXC',
]

def dogequity():
    prices = [(stock, myround(sto.get_live_price(stock))) for stock in DOG] 
    #Makes a list of tuples which returns as ('TICKER', PRICE)
    
    return prices
        
```
[Back To The Top](#WSBvsDOGS) 

---

## References
- [Highchart.js](https://www.highcharts.com/docs/index) Docs
- [yahoo_fin](https://theautomatic.net/yahoo_fin-documentation/) Docs
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) Docs


[Back To The Top](#WSBvsDOGS)

---

## License

MIT License

Copyright (c) [2022] [Carson Fulmer]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

[Back To The Top](#WSBvsDOGS)

---

## Author Info

- LinkedIn - [Carson Fulmer](https://www.linkedin.com/in/carsonfulmer/)
- Website - [Carson Fulmer](http://carsonfulmer.com)

[Back To The Top](#WSBvsDOGS)



