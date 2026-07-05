from openvisionx.core.logger import get_logger


def test_logger():

    logger = get_logger(__name__)

    logger.info("Logger OK")

    assert logger.name.endswith(__name__)