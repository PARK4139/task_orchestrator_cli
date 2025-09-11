

from sources.functions.is_window_opened import is_window_opened

from sources.functions.ensure_command_executed import ensure_command_executed


from sources.objects.pk_local_test_activate import LTA
import logging


from sources.objects.pk_local_test_activate import LTA
from sources.functions.ensure_command_executed import ensure_command_executed

import logging
from sources.functions.is_window_opened import is_window_opened


def run_autoTBD_drive():
    import time

    window_title_seg = "AutoTBD Drive"
    timeout = 5
    start_time = time.time()
    while 1:
        if time.time() - start_time > timeout:
            break
        if not is_window_opened(window_title_seg=window_title_seg):
            window_title_seg = "git log"
            os.chdir(rf"{D_HOME}\source\repos\ms_proto_drive")
            cmd = rf' start cmd.exe /k "title {window_title_seg}&& git log" '
            logging.debug(rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
            ensure_command_executed(cmd=cmd, mode="a")
            break
        ensure_slept(milliseconds=1000)
