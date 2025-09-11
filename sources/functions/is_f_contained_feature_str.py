from sources.objects.pk_local_test_activate import LTA
import logging


def is_f_contained_feature_str(feature_str, d_pnx):
    import os
    if not os.path.exists(d_pnx):
        logging.debug(f'''Directory does not exist: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
        return 0
    for filename in os.listdir(d_pnx):
        if feature_str in filename:
            return 1
    return 0
