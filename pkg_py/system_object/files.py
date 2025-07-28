import os

from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_time_as_ import get_time_as_
from pkg_py.functions_split.is_office_pc import is_office_pc
from pkg_py.system_object.directories import D_PKG_TXT, D_PKG_JSON, D_DOWNLOADS, D_PKG_PK, D_PKG_TOML, D_PKG_WINDOWS, \
    D_PKG_DB, D_DESKTOP, D_PKG_PY, D_PK_RECYCLE_BIN, D_PKG_WINDOWS, D_PK_FUNCTIONS_SPLIT
from pkg_py.system_object.directories_reuseable import D_PROJECT, D_HOME

F_VPC_MAMNAGEMENT_MAP_TOML = f'{D_PKG_TOML}/vpc_mamnagement_map.toml'
F_ALIAS_CMD = rf'{D_PKG_WINDOWS}/ensure_alias_enabled.cmd'
F_CONFIG_TOML = rf'{D_PROJECT}/pkg_toml/pk_config.toml'
F_VIDEO_LIST_ALLOWED_TO_LOAD_TXT = rf'{D_PKG_TXT}/f_videos_allowed_to_load.txt'
F_LOCAL_PKG_CACHE = rf'{D_PROJECT}/pkg_alba/__pycache__/__init__.cpython-312.pyc'
F_MEMO_TRASH_BIN_TOML = rf'{D_PKG_TOML}/memo_trash_bin.toml'
F_MEMO_WORK_PK = rf"{D_PKG_PK}/pk_memo_working.pk"
F_MEMO_HOW_PK = rf"{D_PKG_PK}/pk_memo_how.pk"
F_ICON_PNG = rf"{D_PROJECT}/pkg_png/icon.PNG"
F_LOSSLESSCUT_EXE = rf"{D_DOWNLOADS}/pk_archived/LosslessCut-win-x64/LosslessCut.exe"
F_FFMPEG_EXE = rf"{D_DOWNLOADS}/pk_archived/LosslessCut-win-x64/resources/ffmpeg.exe"
# F_FFMPEG_EXE = rf"{D_PKG_WINDOWS}/ffmpeg.exe"
F_SUCCESS_LOG = rf'{D_PROJECT}/pkg_log/success.log'
F_MACRO_LOG = rf'{D_PROJECT}/pkg_log/macro.log'
# DIRSYNC_LOG = rf'{PROJECT_D}/pkg_log/dirsync.log'
# YT_DLP_CMD = rf"{PROJECT_D}/pkg_yt_dlp/yt-dlp.cmd" # 2023.11.15 구버전
F_YT_DLP_EXE = rf"{D_PROJECT}/pkg_yt_dlp/yt-dlp.exe"  # 2024.04.09 신버전
F_JQ_WIN64_EXE = rf"{D_PROJECT}/pkg_jq/jq-win64.exe"
F_DB_YAML = rf"{D_PROJECT}/pkg_yaml/db.yaml"
F_USELESS_FILE_NAMES_TXT = rf"{D_PKG_TXT}/useless_file_names.txt"
F_SILENT_MP3 = rf"{D_PROJECT}/pkg_sound/silent.mp3"
F_POP_SOUND_POP_SOUND_WAV = rf"{D_PROJECT}/pkg_sound/pop_sound.wav"
F_PK_DB = rf'{D_PKG_DB}/pk.db'
F_PKG_SOUND_POTPLAYER64_DPL = rf"{D_PROJECT}/pkg_sound/PotPlayer64.dpl"
F_PKG_VIDEO_POTPLAYER64_DPL = rf"{D_PROJECT}/pkg_video/PotPlayer64.dpl"
F_DB_JSON = rf"{D_PKG_JSON}/db.json"
F_BOOKS_JSON = rf"{D_PKG_JSON}/books.json"
F_USERS_JSON = rf"{D_PKG_JSON}/users.json"
F_NAV_ITEMS_JSON = rf"{D_PKG_JSON}/nav_items.json"
F_MERGED_EXCEL_FILE = rf'{D_PROJECT}/pkg_xls/merged/머지결과물.xlsx'
F_MONTSERRAT_THIN_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Thin.ttf"
F_NOTOSANSKR_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_font/Noto_Sans_KR/NotoSansKR-VariableFont_wght.ttf"
F_NOTOSANSKR_BLACK_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Black.ttf"
F_NOTOSANSKR_BOLD_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Bold.ttf"
F_NOTOSANSKR_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-ExtraBold.ttf"
F_NOTOSANSKR_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-ExtraLight.ttf"
F_NOTOSANSKR_LIGHT_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Light.ttf"
F_NOTOSANSKR_MEDIUM_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Medium.ttf"
F_NOTOSANSKR_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Regular.ttf"
F_NOTOSANSKR_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-SemiBold.ttf"
F_NOTOSANSKR_THIN_TTF = rf"{D_PROJECT}/pkg_font/NotoSansKR-Thin.ttf"
F_GMARKETSANSTTFBOLD_TTF = rf"{D_PROJECT}/pkg_font/GmarketSansTTFBold.ttf"
F_GMARKETSANSTTFLIGHT_TTF = rf"{D_PROJECT}/pkg_font/GmarketSansTTFLight.ttf"
F_GMARKETSANSTTFMEDIUM_TTF = rf"{D_PROJECT}/pkg_font/GmarketSansTTFMedium.ttf"
F_ITALIC_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat/Montserrat-Italic-VariableFont_wght.ttf"
F_MONTSERRAT_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat/Montserrat-VariableFont_wght.ttf"
F_MONTSERRAT_BLACK_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Black.ttf"
F_MONTSERRAT_BLACKITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-BlackItalic.ttf"
F_MONTSERRAT_BOLD_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Bold.ttf"
F_MONTSERRAT_BOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-BoldItalic.ttf"
F_MONTSERRAT_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraBold.ttf"
F_MONTSERRAT_EXTRABOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraBoldItalic.ttf"
F_MONTSERRAT_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraLight.ttf"
F_MONTSERRAT_EXTRALIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ExtraLightItalic.ttf"
F_MONTSERRAT_ITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Italic.ttf"
F_MONTSERRAT_LIGHT_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Light.ttf"
F_MONTSERRAT_LIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-LightItalic.ttf"
F_MONTSERRAT_MEDIUM_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Medium.ttf"
F_MONTSERRAT_MEDIUMITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-MediumItalic.ttf"
F_MONTSERRAT_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-Regular.ttf"
F_MONTSERRAT_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-SemiBold.ttf"
F_MONTSERRAT_SEMIBOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-SemiBoldItalic.ttf"
F_MONTSERRAT_THINITALIC_TTF = rf"{D_PROJECT}/pkg_font/Montserrat-ThinItalic.ttf"
F_POPPINS_BLACK_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Black.ttf"
F_POPPINS_BLACKITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-BlackItalic.ttf"
F_POPPINS_BOLD_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Bold.ttf"
F_POPPINS_BOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-BoldItalic.ttf"
F_POPPINS_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraBold.ttf"
F_POPPINS_EXTRABOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraBoldItalic.ttf"
F_POPPINS_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraLight.ttf"
F_POPPINS_EXTRALIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ExtraLightItalic.ttf"
F_POPPINS_ITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Italic.ttf"
F_POPPINS_LIGHT_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Light.ttf"
F_POPPINS_LIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-LightItalic.ttf"
F_POPPINS_MEDIUM_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Medium.ttf"
F_POPPINS_MEDIUMITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-MediumItalic.ttf"
F_POPPINS_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Regular.ttf"
F_POPPINS_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_font/Poppins-SemiBold.ttf"
F_POPPINS_SEMIBOLDITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-SemiBoldItalic.ttf"
F_POPPINS_THIN_TTF = rf"{D_PROJECT}/pkg_font/Poppins-Thin.ttf"
F_POPPINS_THINITALIC_TTF = rf"{D_PROJECT}/pkg_font/Poppins-ThinItalic.ttf"
F_RUBIKDOODLESHADOW_REGULAR_TTF = rf"{D_PROJECT}/pkg_font/RubikDoodleShadow-Regular.ttf"  # 너무 귀여운 입체감 있는 영어폰트
F_HISTORICAL_PNX = rf'{D_PKG_TXT}/historical_pnx.txt'
F_HISTORICAL_SEARCH_KEYWORD = rf'{D_PKG_TXT}/historical_search_keyword.txt'
F_POT_PLAYER_MINI_64_EXE = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
F_TEMP_LOG = rf"{D_DESKTOP}/pk_temp_via_{get_nx(__file__)}_{get_time_as_("now")}.log"
F_TEST_PY = rf"{D_PKG_PY}/pk_test.py"
F_PK_WORKSPACE_PY = get_pnx_os_style(rf"{D_PKG_PY}/workspace/pk_workspace.py")
F_UV_ZIP = rf"{D_DOWNLOADS}\uv.zip"
F_UV_EXE = rf"{D_PKG_WINDOWS}\uv.exe"
F_YOUTUBE_COOKIES_TXT = rf"{D_PKG_TXT}/youtube_cookies.txt"
F_PK_ALIAS_MACROS_TXT = rf"{D_PKG_TXT}\pk_alias_macros.txt"
F_PK_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY=rf"{D_PK_FUNCTIONS_SPLIT}/test_pk_python_program_structure.py"

F_PYCHARM64_EDITION_EXE = rf"C:/Program Files/JetBrains/PyCharm Community Edition 2025.1.3.1/bin/pycharm64.exe"
if is_office_pc():
    F_PYCHARM64_EDITION_EXE = rf"C:/Program Files/JetBrains/PyCharm Community Edition 2024.2.4/bin/pycharm64.exe"
    # F_PYCHARM64_EDITION_EXE = r"C:/Program Files/JetBrains/PyCharm Community Edition 2024.3.1/bin/pycharm64.exe"
F_CURSOR_EXE = rf"{D_HOME}\AppData\Local\Programs\cursor\Cursor.exe"
