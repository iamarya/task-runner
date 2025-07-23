import logging

from config.custom_logger import CustomFormatter


def setup():
    # Define format for logs
    fmt ='%(asctime)s | %(levelname)8s | %(module)25s | %(message)s'
    
    # Create stdout handler for logging to the console (logs all five levels)
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.setFormatter(CustomFormatter(fmt))
    logging.basicConfig(level=logging.ERROR, handlers=[stdout_handler])

    logging.getLogger('notify').setLevel(logging.INFO)
    logging.getLogger('client').setLevel(logging.INFO)
    logging.getLogger('notify').setLevel(logging.INFO)
    logging.getLogger('scheduler').setLevel(logging.INFO)
    logging.getLogger('task').setLevel(logging.INFO)

