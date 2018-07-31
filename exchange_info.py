import sys
from random import randint  # for generating unique operation ids
from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

exchange_url = "http://localhost:8080/"
if len(sys.argv) > 1:
    exchange_url = sys.argv[1]

api = ViaBTCAPI(
    exchange_url, 
    _start_op_id=randint(0, 1000000),  # exchange require every operation id to be unique
                                       # all operations will increment this number before execution
)


resp = api.market_list()
print("Markets in exchange: ", [m["name"] for m in resp["result"]])

resp = api.asset_summary()
print("Assets on exchange: ", [a["name"] for a in resp["result"]])
for a in resp["result"]:
    print("{}:\ttotal: {}\tusers has: {}".format(a["name"], a["total_balance"], a["available_count"]))


    