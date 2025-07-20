from notify.notifier import Notifier

import telegram
from dotenv import load_dotenv

import os
import logging


load_dotenv()

logger = logging.getLogger(__name__)

class TelegramNotifier(Notifier):
    def __init__(self):
        self.bot = telegram.Bot(os.getenv('TELEGRAM_TOKEN'))
        self.offset = None
    async def send_message(self, message):
        await self.bot.send_message(chat_id=os.getenv('TELEGRAM_CHAT_ID'), text=message)

    async def receive_message(self)-> list[str]:
        updates = await self.bot.get_updates(offset=self.offset, timeout=1)
        messages = []
        for update in updates:
            if update.message:
                messages.append(update.message)
                self.offset = update.update_id + 1
        return messages
        
notifier = TelegramNotifier()