"""Sets up a logger"""
import logging
import sys

logger = logging.getLogger('papermill')
logging.basicConfig(filename="papermill-nb-runner.out", level=logging.INFO)

h1 = logging.StreamHandler(sys.stdout)
h1.setLevel(logging.DEBUG)
h1.addFilter(lambda record: record.levelno <= logging.INFO)

h2 = logging.StreamHandler()
h2.setLevel(logging.WARNING)

logging.getLogger().addHandler(h1)
logging.getLogger().addHandler(h2)
