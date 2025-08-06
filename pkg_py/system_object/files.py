from pkg_py.functions_split import get_time_as_
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.directories import D_PROJECT, D_HOME, D_PKG_CACHE_PRIVATE, D_PKG_JSON, D_DOWNLOADS, D_PKG_PK, D_PKG_TOML, D_PKG_DB, D_PKG_PY, D_PKG_WINDOWS, D_PK_FUNCTIONS_SPLIT, D_PKG_LOG, ensure_pnx_normalized_this_file

F_VPC_MAMNAGEMENT_MAP_TOML = f'{D_PKG_TOML}/vpc_mamnagement_map.toml'
F_CONFIG_TOML = rf'{D_PROJECT}/pkg_toml/pk_config.toml'
F_PYPROJECT_TOML = rf'{D_PROJECT}/pyproject.toml'
F_VIDEO_LIST_ALLOWED_TO_LOAD_TXT = rf'{D_PKG_CACHE_PRIVATE}/f_videos_allowed_to_load.txt'
F_LOCAL_PKG_CACHE_PRIVATE = rf'{D_PROJECT}/pkg_alba/__pycache__/__init__.cpython-312.pyc'
F_MEMO_TRASH_BIN_TOML = rf'{D_PKG_TOML}/memo_trash_bin.toml'
F_MEMO_WORK_PK = rf"{D_PKG_PK}/pk_memo_working.pk"
F_MEMO_HOW_PK = rf"{D_PKG_PK}/pk_memo_how.pk"
F_ICON_PNG = rf"{D_PROJECT}/pkg_image_and_video_and_sound/icon.PNG"
F_FZF_EXE = rf"{D_PKG_WINDOWS}/fzf.exe"
F_LOSSLESSCUT_EXE = None
F_FFMPEG_EXE = None
F_YT_DLP_EXE = None
F_JQ_WIN64_EXE = None
F_POT_PLAYER_MINI_64_EXE = None
F_EVERYTHING_EXE = None
F_SNIPPING_TOOL_EXE = None
F_BIT_TORRENT_EXE = None
F_CURSOR_EXE = None
F_CLAUDE_EXE = None
F_UV_EXE = None
F_UV_ZIP = None
F_FZF_ZIP = None
F_ENSURE_PK_SYSTEM_ENABLED_CMD = None
F_PYCHARM64_EDITION_EXE = None
F_VSCODE_EXE = None
# OS별 실행 파일 경로 설정
if is_os_windows():
    F_LOSSLESSCUT_EXE = rf"{D_DOWNLOADS}/pk_archived/LosslessCut-win-x64/LosslessCut.exe"
    F_FFMPEG_EXE = rf"{D_DOWNLOADS}/pk_archived/LosslessCut-win-x64/resources/ffmpeg.exe"
    F_YT_DLP_EXE = rf"{D_PROJECT}/pkg_windows/yt-dlp.exe"
    F_JQ_WIN64_EXE = rf"{D_PROJECT}/pkg_windows/jq-win64.exe"
    F_POT_PLAYER_MINI_64_EXE = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
    F_EVERYTHING_EXE = rf"C:\Program Files\Everything\Everything.exe"
    F_SNIPPING_TOOL_EXE = rf"C:\Program Files\WindowsApps\Microsoft.ScreenSketch_11.2506.25.0_x64__8wekyb3d8bbwe\SnippingTool\SnippingTool.exe"
    F_BIT_TORRENT_EXE = rf"C:\Users\wjdgn\AppData\Roaming\bittorrent\bit_torrent.exe"
    F_CURSOR_EXE = rf"{D_HOME}\AppData\Local\Programs\cursor\Cursor.exe"
    F_CLAUDE_EXE = rf"{D_HOME}\AppData\Local\AnthropicClaude\claude.exe"
    F_UV_EXE = rf"{D_PKG_WINDOWS}\uv.exe"
    F_FZF_ZIP = rf"{D_DOWNLOADS}\fzf.zip"
    F_ENSURE_PK_SYSTEM_ENABLED_CMD = f'{D_PKG_WINDOWS}/ensure_pk_system_enabled.cmd'
    F_PYCHARM64_EDITION_EXE = rf"C:/Program Files/JetBrains/PyCharm Community Edition 2025.1.3.1/bin/pycharm64.exe"
    F_VSCODE_EXE = f"{D_HOME}\AppData\Local\Programs\Microsoft VS Code\Code.exe"
