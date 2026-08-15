"""Simple logger wrapper."""
import logging

logger = logging.getLogger('network_scanner')
logger.addHandler(logging.StreamHandler())
