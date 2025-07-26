from tkinter import UNDERLINE

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.ensure_printed import ensure_printed


def update_global_pkg_alba():
    import inspect
    import os
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    local_pkg = rf"{D_PROJECT}\pkg_alba"
    global_pkg = rf"C:\Python312\Lib\site-packages\pkg_alba"
    updateignore_txt = rf"{D_PROJECT}\pkg_alba\updateignore.txt"
    try:
        if os.path.exists(global_pkg):
            # remove시도
            # shutil.rmtree(global_pkg)

            # remove시도
            # for file in os.scandir(global_pkg):
            # os.remove(file.path)

            # 덮어쓰기
            # src= local_pkg
            # dst =os.path.dirname(global_pkg)
            # os.system(f"echo y | copy {src} {dst}")
            # shutil.copytree(local_pkg, os.path.dirname(global_pkg))
            cmd = f'echo y | xcopy "{local_pkg}" "{global_pkg}" /k /e /h /exclude:{updateignore_txt} >nul'
            os.system(cmd)

            ensure_printed(f'{cmd}', print_color='blue')
            ensure_printed(f"{UNDERLINE}", print_color='blue')
            return "REPLACED global pkg_alba AS local_pkg"
        else:
            return "pkg_alba NOT FOUND AT GLOBAL LOCATION"

    except Exception as e:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
