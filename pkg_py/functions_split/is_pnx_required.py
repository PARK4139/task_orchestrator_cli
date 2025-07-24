from pytube import Playlist

from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def is_pnx_required(pnx):
    import os
    import string

    pk_print(f'''pnx={pnx}  {'%%%FOO%%%' if LTA else ''}''')
    if pnx == "":
        pk_print(f'''pnx가 입력되지 않았습니다  {'%%%FOO%%%' if LTA else ''}''')
        return 1
    connected_drives = []
    for drive_letter in string.ascii_uppercase:
        drive_path = drive_letter + ":\\"
        if os.path.exists(drive_path):
            connected_drives.append(drive_path)
            if pnx == drive_path:
                pk_print(f'''입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다  {'%%%FOO%%%' if LTA else ''}''')
                return 1
    if not os.path.exists(pnx):
        pk_print(f'''입력된 pnx가 존재하지 않습니다  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return 1
