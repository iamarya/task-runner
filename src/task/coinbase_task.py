from src.client.coinbase_client import main
import asyncio

import time
from notify.sender import send_message
from notify.reciever import receive_message
import asyncio
import logging



logger = logging.getLogger(__name__)

async def buy_btc_task():
    logger.info("Starting buy_btc_task")
    message = await main()
    if message:
        await send_message(f'buy_btc_task: {message}')