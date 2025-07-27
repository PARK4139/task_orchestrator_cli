from pkg_py.system_object.files import F_FFMPEG_EXE

from pkg_py.functions_split.ensure_printed import ensure_printed


def convert_mp4_to_flac(pnx):
    import inspect
    import os
    import subprocess

    func_n = inspect.currentframe().f_code.co_name

    '''테스트 필요'''

    os.system("chcp 65001 >nul")
    ensure_printed(f'from : {pnx}', print_color='blue')
    file_edited = f'{os.path.splitext(os.path.basename(pnx))[0]}.flac'
    ensure_printed(f'to   : {file_edited}', print_color='blue')

    path_started = os.getcwd()

    ffmpeg_exe = F_FFMPEG_EXE
    destination = 'storage'
    try:
        os.makedirs(destination)
    except Exception as e:
        pass
    os.chdir(destination)
    ensure_printed(f'"{ffmpeg_exe}" -i "{pnx}" -c:a flac "{file_edited}"        를 수행합니다.', print_color='blue')
    subprocess.check_output(f'"{ffmpeg_exe}" -i "{pnx}" -c:a flac "{file_edited}"', shell=True)

    os.chdir(path_started)
