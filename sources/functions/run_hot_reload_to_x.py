from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.does_pnx_exist import is_pnx_existing


def run_hot_reload_to_x():
    # make
    # make_version_new(via_f_txt=True, debug_mode=True)

    # define
    dst = rf"{D_DOWNLOADS}\[]\[Moozzi2] Eighty-Six [ 4K Ver. ] - TV"
    dst = get_pnx_unix_style(pnx=dst)
    src = rf"{dst}\task_orchestrator_cli_organize_video_seg_and_image_here.cmd"
    pnx_new = get_pnx_new(d_working=dst, pnx=src)
    pnx_new = get_pnx_windows_style(pnx=pnx_new)

    # del
    if is_pnx_existing(pnx=pnx_new):
        ensure_command_executed(cmd=rf'echo y | del /f "{pnx_new}"')
        # ensure_slept(milliseconds=500)

    # copy
    copy_pnx_with_overwrite(pnx=src, dst=dst)

    # cd
    os.chdir(dst)

    # call
    try:
        ensure_command_executed(cmd=rf'call "{pnx_new}"', mode='a')  # todo : ?
        # lines=ensure_command_executed_v_1_0_1(cmd=rf'call "{pnx_new}/"')
        # ensure_command_executed_like_human(cmd=rf'"{pnx_new}"')
    except:
        pass
