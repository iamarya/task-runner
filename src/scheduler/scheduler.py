from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

from task.telegram_task import telegram_recieve_task, telegram_send_task
from task.factor_task import factor_send_task
from task.coinbase_task import buy_btc_task



scheduler = AsyncIOScheduler()

scheduler.add_job(factor_send_task, trigger='cron', hour=10, minute=0)
scheduler.add_job(telegram_recieve_task, trigger='interval', seconds=36000)
scheduler.add_job(buy_btc_task, trigger='cron', day=1, hour=11, minute=0)

async def init_async_scheduler():
    print("Starting scheduler...")
    scheduler.start()
    while True:
        await asyncio.sleep(3600)

def start_scheduler():
    asyncio.run(init_async_scheduler())

