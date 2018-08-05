from ViaBTCAPI.ViaBTCAPI import ViaBTCAPI

EXCHANGE_URL = "http://localhost:8080/"  # choose to your exchange url
api = ViaBTCAPI(EXCHANGE_URL)

# consts
user_id = 2
asset = "BTC"
market = "BTCETH"
side = "BUY"

print("\n", "update balance")
print(api.balance_update(user_id=user_id, asset=asset, amount=100.123))

print("\n", "get balance")
print(api.balance_query(user_id=user_id, asset=asset))

print("\n", "see balance change history")
print(api.balance_history(user_id=user_id, asset=asset))

print("\n", "put order")
print(api.order_put_limit(
    user_id=user_id, market=market, side=side, amount=100, price=1.5, 
    taker_fee_rate=0.0001, maker_fee_rate=0.0001
))

print("\n", "get orderbook")
print(api.order_depth(market=market, limit=10))

print("\n", "get all exchange assets summary")
print(api.asset_summary())