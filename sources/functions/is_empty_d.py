

from sources.objects.pk_local_test_activate import LTA
import logging


def is_empty_d(d_src, debug_mode=True):
    import os
    import traceback

    try:
        if len(os.listdir(d_src)) == 0:
            return 1
        else:
            return 0
    except:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
        return None
