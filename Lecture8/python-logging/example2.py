import logging

logger = logging.getLogger('logger_sample')
logger.setLevel(logging.DEBUG)

# File handler
file_handler = logging.FileHandler(filename='example2.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s -- %(levelname)s:%(levelno)s -- %(message)s')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_formatter = logging.Formatter('%(name)s -- %(levelname)s -- %(message)s')
console_handler.setFormatter(console_formatter)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug(f'debug log')
logger.info('info log')
logger.warning('warning log')
logger.error('error log')
logger.critical('critical log')
