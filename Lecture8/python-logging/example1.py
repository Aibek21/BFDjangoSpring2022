import logging

logging.basicConfig(filename='example1.log',
                    level=logging.DEBUG,
                    filemode='w',  # w - write, a - append(default)
                    format='%(asctime)s -- %(levelname)s:%(levelno)s -- %(message)s')

test_message = 'Someone'

logging.debug(f'debug log {test_message}')
logging.info('info log')
logging.warning('warning log')
logging.error('error log')
logging.critical('critical log')
