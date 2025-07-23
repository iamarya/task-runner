from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

from task.telegram_task import telegram_recieve_task, telegram_send_task
from task.factor_task import factor_send_task


scheduler = AsyncIOScheduler()

scheduler.add_job(factor_send_task, trigger='interval', seconds=15)
scheduler.add_job(telegram_recieve_task, trigger='interval', seconds=15)

async def init_async_scheduler():
    print("Starting scheduler...")
    scheduler.start()
    while True:
        await asyncio.sleep(3600)

def start_scheduler():
    asyncio.run(init_async_scheduler())

