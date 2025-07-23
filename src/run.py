import threading
import signal
import sys
from scheduler.scheduler import start_scheduler
from flask import Flask
from app.routes import register_routes
import asyncio
import logging
from config import log_configs

log_configs.setup()


def graceful_exit(*args):
    print("\nShutting down...")
    sys.exit(0)

# Register Ctrl+C handler
signal.signal(signal.SIGINT, graceful_exit)
signal.signal(signal.SIGTERM, graceful_exit)

# start
app = Flask(__name__)
register_routes(app)

if __name__ == '__main__':
    scheduler_thread = threading.Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()

    # Run Flask in the main thread — this allows Ctrl+C to interrupt
    app.run(host="0.0.0.0", port=5000)
