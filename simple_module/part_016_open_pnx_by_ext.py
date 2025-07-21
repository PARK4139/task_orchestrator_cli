

def ensure_pnx_opened_by_ext(pnx):
    from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
    from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
    from pkg_py.simple_module.part_014_pk_print import pk_print
    from pkg_py.simple_module.part_151_get_os_n import get_os_n

    # TBD : tab 으로 뭘로 열지 설정하도록 ?

    import os
    # x = get_x(pnx).replace('.', '')
    x = os.path.splitext(pnx)[1].lower().replace('.', '')
    text_editor = None
    ext_to_program = None
    if get_os_n() == 'windows':
        # ext_to_program = get_value_completed(message="ext_to_program=", option_values=['xc', 'nx', 'no'])
        ext_to_program = {
            '': ('explorer.exe', 'directory, opening in explorer'),
            'txt': ('explorer.exe', 'text file, opening in explorer'),
            'csv': ('explorer.exe', 'csv file, opening in excel'),
            'xlsx': ('explorer.exe', 'excel file, opening in excel'),
            'xlsm': ('explorer.exe', 'excel file, opening in excel'),
            'xls': ('explorer.exe', 'excel file, opening in excel'),

            # Video files
            'mp4': ('explorer.exe', 'video file, opening in default player'),
            'avi': ('explorer.exe', 'video file, opening in default player'),
            'mkv': ('explorer.exe', 'video file, opening in default player'),
            'mov': ('explorer.exe', 'video file, opening in default player'),
            'wmv': ('explorer.exe', 'video file, opening in default player'),
            'flv': ('explorer.exe', 'video file, opening in default player'),
            'webm': ('explorer.exe', 'video file, opening in default player'),
        }
    program, description = ext_to_program.get(x, (None, None))
    if program:
        text_editor = program
        pnx = get_pnx_windows_style(pnx=pnx)
        pk_print(f"open_pnx_by_ext: {pnx} is a {description}", print_color='blue')
    cmd = f'{text_editor} "{pnx}" '
    cmd_to_os(cmd=cmd, mode='a')
    # else:
    #     if x == '':  # d 인 경우
    #         text_editor = 'explorer.exe'
    #     elif x == 'txt':
    #         text_editor = 'gedit' # nvim, nano, vim, code
    #     # elif x == 'csv':
    #     #     text_editor = 'explorer.exe'
    #     # elif x == 'xlsx':
    #     #     text_editor = 'explorer.exe'
    #     # elif x == 'xls':
    #     #     text_editor = 'explorer.exe'
    #     pnx = get_pnx_unix_style(pnx=pnx)
