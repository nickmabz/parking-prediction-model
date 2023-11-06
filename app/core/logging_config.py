import logging.config
import os

# Ensure the logs directory exists
logs_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_dir, exist_ok=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


def get_level_number(level_name):
    level_number = getattr(logging, level_name, None)
    if isinstance(level_number, int):
        return level_number
    raise ValueError(f'Invalid log level: {level_name}')


class LogLevelFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = get_level_number(level)

    def filter(self, record):
        return record.levelno == self.level


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "info_filter": {
            "()": LogLevelFilter,
            "level": "INFO",
        },
        "warning_filter": {
            "()": LogLevelFilter,
            "level": "WARNING",
        },
        "error_filter": {
            "()": LogLevelFilter,
            "level": "ERROR",
        },
    },
    "handlers": {
        "info_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detailed",
            "filename": "logs/info.log",
            "filters": ["info_filter"],
            "maxBytes": 10485760,  # 10 MB
            "backupCount": 10,
        },
        "warning_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detailed",
            "filename": "logs/warning.log",
            "filters": ["warning_filter"],
            "maxBytes": 10485760,  # 10 MB
            "backupCount": 10,
        },
        "error_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detailed",
            "filename": "logs/error.log",
            "filters": ["error_filter"],
            "maxBytes": 10485760,  # 10 MB
            "backupCount": 10,
        },
    },
    "formatters": {
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "loggers": {
        "uvicorn": {"level": LOG_LEVEL, "handlers": ["info_file", "warning_file", "error_file"]},
        "fastapi": {"level": LOG_LEVEL, "handlers": ["info_file", "warning_file", "error_file"]},
        "app": {"level": LOG_LEVEL, "handlers": ["info_file", "warning_file", "error_file"]},
    },
    "root": {
        "level": LOG_LEVEL,
        "handlers": ["info_file", "warning_file", "error_file"],
    },
}


def setup_logging():
    try:
        logging.config.dictConfig(LOGGING_CONFIG)
    except Exception as e:
        logging.basicConfig(level=logging.INFO)
        logging.error(f"Failed to configure logging: {e}", exc_info=True)
