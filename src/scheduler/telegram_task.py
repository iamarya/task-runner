import time
from notify.sender import send_message
from notify.reciever import receive_message
import asyncio

async def telegram_send_task():
    print(f"[{time.strftime('%X')}] Scheduled job ran for telegram")
    await send_message(f"[{time.strftime('%X')}] Scheduled job ran for telegram")

async def telegram_recieve_task():
    await receive_message()

    