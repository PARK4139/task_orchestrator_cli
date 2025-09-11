from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE

import logging
from sources.objects.pk_map_texts import PkTexts


def convert_mp3_to_flac(f_mp3):
    import inspect
    import os
    import subprocess

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    '''테스트 필요'''
    os.system("chcp 65001 >NUL")

    logging.debug(f'f_mp3 : {f_mp3}')
    f_edited = f'{os.path.splitext(os.path.basename(f_mp3))[0]}.flac'
    logging.debug(f'f_edited   : {f_edited}')

    d_started = os.getcwd()

    ffmpeg_exe = F_FFMPEG_EXE
    d_dst = 'storage'
    try:
        os.makedirs(d_dst)
    except Exception as e:
        pass
    os.chdir(d_dst)
    logging.debug(f'"{ffmpeg_exe}" -i "{f_mp3}" -c:a flac "{f_edited}"        {PkTexts.PERFORMING_OPERATION}.')
    subprocess.check_output(f'"{ffmpeg_exe}" -i "{f_mp3}" -c:a flac "{f_edited}"', shell=True)

    os.chdir(d_started)
