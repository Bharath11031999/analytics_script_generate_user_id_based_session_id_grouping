import logging
import os


def setup_logging(cron_job_name, env='dev', level=logging.INFO):
    # Create log directory if it doesn't exist
    log_dir = os.path.join(os.path.expanduser('~'), 'cron_jobs_logs')
    os.makedirs(log_dir, exist_ok=True)

    app_dir = os.path.join(log_dir, f'{env}_app_logs')
    os.makedirs(app_dir, exist_ok=True)

    # Create app-specific log filename using the cron job name
    log_filename = cron_job_name + '.log'
    log_filepath = os.path.join(app_dir, log_filename)

    # Create a logger object with the specified level
    logger = logging.getLogger()
    logger.setLevel(level)

    # Create a file handler
    file_handler = logging.FileHandler(log_filepath, mode='a')
    file_handler.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - Thread:%(thread)d - %(message)s')

    # Add the formatter to the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger
