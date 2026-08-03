import argparse

from bot.logging_config import logger
from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

parser = argparse.ArgumentParser(
    description="Binance Futures Testnet Trading Bot"
)

parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
parser.add_argument("--side", required=True, help="BUY or SELL")
parser.add_argument("--type", required=True, help="MARKET or LIMIT")
parser.add_argument("--quantity", required=True, help="Order quantity")
parser.add_argument("--price", help="Price (required for LIMIT orders)")

args = parser.parse_args()

try:
    symbol = args.symbol.upper()
    side = validate_side(args.side)
    order_type = validate_order_type(args.type)
    quantity = validate_quantity(args.quantity)
    price = validate_price(args.price, order_type)

    print("\n========== ORDER ==========")
    print(f"Symbol : {symbol}")
    print(f"Side   : {side}")
    print(f"Type   : {order_type}")
    print(f"Qty    : {quantity}")

    if price is not None:
        print(f"Price  : {price}")

    print("===========================\n")

    if order_type == "MARKET":
        response = place_market_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
        )
    else:
        response = place_limit_order(
            symbol=symbol,
            side=side,
            quantity=quantity,
            price=price,
        )

    print("\nSUCCESS")
    print("=" * 40)
    print(f"Order ID       : {response.get('orderId')}")
    print(f"Symbol         : {response.get('symbol')}")
    print(f"Side           : {response.get('side')}")
    print(f"Order Type     : {response.get('type')}")
    print(f"Status         : {response.get('status')}")
    print(f"Original Qty   : {response.get('origQty')}")
    print(f"Executed Qty   : {response.get('executedQty')}")
    print(f"Cumulative Qty : {response.get('cumQty', response.get('executedQty'))}")
    print(f"Average Price  : {response.get('avgPrice', 'N/A')}")
    print("=" * 40)

except Exception as e:
    logger.exception("CLI execution failed")

    print("\nFAILED")
    print("=" * 40)
    print(f"Error: {e}")