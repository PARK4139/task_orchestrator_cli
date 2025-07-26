from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def load_f_video_on_losslesscut(f_video):
    if f_video is not None:
        if does_pnx_exist(f_video):
            cmd_to_os(cmd=rf'''start "" /MAX "{F_LOSSLESSCUT_EXE}" "{f_video}"''')
    else:
        ensure_printed(f'''f_video is None {'%%%FOO%%%' if LTA else ''}''')
