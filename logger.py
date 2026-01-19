import logging
import os
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()


def setup_logger(name: str = "lead_generation") -> logging.Logger:
    """
    Setup and return a configured logger instance
    """

    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    log_file = os.getenv("LOG_FILE", "logs/app.log")

    # Create logs directory if not exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # Log format
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File handler (rotating)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Global logger instance
logger = setup_logger()
