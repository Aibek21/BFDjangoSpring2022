import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

file_handler = RotatingFileHandler('example3.log', maxBytes=100, backupCount=10)
file_formatter = logging.Formatter('%(name)s -- %(levelname)s -- %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)

for i in range(40):
    logger.error(f'test message: {i}')
