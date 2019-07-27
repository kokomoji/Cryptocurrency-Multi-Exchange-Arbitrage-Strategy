# -*- coding: utf-8 -*-

import os
import sys


root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402


'''
Example snippet to traverse GDAX / CoinBase Pro pagination.
Useful for reaching back more than 100 myTrades, the same works
for fetchClosedOrders
'''

exchange = ccxt.gdax({
        "apiKey":         "123456",
        "secret":         "/abcdefghijklmnop/w==",
        "password":       "987654321",
        "enableRateLimit":True
})

param_key = ''
param_value = ''
allMyTrades = []

while True:
    myTrades = exchange.fetch_my_trades(symbol = 'BTC/USD', params = { param_key:param_value })

    # Handle gdax with pagination ...
    if exchange.last_response_headers._store.get('cb-after'):
        param_key = 'after'
        param_value = exchange.last_response_headers._store['cb-after'][1]

        allMyTrades.extend(myTrades)

    else:
        allMyTrades.extend(myTrades)
        break

for trade in allMyTrades:
    print(trade)
