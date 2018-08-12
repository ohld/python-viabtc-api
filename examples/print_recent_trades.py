# Show recent trades that were executed.
# Very usefull in development debug.

from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

EXCHANGE_URL = "http://localhost:8080/"  # choose to your exchange url
api = ViaBTCAPI(EXCHANGE_URL)

print_last_deals = 20
result = api.market_deals("TESTNET3RINKEBY", limit=print_last_deals)
for order in result['result']:
    print(order)