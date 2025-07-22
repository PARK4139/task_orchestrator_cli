from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style


def cmd_f_in_cmd_exe_like_person(cmd_prefix, f):
    # make
    # make_version_new(via_f_txt=True, debug_mode=True)

    # src
    f = get_pnx_unix_style(pnx=f)

    dst = get_p(f)
    dst = get_pnx_unix_style(pnx=dst)

    # pnx_new
    pnx_new = get_pnx_new(d_working=dst, pnx=f)
    pnx_new = get_pnx_windows_style(pnx=pnx_new)

    # kill
    # kill_process_via_taskkill(process_name='cmd.exe')
    # kill_process_via_wmic(process_img_n='cmd.exe')
    window_title_seg = f
    window_title_seg = get_pnx_windows_style(window_title_seg)
    kill_window_like_person(window_title_seg=window_title_seg)

    # run
    try:
        cmd_to_os_like_person(cmd=rf'"{D_PROJECT}\.venv\Scripts\activate.cmd"')
        cmd_to_os_like_person(cmd=rf'{cmd_prefix} "{pnx_new}"')
    except:
        pass

    # move (to pycharm64.exe)
    ensure_window_to_front_of_pycharm()
