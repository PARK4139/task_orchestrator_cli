from pkg_py.functions_split.ensure_pnx_normalized_this_file import ensure_pnx_normalized_this_file

import socket
from os import environ
from pathlib import Path

HOSTNAME = environ.get('HOSTNAME', socket.gethostname())

D_PROJECT = str(Path(__file__).resolve().parent.parent.parent)
D_PROJECT_PARENTS = str(Path(D_PROJECT).parent)
D_HOME = environ.get('USERPROFILE') or environ.get('HOME')  # Windows 우선, Linux/macOS fallback # 상대경로의 사용은 필연적인데, 상대경로로 경로를 설정할때 기준이 되는 절대경로 하나는 반드시 필요한 것 같다.
D_USERPROFILE = D_HOME
D_C_DRIVE = rf'C:/'
D_DOWNLOADS = rf'{D_HOME}/Downloads'
D_DESKTOP = rf'{D_HOME}/Desktop'
D_PK_WORKING = rf"{D_DOWNLOADS}/pk_working"
D_XLS_TO_MERGE = rf'{D_PROJECT}/pkg_xls/to_merge'
D_XLS_MERGED = rf'{D_PROJECT}/pkg_xls/merged'
D_VENV = rf'{D_PROJECT}/.venv'
D_TESTS = rf"{D_PROJECT}/tests"
D_PROJECT_VSTEST = rf'{D_PROJECT}/project_vstest'
D_PROJECT_FASTAPI = rf'{D_PROJECT}/project_fastapi'
D_PROJECT_CMAKE = rf'{D_PROJECT}/project_cmake'
D_PKG_WINDOWS = rf'{D_PROJECT}/pkg_windows'
D_PKG_LINUX = rf'{D_PROJECT}/pkg_linux'
D_PKG_VIDEO = rf'{D_PROJECT}/pkg_video'
D_PKG_CACHE_PRIVATE = rf'{D_PROJECT}/pkg_cache_private'
D_PKG_TOML = rf'{D_PROJECT}/pkg_toml'
D_PKG_PY = rf'{D_PROJECT}/pkg_py'
D_PKG_LOG = rf'{D_PROJECT}/pkg_log'
D_PKG_JSON = rf'{D_PROJECT}/pkg_json'
D_PKG_IMAGE_AND_VIDEO_AND_SOUND = rf'{D_PROJECT}/pkg_image_and_video_and_sound'
D_PKG_DPL = rf'{D_PROJECT}/pkg_video'
D_PKG_DB = rf'{D_PROJECT}/pkg_cache_private'
D_PKG_CLOUD = rf'{D_PROJECT_FASTAPI}/pkg_cloud'
D_VIDEO_MERGED = rf"{D_PK_WORKING}/pk_video_merged"
D_SYSTEM_OBJECT = rf"{D_PKG_PY}/system_object"
D_PKG_ARCHIVED = rf'{D_PKG_CACHE_PRIVATE}/pkg_archived'
D_PK_SYSTEM = rf"{D_DOWNLOADS}/pk_system"
D_PK_MEMO = rf"{D_DOWNLOADS}/pk_memo"
D_PK_RECYCLE_BIN = rf"{D_DESKTOP}/휴지통"  # pk_option
# D_PK_DOWNLOADING = rf"{D_PK_WORKING}/pk_downloading"
D_PK_DOWNLOADING = D_PK_RECYCLE_BIN
D_HOW = rf"{D_DOWNLOADS}/pk_working/pk_how"
D_PK_FUNCTIONS_SPLIT = rf"{D_PKG_PY}/functions_split"
D_PK_REFACTOR = rf"{D_PKG_PY}/refactor"
D_BUSINESS_DEMO = rf"{D_DOWNLOADS}/business_demo"
D_ARCHIVED = rf"{D_DOWNLOADS}/pk_working/pk_archived"
D_PKG_PK = rf'{D_PROJECT_PARENTS}/pk_memo/pkg_pk'
D_PROJECT_MEMO = rf"{D_PROJECT_PARENTS}/pk_memo"
D_G_DRIVE_PK_WORKING = rf"G:/Downloads/pk_working"
# D_CODING_TEST_RESULT = rf'{D_PROJECT}/pkg_coding_test_submit'
# D_ARCHIVED_EXTERNAL = rf"{D_G_DRIVE_PK_WORKING}/pk_archived"
# D_STATIC = os.path.join(D_PROJECT_FASTAPI, "pkg_web", "static")
# D_PROJECT_RELEASE_SERVER = rf'{D_PROJECT}/project_ensure_release_server_ran'
D_D_DRIVE = rf'D:/'
D_F_DRIVE = rf'F:/'
D_G_DRIVE = rf'G:/'
D_H_DRIVE = rf'H:/'
D_I_DRIVE = rf'I:/'
D_J_DRIVE = rf'J:/'


def get_normalized_path(path: str) -> str:
    """경로를 OS에 맞게 정규화"""
    try:
        from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
        return str(get_pnx_os_style(path))
    except ImportError:
        # If import fails, return the original path
        return path


def normalize_pnx_prefix_paths(prefixes=('D_', 'F_')):
    """지정된 접두사를 가진 경로 변수들을 정규화"""
    for k, v in list(globals().items()):
        if any(k.startswith(prefix) for prefix in prefixes) and isinstance(v, str):
            try:
                new_path = get_normalized_path(v)
                globals()[k] = new_path
                print(f"[정규화] {k}: {v} -> {new_path}")
            except Exception as e:
                print(f"[스킵] {k}: {e}")


ensure_pnx_normalized_this_file()  # 현재 파일에 작성된 경로 자동 정규화
