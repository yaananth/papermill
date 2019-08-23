"""Sets up a logger"""
import logging

logger = logging.getLogger('papermill')
logging.basicConfig(filename="papermill-nb-runner.out", level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler())
