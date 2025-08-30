import os
from dotenv import load_dotenv
from coinbase.rest import RESTClient
import uuid
load_dotenv()
import logging



logger = logging.getLogger(__name__)

class CoinbaseClient:
    def __init__(self):
        self.api_key = os.getenv('COINBASE_API_KEY')
        self.api_secret = os.getenv('COINBASE_API_PRIVATE_KEY')
        self.client = RESTClient(self.api_key, self.api_secret)

    def get_usdc_balance(self):
        try:
            accounts = self.client.get_accounts()
            for account in accounts['accounts']:
                if account['currency'] == 'USDC':
                    return float(account['available_balance']['value'])
            return 0.0
        except Exception as e:
            print(f"Error fetching USDC balance: {e}")
            return None

    def buy_btc_with_usdc(self):
        usdc_balance = self.get_usdc_balance()
        if usdc_balance > 100:
            # Get latest BTC-USDC price
            try:
                ticker = self.client.get_product(product_id='BTC-USDC')
                latest_price = float(ticker['price'])
                target_price = round(latest_price * 0.99, 2)  # 1% below
                size = round(100 / target_price, 8)
                print(f"Latest BTC-USDC price: {latest_price}, placing buy order at: {target_price}")
                buy_order = self.client.limit_order_gtc_buy(
                    product_id='BTC-USDC',
                    client_order_id=str(uuid.uuid4()),
                    limit_price=str(target_price),
                    base_size=str(size)
                )
                if buy_order.success:
                    print(f"Buy order placed successfully: {buy_order}")
                    return "Success"
                else:
                    print(f"Buy order failed: {buy_order}")
                return "Buy order failed"
            except Exception as e:
                print(f"Error placing buy order: {e}")
                return "Error placing buy order"
        else:
            print("USDC balance is not sufficient to place order.")
            return "USDC balance is not sufficient"

    def _get_account_id(self, currency):
        accounts = self.client.get_accounts()
        for account in accounts['data']:
            if account['currency'] == currency:
                return account['id']
        return None

import asyncio

async def main():
    cb_client = CoinbaseClient()
    loop = asyncio.get_event_loop()
    usdc_balance = await loop.run_in_executor(None, cb_client.get_usdc_balance)
    print(f"Current USDC balance: {usdc_balance}")

if __name__ == "__main__":
    asyncio.run(main())
