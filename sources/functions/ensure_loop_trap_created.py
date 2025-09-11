import time

import logging

from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_local_test_activate import LTA

@ensure_seconds_measured
def ensure_loop_trap_created():
    logging.debug("루프 트랩 인게이지")
    while 1:
        time.sleep(10)
        pass