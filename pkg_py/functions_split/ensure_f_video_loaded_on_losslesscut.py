def ensure_f_video_loaded_on_losslesscut(f_video):
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
    from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
    from pkg_py.system_object.local_test_activate import LTA
    F_LOSSLESSCUT_EXE = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    f_video = get_pnx_windows_style(pnx=f_video)
    if f_video is not None:
        if does_pnx_exist(f_video):
            ensure_command_excuted_to_os(cmd=rf'''start "" /MAX "{F_LOSSLESSCUT_EXE}" "{f_video}"''')
    else:
        ensure_printed(f'''f_video is None {'%%%FOO%%%' if LTA else ''}''')
