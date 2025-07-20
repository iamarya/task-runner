from client.telegram_notifier_client import notifier

async def receive_message():
    try:
        msgs:list[str] = await notifier.receive_message()
        print("Polled:", msgs)
    except Exception as e:
        print("Polling error:", e)
