import logging
import os


def setup_logger():
    log_directory = os.path.join(os.path.dirname(__file__), '../logs')
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    log_file = os.path.join(log_directory, 'error_log.log')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    return logging.getLogger()
