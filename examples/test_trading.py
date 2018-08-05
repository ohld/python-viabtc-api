import sys
from random import randint  # for generating unique operation ids
from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

EXCHANGE_URL = "http://localhost:8080/"
USER_ID = 1
USER_ID_2 = 2
UPDATE_MONEY = 0.1
ORDER_PRICE = 0.1

if len(sys.argv) > 1:
    EXCHANGE_URL = sys.argv[1]

api = ViaBTCAPI(EXCHANGE_URL)

# get consts from exchange
resp = api.market_list()
m = resp["result"][0]
market, stock, money = m["name"], m["stock"], m["money"]

# balance change
r = api.balance_query(user_id=USER_ID, asset=money)
balance_before = float(r["result"][money]["available"])

_ = api.balance_update(user_id=USER_ID, asset=money, amount=UPDATE_MONEY)

r = api.balance_query(user_id=USER_ID, asset=money)
balance_after = float(r["result"][money]["available"])

assert(balance_after == balance_before + UPDATE_MONEY)


# limit order creation
r = api.order_put_limit(
    user_id=USER_ID, market=market, side='BUY', amount=UPDATE_MONEY, price=ORDER_PRICE, 
    taker_fee_rate=0, maker_fee_rate=0)

r = api.order_depth(market=market, limit=10)
bid_prices = [float(b[0]) for b in r["result"]["bids"]]
assert(ORDER_PRICE in bid_prices)
bid_volume = [float(b[1]) for b in r["result"]["bids"] if float(b[0]) == ORDER_PRICE][0]


# create the second user and execute the order
_ = api.balance_update(user_id=USER_ID_2, asset=stock, amount=bid_volume)
r = api.order_put_limit(
    user_id=USER_ID_2, market=market, side='SELL', amount=bid_volume, price=ORDER_PRICE, 
    taker_fee_rate=0, maker_fee_rate=0)

r = api.order_depth(market=market, limit=10)
prices = [float(b[0]) for b in r["result"]["bids"] + r["result"]["asks"]]
assert(ORDER_PRICE not in prices)

# reset balances
for user_id in [USER_ID, USER_ID_2]:
    for asset in [money, stock]:
        r = api.balance_query(user_id=user_id, asset=asset)
        balance_current = float(r["result"][asset]["available"])
        r = api.balance_update(user_id=user_id, asset=asset, amount=(-1) * balance_current)

print("All tests have been passed!")
