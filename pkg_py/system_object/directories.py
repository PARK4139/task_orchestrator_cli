import os

from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.system_object.directories_reuseable import D_PROJECT, D_HOME, D_PROJECT_PARENTS

D_C_DRIVE = rf'C:/'
D_D_DRIVE = rf'D:/'
D_F_DRIVE = rf'F:/'
D_G_DRIVE = rf'G:/'
D_H_DRIVE = rf'H:/'
D_I_DRIVE = rf'I:/'
D_J_DRIVE = rf'J:/'
D_DOWNLOADS = rf'{D_HOME}/Downloads'
D_WORKING = rf"{D_DOWNLOADS}/pk_working"
D_PK_MEMO = rf"{D_DOWNLOADS}/pk_memo"
D_WORKING_EXTERNAL = rf"G:/Downloads/pk_working"
D_VENV = rf'{D_PROJECT}/.venv'
D_XLS_TO_MERGE = rf'{D_PROJECT}/pkg_xls/to_merge'
D_XLS_MERGED = rf'{D_PROJECT}/pkg_xls/merged'
D_VIDEOES_MERGED = rf"{D_WORKING}/pk_video_merged"
D_DESKTOP = rf'{D_HOME}/Desktop'
D_PK_RECYCLE_BIN = rf"{D_DESKTOP}/pk_recycle_bin"
D_PROJECT_VSTEST = rf'{D_PROJECT}/project_vstest'
D_PROJECT_RELEASE_SERVER = rf'{D_PROJECT}/project_release_server'
D_PROJECT_FASTAPI = rf'{D_PROJECT}/project_fastapi'
D_PROJECT_CMAKE = rf'{D_PROJECT}/project_cmake'
D_STATIC = os.path.join(D_PROJECT_FASTAPI, "pkg_web", "static")
D_PKG_ARCHIVED = rf'{D_PROJECT}/pkg_archived'
D_PKG_EXE = rf'{D_PROJECT}/pkg_exe'
D_PKG_DB = rf'{D_PROJECT}/pkg_db'
D_PKG_CSV = rf'{D_PROJECT}/pkg_csv'
D_PKG_VIDEO = rf'{D_PROJECT}/pkg_video'
D_PKG_TXT = rf'{D_PROJECT}/pkg_txt'
D_PKG_TOML = rf'{D_PROJECT}/pkg_toml'
D_PKG_PY = rf'{D_PROJECT}/pkg_py'
D_PKG_PNG = rf'{D_PROJECT_FASTAPI}/pkg_png'
D_PKG_LOG = rf'{D_PROJECT}/pkg_log'
D_PKG_JSON = rf'{D_PROJECT}/pkg_json'
D_PKG_IMAGE = rf'{D_PROJECT}/pk_image'
D_PKG_DPL = rf'{D_PROJECT}/pkg_dpl'
D_PKG_CLOUD = rf'{D_PROJECT_FASTAPI}/pkg_cloud'
D_PKG_WINDOWS = rf'{D_PROJECT}/pkg_windows'
D_HOW = rf"{D_DOWNLOADS}/pk_working/pk_how"
D_EMPTY = rf"{D_WORKING}/pk_empty"
D_DOWNLOADING = rf"{D_WORKING}/pk_downloading"
D_CODING_TEST_RESULT = rf'{D_PROJECT}/pkg_coding_test_submit'
D_CLASSIFIED = rf"{D_DOWNLOADS}/pk_working"  # TODO : deprecate
D_ARCHIVED_EXTERNAL = rf"{D_WORKING_EXTERNAL}/pk_archived"
D_ARCHIVED = rf"{D_DOWNLOADS}/pk_working/pk_archived"
D_PK_TEMP = rf"{D_HOME}/pk_temp"
D_PKG_PKL = rf"{D_PROJECT}/pkg_pkl"
D_PKG_MP4 = rf"{D_PROJECT}/pkg_mp4"
D_TESTS = rf"{D_PROJECT}/tests"
D_WORKSPACE = rf"{D_PKG_PY}/workspace"
D_FUNCTIONS_SPLIT = rf"{D_PKG_PY}/functions_split"
D_SYSTEM_OBJECT = rf"{D_PKG_PY}/system_object"
D_PKG_HISTORY = rf"{D_PROJECT}/pkg_history"

D_PKG_PK = rf'{D_PROJECT_PARENTS}/pk_memo/pkg_pk'
D_PROJECT_MEMO = rf"{D_PROJECT_PARENTS}/pk_memo"

# external device directory
D_DEPRECATED_EXTERNAL = rf"G:/pk_deprecated"


