from client.telegram_notifier_client import notifier
import logging

logger = logging.getLogger(__name__)

async def receive_message():
    try:
        msgs:list[str] = await notifier.receive_message()
        logger.info("Polled: %s", msgs)
    except Exception as e:
        logger.error("Polling error: %s", e)
