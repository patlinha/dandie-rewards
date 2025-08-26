import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.getLogger("dundie")
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    "l:%(lineno)d f:%(filename)s: %(message)s"
)


def get_logger(logfile="dundie.log"):
    """Returns a configured log"""
    # ch = logging.StreamHandler()
    # ch.setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        logfile, maxBytes=300, backupCount=10  # 10**6
    )
    fh.setLevel(LOG_LEVEL)
    # ch.setFormatter(fmt)
    fh.setFormatter(fmt)
    # log.addHandler(ch)
    log.addHandler(fh)
    return log
