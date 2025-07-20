from client.telegram_notifier_client import notifier

async def send_message(message):
    await notifier.send_message(message)