else:
    # Linux 환경용 경로
    F_LOSSLESSCUT_EXE = rf"{D_DOWNLOADS}/pk_archived/LosslessCut-linux-x64/LosslessCut"
    F_FFMPEG_EXE = "ffmpeg"  # 시스템에 설치된 ffmpeg 사용
    F_YT_DLP_EXE = "yt-dlp"  # 시스템에 설치된 yt-dlp 사용
    F_JQ_WIN64_EXE = "jq"  # 시스템에 설치된 jq 사용
    F_POT_PLAYER_MINI_64_EXE = None  # Linux에서는 PotPlayer 사용 불가
    F_EVERYTHING_EXE = None  # Linux에서는 Everything 사용 불가
    F_SNIPPING_TOOL_EXE = "gnome-screenshot"  # Linux 스크린샷 도구
    F_BIT_TORRENT_EXE = "transmission-gtk"  # Linux 토렌트 클라이언트
    F_CURSOR_EXE = "cursor"  # Linux Cursor 실행 파일
    F_CLAUDE_EXE = rf"claude"
    F_UV_EXE = "uv"  # 시스템에 설치된 uv 사용
    F_UV_ZIP = None  # Linux에서는 zip 파일 불필요
    F_FZF_ZIP = None
    F_ENSURE_PK_SYSTEM_ENABLED_CMD = f'{D_PKG_WINDOWS}/ensure_pk_system_enabled.sh'
    F_PYCHARM64_EDITION_EXE = "pycharm-community"  # 시스템 PATH에 있는 경우
    F_VSCODE_EXE = f"code"

# 공통 파일들
F_WORKING = rf"{D_PROJECT}/tests/pk_working.py"
F_SUCCESS_LOG = rf'{D_PROJECT}/pkg_log/success.log'
F_MACRO_LOG = rf'{D_PROJECT}/pkg_log/macro.log'
F_DB_YAML = rf"{D_PROJECT}/pkg_cache_private/db.yaml"
F_USELESS_FILE_NAMES_TXT = rf"{D_PKG_CACHE_PRIVATE}/useless_file_names.txt"
F_SILENT_MP3 = rf"{D_PROJECT}/pkg_image_and_video_and_sound/silent.mp3"
F_POP_SOUND_POP_SOUND_WAV = rf"{D_PROJECT}/pkg_image_and_video_and_sound/pop_sound.wav"
F_PK_SYSTEM_SQLITE = rf'{D_PKG_DB}/pk_system.sqlite'
F_PKG_IMAGE_AND_VIDEO_AND_SOUND_POTPLAYER64_DPL = rf"{D_PROJECT}/pkg_image_and_video_and_sound/PotPlayer64.dpl"
F_PKG_VIDEO_POTPLAYER64_DPL = rf"{D_PROJECT}/pkg_video/PotPlayer64.dpl"
F_DB_JSON = rf"{D_PKG_JSON}/db.json"
F_BOOKS_JSON = rf"{D_PKG_JSON}/books.json"
F_USERS_JSON = rf"{D_PKG_JSON}/users.json"
F_NAV_ITEMS_JSON = rf"{D_PKG_JSON}/nav_items.json"
F_MERGED_EXCEL_FILE = rf'{D_PROJECT}/pkg_xls/merged/merged.xlsx'
F_HISTORICAL_PNX = rf'{D_PKG_CACHE_PRIVATE}/historical_pnx.txt'
F_HISTORICAL_SEARCH_KEYWORD = rf'{D_PKG_CACHE_PRIVATE}/historical_search_keyword.txt'
F_TEMP_LOG = rf"{D_PKG_LOG}/pk_temp_via_{get_nx(__file__)}_{get_time_as_("now")}.log"
F_TEST_PY = rf"{D_PKG_PY}/pk_test.py"
F_YOUTUBE_COOKIES_TXT = rf"{D_PKG_CACHE_PRIVATE}/youtube_cookies.txt"
F_PK_ALIAS_MACROS_TXT = rf"{D_PKG_CACHE_PRIVATE}/pk_alias_macros.txt"
F_TEST_PK_PYTHON_PROGRAM_STRUCTURE_PY = rf"{D_PK_FUNCTIONS_SPLIT}/test_pk_system_process_structure.py"

