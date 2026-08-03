import time

from binance.enums import (
    FUTURE_ORDER_TYPE_MARKET,
    FUTURE_ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC,
)

from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order and return the latest order status.
    """
    try:
        logger.info(
            f"Sending MARKET order | Symbol={symbol} | Side={side} | Quantity={quantity}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity,
        )

        logger.info(f"Initial Response: {order}")

        # Wait briefly before fetching updated order status
        time.sleep(2)

        latest_order = client.futures_get_order(
            symbol=symbol,
            orderId=order["orderId"],
        )

        logger.info(f"Latest Response: {latest_order}")

        return latest_order

    except Exception as e:
        logger.exception(f"Market order failed: {e}")
        raise


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order and return the latest order status.
    """
    try:
        logger.info(
            f"Sending LIMIT order | Symbol={symbol} | Side={side} | Quantity={quantity} | Price={price}"
        )

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC,
        )

        logger.info(f"Initial Response: {order}")

        time.sleep(2)

        latest_order = client.futures_get_order(
            symbol=symbol,
            orderId=order["orderId"],
        )

        logger.info(f"Latest Response: {latest_order}")

        return latest_order

    except Exception as e:
        logger.exception(f"Limit order failed: {e}")
        raise