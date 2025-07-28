import os

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.get_list_from_f import get_list_from_f
from pkg_py.functions_split.is_empty_d import is_empty_d
from pkg_py.functions_split.move_pnx import move_pnx
from pkg_py.functions_split.ensure_pnxs_moved_to_trash_bin import ensure_pnxs_moved_to_trash_bin
from pkg_py.functions_split.ensure_pnxs_move_to_recycle_bin import ensure_pnxs_move_to_recycle_bin
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.files import F_USELESS_FILE_NAMES_TXT


def ensure_files_useless_gathered():
    import inspect
    import traceback

    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_historical_list import get_historical_list
    from pkg_py.functions_split.get_list_calculated import get_list_calculated
    from pkg_py.functions_split.get_list_sorted import get_list_sorted
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.system_object.directories import D_DOWNLOADS, D_PK_WORKING
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025

    try:

        func_n = inspect.currentframe().f_code.co_name
        d_working = None
        if LTA:
            key_name = "d_working"
            file_to_working = get_file_id(key_name, func_n)
            historical_pnxs = get_historical_list(f=file_to_working)
            options = historical_pnxs + get_list_sorted(working_list=[D_PK_WORKING, D_DOWNLOADS], mode_asc=1)
            d_working = get_value_completed(key_hint='d_working=', values=options)
            ensure_printed(f'''[{PkMessages2025.DATA}] len(historical_pnxs)={len(historical_pnxs)} {'%%%FOO%%%' if LTA else ''}''')
            ensure_printed(f'''[{PkMessages2025.DATA}] len(options)={len(options)} {'%%%FOO%%%' if LTA else ''}''')
            d_working = get_pnx_os_style(pnx=d_working).strip()
            values_to_save = [v for v in [d_working] + historical_pnxs + options if does_pnx_exist(pnx=v)]
            values_to_save = get_list_calculated(origin_list=values_to_save, dedup=True)
            ensure_list_written_to_f(f=file_to_working, working_list=values_to_save, mode="w")

        editable = True  # pk_option

        useless_file_names_txt = F_USELESS_FILE_NAMES_TXT
        if editable:
            ensure_pnx_opened_by_ext(pnx=useless_file_names_txt)

        dst = rf"G:\Downloads\pk_recycle_bin\pk_useless"
        ensure_pnx_made(pnx=dst, mode="d")
        ensure_printed(f'''dst={dst}  {'%%%FOO%%%' if LTA else ''}''')
        if not is_empty_d(d_src=dst):
            ensure_command_excuted_to_os(cmd=rf'explorer "{dst}" ', encoding='cp949')

        os.chdir(d_working)

        # string_clipboard_bkp=ensure_pasted()

        # useless_f_set 수집
        useless_f_set = set()

        useless_files = get_list_from_f(useless_file_names_txt)
        # open_pnx(pnx=useless_file_names_txt, debug_mode=True)
        for useless_f_nx in useless_files:
            if useless_f_nx is not None:
                useless_f_nx = useless_f_nx.strip()
                useless_f_nx = useless_f_nx.strip("\n")
                cmd = f'dir /b /s "{useless_f_nx}"'
                useless_files = ensure_command_excuted_to_os(cmd=cmd, encoding='cp949')
                if useless_files is None:
                    useless_files = []
                for uleless_f in useless_files:
                    if does_pnx_exist(pnx=uleless_f):
                        useless_f_set.add(uleless_f)

        os.chdir(D_PROJECT)
        if len(useless_f_set) == 0:
            ensure_printed(f'''len(useless_f_set)={len(useless_f_set)}  {'%%%FOO%%%' if LTA else ''}''')
            return
        else:
            for useless_f in useless_f_set:
                # move_pnx(pnx=useless_f, d_dst=dst)  # todo : fix:외장드라이브에서는 안되는듯
                ensure_pnxs_move_to_recycle_bin(pnx=useless_f)
        ensure_printed(str_working=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
