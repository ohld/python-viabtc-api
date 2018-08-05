import sys
from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

EXCHANGE_URL = "http://localhost:8080/"  # choose to your exchange url
api = ViaBTCAPI(EXCHANGE_URL)

if len(sys.argv) - 1 != 3:
    print("USAGE: {} <user_id> <asset> <amount>".format(sys.argv[0]))
    exit()

user_id = int(sys.argv[1])
asset = str(sys.argv[2])
amount = str(sys.argv[3])

resp = api.balance_update(user_id, asset, amount)
print(resp["result"]["status"])
