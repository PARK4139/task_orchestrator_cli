import logging
from sources.objects.pk_local_test_activate import LTA


def get_f_contained_feature_str(feature_str, d_pnx):
    import os
    if not os.path.exists(d_pnx):
        logging.debug(f'''Directory does not exist: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
        return None
    else:
        logging.debug(f'''Searching for feature_str="{feature_str}" in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    for filename in os.listdir(d_pnx):
        if feature_str in filename:
            full_path = os.path.join(d_pnx, filename)
            logging.debug(f'''Found file: {full_path}  {'%%%FOO%%%' if LTA else ''}''')
            return full_path
    else:
        logging.debug(f'''No file containing feature_str="{feature_str}" found in directory: {d_pnx}  {'%%%FOO%%%' if LTA else ''}''')
    return None
