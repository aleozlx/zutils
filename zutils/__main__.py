import os, sys, logging
from .backend import candidate_heaps
logger = logging.getLogger('zutils')

for api, heap in candidate_heaps.items():
    logger.info('{symbol} => {func}'.format(symbol=api, func=heap[0][1].__name__))
    logger.info('\tcandidates: {}'.format(list(map(lambda i: i[1].__name__, heap))))

