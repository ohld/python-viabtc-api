import sys
from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

MARKET_NAME = "TESTNET3RINKEBY"
EXCHANGE_URL = "http://localhost:8080/"  # choose to your exchange url
api = ViaBTCAPI(EXCHANGE_URL)

ob = api.order_depth(market=MARKET_NAME)["result"]
bids = ob["bids"]
asks = ob["asks"]
for price, volume in bids[::-1]:
    print("BID\t price: {}\t volume: {}".format(price, volume))

for price, volume in asks:
    print("ASK\t price: {}\t volume: {}".format(price, volume))
