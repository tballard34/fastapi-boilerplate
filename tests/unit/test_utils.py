import logging

from app.utils import get_logger


def test_get_logger_returns_correct_logger():
    """Ensure get_logger returns a logging.Logger with the given name."""
    logger_name = "sample-test-logger"
    logger = get_logger(logger_name)

    assert isinstance(logger, logging.Logger)
    assert logger.name == logger_name
