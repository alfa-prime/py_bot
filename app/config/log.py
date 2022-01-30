import logging
import time
from pathlib import Path

from .app import settings

LOG_LEVELS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]

# маппер для настройки вывода логов
LOG_HANDLERS = {
    "CONSOLE": lambda: (logging.StreamHandler(),),
    "FILE": lambda: (logging.FileHandler(set_log_file_name()),),
    "CONSOLE_AND_FILE": lambda: (logging.StreamHandler(), logging.FileHandler(set_log_file_name()),),
}


def set_log_file_name():
    file_name = time.strftime("%Y-%m-%d-%H_%M_%S") + '.log'
    dir_ = Path('./', 'logs')
    if not dir_.exists():
        dir_.mkdir()
    return Path(dir_, file_name)


# если LOG_OUTPUT не указан или указан неверно, то устанавливается вывод в CONSOLE
handlers = LOG_HANDLERS[settings.log_output]() if settings.log_output in LOG_HANDLERS else LOG_HANDLERS["CONSOLE"]()

# если LOG_LEVEL не указан или указан неверно, устанавливается уровень INFO
level = settings.log_level if settings.log_level in LOG_LEVELS else "INFO"


logging.basicConfig(
    handlers=handlers,
    format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
    level=level
)

logger = logging.getLogger(__name__)
