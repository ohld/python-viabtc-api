# pass user ids as a cli arguments to shor their balances
# works perfectly with 'watch' utility: 
# $ watch python3 print_balances.py 1 2 3

import sys
from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

EXCHANGE_URL = "http://localhost:8080/"  # choose to your exchange url
api = ViaBTCAPI(EXCHANGE_URL)

if len(sys.argv) == 1:
    print("Pass user_ids as arguments")
    exit()

user_ids = [int(i) for i in sys.argv[1:]]

for user_id in user_ids:
    balances = api.balance_query(user_id)
    bal_str = ""
    for asset in balances["result"]:
        a = balances["result"][asset]
        bal_str += "{0}:\t {1:0.5f} ({2:0.5f})\t ".format(asset, float(a["available"]), float(a["freeze"]))
    print("{}:\t {}".format(user_id, bal_str))