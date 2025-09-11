from pathlib import Path


from sources.objects.pk_local_test_activate import LTA
import logging


def save_d_to_f(d, f):
    with open(f, "w", encoding='utf-8') as f_obj:
        d = Path(d)
        f_obj.write(d)
        if LTA:
            logging.debug(f'''d={d} %%%FOO%%%''')
