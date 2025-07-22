from pkg_py.pk_system_object.files import F_FFMPEG_EXE

from pkg_py.functions_split.pk_print import pk_print


def convert_mp3_to_flac(f_mp3):
    import inspect
    import os
    import subprocess

    func_n = inspect.currentframe().f_code.co_name
    '''테스트 필요'''
    os.system("chcp 65001 >nul")

    pk_print(f'f_mp3 : {f_mp3}', print_color='blue')
    f_edited = f'{os.path.splitext(os.path.basename(f_mp3))[0]}.flac'
    pk_print(f'f_edited   : {f_edited}', print_color='blue')

    d_started = os.getcwd()

    ffmpeg_exe = F_FFMPEG_EXE
    d_dst = 'storage'
    try:
        os.makedirs(d_dst)
    except Exception as e:
        pass
    pk_chdir(d_dst)
    pk_print(f'"{ffmpeg_exe}" -i "{f_mp3}" -c:a flac "{f_edited}"        를 수행합니다.', print_color='blue')
    subprocess.check_output(f'"{ffmpeg_exe}" -i "{f_mp3}" -c:a flac "{f_edited}"', shell=True)

    pk_chdir(d_started)
