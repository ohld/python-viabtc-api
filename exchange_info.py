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


resp = api.market_list()
print(resp)
market_names = [m["name"] for m in resp["result"]]
print("Markets in exchange: ", market_names)

for market in market_names:
    ob = api.order_depth(market=market)
    print(market, ob["result"])

resp = api.asset_summary()
asset_names = [a["name"] for a in resp["result"]]
print("Assets on exchange: ", asset_names)
for a in resp["result"]:
    print("{}:\ttotal: {}\tusers has: {}".format(a["name"], a["total_balance"], a["available_count"]))

