from notify.telegram_notifier import TelegramNotifier
notifier = TelegramNotifier()

async def send_message(message):
    await notifier.send_message(message)