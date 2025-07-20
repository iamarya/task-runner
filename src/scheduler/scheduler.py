from scheduler.telegram_task import telegram_recieve_task, telegram_send_task
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio


scheduler = AsyncIOScheduler()

scheduler.add_job(telegram_send_task, trigger='interval', seconds=15)
scheduler.add_job(telegram_recieve_task, trigger='interval', seconds=15)

async def init_async_scheduler():
    print("Starting scheduler...")
    scheduler.start()
    while True:
        await asyncio.sleep(3600)

def start_scheduler():
    asyncio.run(init_async_scheduler())

