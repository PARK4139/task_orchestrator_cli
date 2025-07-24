from pkg_py.system_object.files import F_FFMPEG_EXE

from pkg_py.functions_split.pk_print import pk_print


def convert_mp4_to_flac(pnx):
    import inspect
    import os
    import subprocess

    func_n = inspect.currentframe().f_code.co_name

    '''테스트 필요'''

    os.system("chcp 65001 >nul")
    pk_print(f'from : {pnx}', print_color='blue')
    file_edited = f'{os.path.splitext(os.path.basename(pnx))[0]}.flac'
    pk_print(f'to   : {file_edited}', print_color='blue')

    path_started = os.getcwd()

    ffmpeg_exe = F_FFMPEG_EXE
    destination = 'storage'
    try:
        os.makedirs(destination)
    except Exception as e:
        pass
    pk_chdir(destination)
    pk_print(f'"{ffmpeg_exe}" -i "{pnx}" -c:a flac "{file_edited}"        를 수행합니다.', print_color='blue')
    subprocess.check_output(f'"{ffmpeg_exe}" -i "{pnx}" -c:a flac "{file_edited}"', shell=True)

    pk_chdir(path_started)
