from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def load_f_video_on_losslesscut(f_video):
    if f_video is not None:
        if does_pnx_exist(f_video):
            cmd_to_os(cmd=rf'''start "" /MAX "{F_LOSSLESSCUT_EXE}" "{f_video}"''')
    else:
        pk_print(f'''f_video is None {'%%%FOO%%%' if LTA else ''}''')
