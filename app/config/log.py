import logging
import time
from pathlib import Path

from .app import settings


def set_log_level():
    if settings.log_level not in ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]:
        print("Check LOG_LEVEL values in .env file, the log level will be INFO")
        settings.log_level = "INFO"
    return settings.log_level


def set_log_file_name():
    time_stamp = time.strftime("%Y-%m-%d-%H_%M_%S")
    file_name = time_stamp + '.log'
    dir_ = Path('./', 'logs')

    if not dir_.exists():
        dir_.mkdir()

    return Path(dir_, file_name)


def set_log_handlers():
    log_console = logging.StreamHandler()
    log_file_name = set_log_file_name()

    if settings.log_output == 'CONSOLE_AND_FILE':
        log_file = logging.FileHandler(log_file_name)
        handlers = (log_file, log_console)

    elif settings.log_output == 'CONSOLE':
        handlers = (log_console,)

    elif settings.log_output == 'FILE':
        log_file = logging.FileHandler(log_file_name)
        handlers = (log_file,)

    else:
        print("Check LOG_OUTPUT values in .env file, the log will be output to the CONSOLE")
        handlers = (log_console,)

    return handlers


logging.basicConfig(
    handlers=set_log_handlers(),
    format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
    level=set_log_level()
)

logger = logging.getLogger(__name__)
