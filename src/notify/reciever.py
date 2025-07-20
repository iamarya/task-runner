from notify.telegram_notifier import TelegramNotifier

notifier = TelegramNotifier()

async def receive_message():
    try:
        msgs:list[str] = await notifier.receive_message()
        print("Polled:", msgs)
    except Exception as e:
        print("Polling error:", e)
