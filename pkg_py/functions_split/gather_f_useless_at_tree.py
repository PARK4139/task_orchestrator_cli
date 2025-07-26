from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.directories_reuseable import D_PROJECT

from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def gather_f_useless_at_tree(d_working):
    import traceback

    dst = rf"D:\[]\[useless]"
    ensure_pnx_made(pnx=dst, mode="d")
    ensure_printed(f'''dst={dst}  {'%%%FOO%%%' if LTA else ''}''')
    if not is_empty_d(d_src=dst):
        ensure_command_excuted_to_os(cmd=rf'explorer "{dst}" ', encoding='cp949')
    try:
        pk_chdir(d_dst=d_working)

        # string_clipboard_bkp=pk_paste()

        # useless_f_set 수집
        useless_f_set = set()
        is_target_moved_done = False
        useless_file_names_txt = F_USELESS_FILE_NAMES_TXT
        uleless_f_list = get_list_from_f(useless_file_names_txt)
        # open_pnx(pnx=useless_file_names_txt, debug_mode=True)
        for useless_f_nx in uleless_f_list:
            if useless_f_nx is not None:
                useless_f_nx = useless_f_nx.strip()
                useless_f_nx = useless_f_nx.strip("\n")
                cmd = f'dir /b /s "{useless_f_nx}"'
                uleless_f_list = ensure_command_excuted_to_os(cmd=cmd, encoding='cp949')
                if uleless_f_list is None:
                    uleless_f_list = []
                for uleless_f in uleless_f_list:
                    if does_pnx_exist(pnx=uleless_f):
                        useless_f_set.add(uleless_f)

        pk_chdir(D_PROJECT)

        if len(useless_f_set) == 0:
            ensure_printed(f'''len(useless_f_set)={len(useless_f_set)}  {'%%%FOO%%%' if LTA else ''}''')
            return
        else:
            for useless_f in useless_f_set:
                move_pnx(pnx=useless_f, d_dst=dst)  # todo : fix:외장드라이브에서는 안되는듯
                # move_pnx_to_trash_bin(src=useless_f)
        ensure_printed(str_working=rf'''dst="{dst}"  {'%%%FOO%%%' if LTA else ''}''', print_color='green')
    except:
        ensure_printed(f"{traceback.format_exc()}", print_color='red')
