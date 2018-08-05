"""
This script will show the information about the exchange on address {EXCHANGE_URL}.
You can use it for an exchange API debug or just to monitor activity on your exchange.

USAGE:
You need to change EXCHANGE_URL to your ViaBTC exchange server's `accesshttp` port. 
Or you can just pass the URL as command line argument list this:
``` 
    python3 exchange_info.py http://localhost:8080/
```

Author: @okhlopkov
"""

import sys
from random import randint  # for generating unique operation ids
from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

EXCHANGE_URL = "http://localhost:8080/"
if len(sys.argv) > 1:
    EXCHANGE_URL = sys.argv[1]

api = ViaBTCAPI(
    EXCHANGE_URL, 
    _start_op_id=randint(0, 1000000),  # exchange require every operation id to be unique
                                       # all operations will increment this number before execution
)


print("Exchange address: {}".format(EXCHANGE_URL))

print("\n{0}\nMarkets\n{0}".format("-" * 50))

resp = api.market_list()
market_names = [m["name"] for m in resp["result"]]
print("Exchange markets: ", market_names)

for market in market_names:
    last = api.market_last(market)
    print(market, last["result"])

print("\nMarket summary:")
for market in market_names:
    info = api.market_summary(market)
    print(market, info["result"])

print("\nMarket status last week:")
for market in market_names:
    status = api.market_status(market, period=86400 * 7)
    print(market, status["result"])

print("\nMarket status last 24h:")
for market in market_names:
    status = api.market_status_today(market)
    print(market, status["result"])

# Don't know how to call this method, see:
# https://github.com/viabtc/viabtc_exchange_server/issues/125
# print("\nMarket KLine:")
# for market in market_names:
#     kline = api.market_kline(market, 0, 0, 0)
#     print(market, kline["result"])




print("\n{0}\nOrders\n{0}".format("-" * 50))

print("\nOrderbooks:")
for market in market_names:
    ob = api.order_depth(market=market)
    print(market, ob["result"])

print("\nExecuted orders:")
for market in market_names:
    history = api.market_deals(market=market, limit=100, last_id=0)
    print(market, history["result"])




print("\n{0}\nAssets\n{0}".format("-" * 50))

asset_list = api.asset_list()
print("\nAssets on exchange:")
for asset in asset_list["result"]:
    print(asset)

resp = api.asset_summary()
for a in resp["result"]:
    print("{}:\ttotal: {}\tusers has: {}".format(a["name"], a["total_balance"], a["available_count"]))

