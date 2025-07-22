from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def move_pnx_v1(pnx, d_dst, with_overwrite=0, sequential_mode=0, timestamp_mode=0):
    import os
    import random
    import re
    import shutil
    import traceback

    try:
        if with_overwrite == 0:
            pnx_p = os.path.dirname(pnx)
            time_pattern = rf"{get_time_as_('now')}"
            pnx_n = get_n(pnx)
            pnx_x = get_x(pnx)
            pnx_with_timestamp = rf'{pnx_p}\{re.sub(pattern=r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}', repl='', string=pnx_n)}_{time_pattern}{random.randint(10, 99)}{pnx_x}'
            src_type = None
            if is_f(pnx):
                src_type = 'f'
            elif is_d(pnx):
                src_type = 'd'
            dst_n_timestamp_x = rf'{d_dst}\{get_nx(pnx_with_timestamp)}'

            if d_dst != os.path.dirname(pnx_with_timestamp):
                os.rename(pnx, pnx_with_timestamp)
                if not does_pnx_exist(pnx_with_timestamp):
                    shutil.move(src=pnx_with_timestamp, dst=d_dst)
                if LTA:
                    pk_print(working_str=rf'''time_pattern="{time_pattern}"  {'%%%FOO%%%' if LTA else ''}''')
                    pk_print(
                        working_str=rf'''src_type="{src_type:5s}" pnx_with_timestamp="{pnx_with_timestamp:<150}" dst="{d_dst:<50}" {'%%%FOO%%%' if LTA else ''}''',
                        print_color='green')
                    pk_print(
                        working_str=rf'''src_type={src_type} pnx_with_timestamp={pnx_with_timestamp.replace('\n', ''):<150} dst={d_dst.replace('\n', ''):<50}  {'%%%FOO%%%' if LTA else ''}''',
                        print_color='green')
                pk_print(
                    working_str=rf'''src_type={src_type} pnx_with_timestamp={pnx_with_timestamp:<150} dst={d_dst:<50}  {'%%%FOO%%%' if LTA else ''}'''.replace(
                        '\n', ''), print_color='green')
        elif with_overwrite == 1:
            if not is_f(pnx):
                pk_print(f"Source file does not exist: {pnx}")

            d_dst = os.path.dirname(d_dst)
            if d_dst and not os.path.exists(d_dst):
                os.makedirs(d_dst)
            try:
                if os.path.exists(d_dst):
                    os.remove(d_dst)  # Remove the existing file
                shutil.move(pnx, d_dst)
                pk_print(f"Successfully moved '{pnx}' to '{d_dst}'", print_color='green')
            except Exception as e:
                pk_print(f"Failed to move file: {e}")

    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
