





from typing import TypeVar

from sources.objects.pk_local_test_activate import LTA
import logging

# , pk_measure_memory
# from sources.objects.time_and_lanauge_util import sleep

T = TypeVar('T')


def todo(id):
    logging.debug(f'''여기 할 차례입니다. at {id}. {'%%%FOO%%%' if LTA else ''}''')
    raise
