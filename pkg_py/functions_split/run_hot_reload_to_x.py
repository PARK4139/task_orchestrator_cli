from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.system_object.directories import D_DOWNLOADS
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def run_hot_reload_to_x():
    # make
    # make_version_new(via_f_txt=True, debug_mode=True)

    # define
    dst = rf"{D_DOWNLOADS}\[]\[Moozzi2] Eighty-Six [ 4K Ver. ] - TV"
    dst = get_pnx_unix_style(pnx=dst)
    src = rf"{dst}\pk_system_organize_video_seg_and_image_here.cmd"
    pnx_new = get_pnx_new(d_working=dst, pnx=src)
    pnx_new = get_pnx_windows_style(pnx=pnx_new)

    # del
    if does_pnx_exist(pnx=pnx_new):
        cmd_to_os(cmd=rf'echo y | del /f "{pnx_new}"')
        # ensure_slept(milliseconds=500)

    # copy
    copy_pnx_with_overwrite(pnx=src, dst=dst)

    # cd
    pk_chdir(dst)

    # call
    try:
        cmd_to_os(cmd=rf'call "{pnx_new}"', mode='a')  # todo : ?
        # lines=cmd_to_os_v_1_0_1(cmd=rf'call "{pnx_new}/"')
        # cmd_to_os_like_person(cmd=rf'"{pnx_new}"')
    except:
        pass
