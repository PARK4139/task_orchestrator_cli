from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.etc import PK_UNDERLINE


def measure_time_to_import_module_via_time():
    modules = [
        # 기본 라이브러리
        "asyncio", "datetime", "inspect", "json", "os", "platform", "random", "re", "shutil", "string", "subprocess", "sys", "threading", "time", "traceback", "urllib", "webbrowser", "zipfile", "collections.Counter", "functools.partial", "typing.TypeVar", "typing.List", "urllib.parse.quote", "urllib.parse.urlparse", "zipfile.BadZipFile",

        # 외부 라이브러리
        "chardet", "clipboard", "cv2", "easyocr", "ipdb", "keyboard", "mutagen", "numpy as np", "pandas as pd", "psutil", "pyaudio", "pyautogui", "pygetwindow", "pyglet", "pywintypes", "requests", "selenium.webdriver as webdriver", "send2trash", "speech_recognition as sr", "tqdm", "win32con", "win32gui", "win32process", "PIL.Image", "PIL.ImageFont", "PIL.ImageDraw", "PIL.ImageFilter",
        "playwright.sync_api as sync_playwright", "bs4.BeautifulSoup", "bs4.ResultSet", "dirsync.sync", "fastapi.HTTPException", "gtts.gTTS", "moviepy.VideoFileClip", "pynput.mouse", "pytube.Playlist", "selenium.webdriver.chrome.options as Options", "selenium.webdriver.common.by as By",

        # 사용자 정의 모듈
        "legacy.CustomErrorUtil", "legacy.DataStructureUtil", "pkg_py.interface_cmd_line.ensure_printed", "pkg_py.interface_cmd_line.print_light_black", "pkg_py.interface_cmd_line.print_cyan", "pkg_py.interface_cmd_line.print_with_underline", "pkg_py.interface_cmd_line.print_red", "pkg_py.interface_cmd_line.print_magenta", "pkg_py.interface_cmd_line.print_light_white",
        "pkg_py.interface_cmd_line.ColoramaUtil", "pkg_py.interface_cmd_line.print_ment_via_colorama",
        "pkg_py.interface_cmd_line.print_success", "pkg_py.interface_cmd_line.print_light_yellow", "pkg_py.interface_cmd_line.print_yellow",
        "pkg_py.constants.USERPROFILE", "pkg_py.constants.HOSTNAME", "pkg_py.constants.PK_UNDERLINE",
        "pkg_py.constants.BLANK", "pkg_py.constants.BIGGEST_PNXS", "pkg_py.constants.SMALLEST_PNXS",
        "pkg_py.constants.PLAYING_SOUNDS", "pkg_py.constants.COUNTS_FOR_GUIDE_TO_SLEEP",
        "pkg_py.constants.[]", "pkg_py.constants.VIDEO_IDS_ALLOWED",
        "pkg_py.constants.AUDIO_IDS_ALLOWED", "pkg_py.constants.STORAGE_VIDEOES_MERGED",
        "pkg_py.constants.PROJECT_PARENTS_DIRECTORY", "pkg_py.constants.DESKTOP",
        "pkg_py.constants.DOWNLOADS", "pkg_py.constants.pkg_image_and_video_and_sound", "pkg_py.constants.PKG_DPL",
        "pkg_py.constants.PKG_CACHE_PRIVATE", "pkg_py.constants.CLASSIFYING", "pkg_py.constants.RECYCLE_BIN",
        "pkg_py.constants.LOCAL_PKG_CACHE_PRIVATE_FILE", "pkg_py.constants.SUCCESS_LOG", "pkg_py.constants.SCHECLUER_YAML", "pkg_py.constants.YT_DLP_CMD",
        "pkg_py.constants.JQ_WIN64_EXE", "pkg_py.constants.FFMPEG_EXE", "pkg_py.constants.DB_YAML",
        "pkg_py.constants.USELESS_FILE_NAMES_TXT", "pkg_py.constants.SILENT_MP3",
        "pkg_py.constants.PKG_IMAGE_AND_VIDEO_AND_SOUND_POTPLAYER64_DPL", "pkg_py.constants.PKG_VIDEO_POTPLAYER64_DPL",
        "pkg_py.constants.MERGED_EXCEL_FILE", "pkg_py.constants.PROJECT_D",
        "pkg_py.constants.YES", "pkg_py.constants.NO", "pkg_py.constants.NOT_PREPARED_YET",
        "pkg_py.gui.GuiUtil", "pkg_py.gui.get_display_info", "times.get_time_as_"
    ]
    import time
    test_result_list = []
    for module in modules:
        start_time = time.time()
        try:
            exec(f"import {module}")
            test_result_list.append(f"in {time.time() - start_time:.4f} seconds  {module:60s} imported")
        except Exception as e:
            test_result_list.append(f"in {time.time() - start_time:.4f} seconds  {module:60s} FAILED ({e})")

    test_result_list = sorted(test_result_list)
    print("\n".join(test_result_list))


def function_to_test():
    pass



def ensure_seconds_measured_to_exec_function_via_time():
    import time
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    ensure_printed(str_working=rf'''{PK_UNDERLINE}{func_n}() s %%%FOO%%%''', print_color='blue')
    debug_mode = True
    total_start = time.time()
    try:
        start = time.time()
        function_to_test()
        print(f"function_to_test() took {time.time() - start:.2f} seconds")
    except Exception as e:
        print(f"Exception occurred: {e}")
    print(f"Total execution time: {time.time() - total_start:.2f} seconds")
    ensure_printed(str_working=rf'''{PK_UNDERLINE}{func_n}() e %%%FOO%%%''', print_color='blue')




if __name__ == '__main__':
    debug_mode = True
    try:
        # todo
        # ipdb.set_trace()
        measure_time_to_import_module_via_time()
    except Exception as e:
        # debug
        import ipdb

        ipdb.set_trace()
