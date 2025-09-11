from sources.objects.pk_local_test_activate import LTA
from sources.functions.is_d import is_d
import logging


def is_leaf_d(d):
    import traceback

    import os
    logging.debug(f'''d={d}  {'%%%FOO%%%' if LTA else ''}''')
    try:
        contents = os.listdir(d)
        if len(contents) > 0:
            return 0
        for content in contents:
            pnx = os.path.join(d, content)
            if is_d(pnx):
                return 0
        return 1
    except:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