# 폰트 파일들 (공통)
F_MONTSERRAT_THIN_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-Thin.ttf"
F_NOTOSANSKR_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Noto_Sans_KR/NotoSansKR-VariableFont_wght.ttf"
F_NOTOSANSKR_BLACK_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-Black.ttf"
F_NOTOSANSKR_BOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-Bold.ttf"
F_NOTOSANSKR_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-ExtraBold.ttf"
F_NOTOSANSKR_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-ExtraLight.ttf"
F_NOTOSANSKR_LIGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-Light.ttf"
F_NOTOSANSKR_MEDIUM_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-Medium.ttf"
F_NOTOSANSKR_REGULAR_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-Regular.ttf"
F_NOTOSANSKR_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-SemiBold.ttf"
F_NOTOSANSKR_THIN_TTF = rf"{D_PROJECT}/pkg_cache_private_public/NotoSansKR-Thin.ttf"
F_GMARKETSANSTTFBOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/GmarketSansTTFBold.ttf"
F_GMARKETSANSTTFLIGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/GmarketSansTTFLight.ttf"
F_GMARKETSANSTTFMEDIUM_TTF = rf"{D_PROJECT}/pkg_cache_private_public/GmarketSansTTFMedium.ttf"
F_ITALIC_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat/Montserrat-Italic-VariableFont_wght.ttf"
F_MONTSERRAT_VARIABLEFONT_WGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat/Montserrat-VariableFont_wght.ttf"
F_MONTSERRAT_BLACK_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-Black.ttf"
F_MONTSERRAT_BLACKITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-BlackItalic.ttf"
F_MONTSERRAT_BOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-Bold.ttf"
F_MONTSERRAT_BOLDITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-BoldItalic.ttf"
F_MONTSERRAT_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-ExtraBold.ttf"
F_MONTSERRAT_EXTRABOLDITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-ExtraBoldItalic.ttf"
F_MONTSERRAT_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-ExtraLight.ttf"
F_MONTSERRAT_EXTRALIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-ExtraLightItalic.ttf"
F_MONTSERRAT_ITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-Italic.ttf"
F_MONTSERRAT_LIGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-Light.ttf"
F_MONTSERRAT_LIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-LightItalic.ttf"
F_MONTSERRAT_MEDIUM_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-Medium.ttf"
F_MONTSERRAT_MEDIUMITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-MediumItalic.ttf"
F_MONTSERRAT_REGULAR_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-Regular.ttf"
F_MONTSERRAT_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-SemiBold.ttf"
F_MONTSERRAT_SEMIBOLDITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-SemiBoldItalic.ttf"
F_MONTSERRAT_THINITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Montserrat-ThinItalic.ttf"
F_POPPINS_BLACK_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-Black.ttf"
F_POPPINS_BLACKITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-BlackItalic.ttf"
F_POPPINS_BOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-Bold.ttf"
F_POPPINS_BOLDITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-BoldItalic.ttf"
F_POPPINS_EXTRABOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-ExtraBold.ttf"
F_POPPINS_EXTRABOLDITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-ExtraBoldItalic.ttf"
F_POPPINS_EXTRALIGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-ExtraLight.ttf"
F_POPPINS_EXTRALIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-ExtraLightItalic.ttf"
F_POPPINS_ITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-Italic.ttf"
F_POPPINS_LIGHT_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-Light.ttf"
F_POPPINS_LIGHTITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-LightItalic.ttf"
F_POPPINS_MEDIUM_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-Medium.ttf"
F_POPPINS_MEDIUMITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-MediumItalic.ttf"
F_POPPINS_REGULAR_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-Regular.ttf"
F_POPPINS_SEMIBOLD_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-SemiBold.ttf"
F_POPPINS_SEMIBOLDITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-SemiBoldItalic.ttf"
F_POPPINS_THIN_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-Thin.ttf"
F_POPPINS_THINITALIC_TTF = rf"{D_PROJECT}/pkg_cache_private_public/Poppins-ThinItalic.ttf"
F_RUBIKDOODLESHADOW_REGULAR_TTF = rf"{D_PROJECT}/pkg_cache_private_public/RubikDoodleShadow-Regular.ttf"  # 너무 귀여운 입체감 있는 영어 폰트

ensure_pnx_normalized_this_file()  # 현재 파일에 작성된 경로 자동 정규화
