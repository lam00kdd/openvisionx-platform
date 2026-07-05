import logging

from openvisionx.core.logger import (
    configure_logger,
    get_logger,
)


def test_configure_logger():

    logger = configure_logger()

    assert logger.name == "OpenVisionX"


def test_get_logger():

    logger = get_logger("GrayTool")

    assert logger.name.endswith("GrayTool")


def test_logger_level():

    logger = logging.getLogger("OpenVisionX")

    logger.setLevel(logging.DEBUG)

    assert logger.level == logging.DEBUG