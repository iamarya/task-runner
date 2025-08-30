import time
from notify.sender import send_message
from notify.reciever import receive_message
import asyncio
from client.factor_client import check_balance
import logging



logger = logging.getLogger(__name__)

async def factor_send_task():
    logger.info("Starting factor_send_task")
    message = await check_balance()
    if message:
        await send_message(f'factor_send_task: {message}')