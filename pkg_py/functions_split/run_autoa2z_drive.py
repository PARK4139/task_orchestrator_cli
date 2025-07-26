

from pkg_py.functions_split.is_window_opened import is_window_opened

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.is_window_opened import is_window_opened


def run_autoa2z_drive():
    import time

    window_title_seg = "AutoA2Z Drive"
    timeout = 5
    start_time = time.time()
    while 1:
        if time.time() - start_time > timeout:
            break
        if not is_window_opened(window_title_seg=window_title_seg):
            window_title_seg = "git log"
            pk_chdir(d_dst=rf"{D_HOME}\source\repos\ms_proto_drive")
            cmd = rf' start cmd.exe /k "title {window_title_seg}&& git log" '
            ensure_printed(str_working=rf'''cmd="{cmd}"  {'%%%FOO%%%' if LTA else ''}''')
            ensure_command_excuted_to_os(cmd=cmd, mode="a")
            break
        ensure_slept(milliseconds=1000)
