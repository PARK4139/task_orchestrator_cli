import platform
from os import environ
from pathlib import Path

from sources.objects.pk_local_test_activate import LTA

# 프로젝트 기준 경로 : 상대경로는 절대경로에 의존
D_TASK_ORCHESTRATOR_CLI = Path(__file__).resolve().parent.parent.parent
D_TASK_ORCHESTRATOR_CLI_PARENTS = Path(__file__).resolve().parent.parent.parent.parent

if platform.system().lower() == "windows":
    D_USERPROFILE = Path(environ.get('USERPROFILE'))
    D_C_DRIVE = Path('C:/')
    D_D_DRIVE = Path('D:/')
    D_F_DRIVE = Path('F:/')
    D_G_DRIVE = Path('G:/')
    D_H_DRIVE = Path('H:/')
    D_I_DRIVE = Path('I:/')
    D_J_DRIVE = Path('J:/')
    D_TASK_ORCHESTRATOR_CLI = D_TASK_ORCHESTRATOR_CLI_PARENTS / "task_orchestrator_cli"

    D_G_DRIVE_PK_WORKING = D_G_DRIVE / "Downloads" / "pk_working"

    D_VENV = D_TASK_ORCHESTRATOR_CLI / '.venv_windows'

    D_DOWNLOADS = D_USERPROFILE / 'Downloads'
    D_DESKTOP = D_USERPROFILE / 'Desktop'
    D_PK_RECYCLE_BIN = D_DESKTOP / "휴지통"  # task_orchestrator_cli_option
    D_TEMP = D_PK_RECYCLE_BIN / "temp"
    D_TEST = D_TEMP / "test"
    D_TEST_RESULT = D_TEMP / "test_result"

    D_PK_DOWNLOADING = D_PK_RECYCLE_BIN

    D_TASK_ORCHESTRATOR_CLI_TESTS = D_TASK_ORCHESTRATOR_CLI / "task_orchestrator_cli_tests"
    D_TASK_ORCHESTRATOR_CLI_SENSITIVE = D_TASK_ORCHESTRATOR_CLI / 'task_orchestrator_cli_sensitive'

    D_TASK_ORCHESTRATOR_CLI_LOGS = None
    if LTA:
        # task_orchestrator_cli_option : recomanded
        # D_TASK_ORCHESTRATOR_CLI_LOGS = D_PK_RECYCLE_BIN / "logs"
        # D_TASK_ORCHESTRATOR_CLI_RESOURCES = D_PK_RECYCLE_BIN / 'resources'

        # task_orchestrator_cli_option : for gemini cli가 외부 경로에서 파일 리소스 못찾는 문제해결하기 위함.
        D_TASK_ORCHESTRATOR_CLI_LOGS = D_TASK_ORCHESTRATOR_CLI / "logs"
    else:
        D_TASK_ORCHESTRATOR_CLI_LOGS = D_TASK_ORCHESTRATOR_CLI / "logs"


    D_TASK_ORCHESTRATOR_CLI_RESOURCES = D_TASK_ORCHESTRATOR_CLI / 'resources'
    D_TASK_ORCHESTRATOR_CLI_SOURCES = D_TASK_ORCHESTRATOR_CLI / 'sources'
    D_TASK_ORCHESTRATOR_CLI_INFO = D_TASK_ORCHESTRATOR_CLI_SOURCES / 'system_info'
    D_TASK_ORCHESTRATOR_CLI_CACHE = D_TASK_ORCHESTRATOR_CLI / 'task_orchestrator_cli_cache'
    D_TTL_CACHE = D_TASK_ORCHESTRATOR_CLI_CACHE / 'ttl_cache'
    D_HISTORY_CACHE = D_TASK_ORCHESTRATOR_CLI_CACHE / "history_cache"

    D_PK_WORKING = D_DOWNLOADS / "pk_working"

    D_DOWNLOADED_FROM_TORRENT = D_PK_WORKING / "downloaded_from_torrent"
    D_PK_WORKING_S = D_G_DRIVE_PK_WORKING / "pk_working_s"

    D_PKG_ARCHIVED = D_TASK_ORCHESTRATOR_CLI_PARENTS / 'task_orchestrator_cli_archived'
    D_XLS_TO_MERGE = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / 'xls_files_to_merge'
    D_XLS_MERGED = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / 'xls_files'

    D_TASK_ORCHESTRATOR_CLI_FUNCTIONS = D_TASK_ORCHESTRATOR_CLI_SOURCES / "functions"
    D_TASK_ORCHESTRATOR_CLI_OBJECTS = D_TASK_ORCHESTRATOR_CLI_SOURCES / "objects"
    D_TASK_ORCHESTRATOR_CLI_REFACTORS = D_TASK_ORCHESTRATOR_CLI_SOURCES / "task_orchestrator_cli_refactors"
    D_TASK_ORCHESTRATOR_CLI_WRAPPERS = D_TASK_ORCHESTRATOR_CLI_SOURCES / "wrappers"

    D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES = D_TASK_ORCHESTRATOR_CLI_RESOURCES / 'system_resources'
    D_TASK_ORCHESTRATOR_CLI_VIDEO = D_TASK_ORCHESTRATOR_CLI_RESOURCES / 'task_orchestrator_cli_video'
    D_TASK_ORCHESTRATOR_CLI_SOUND = D_TASK_ORCHESTRATOR_CLI_RESOURCES / 'system_sounds'
    D_PKG_VIDEO = D_TASK_ORCHESTRATOR_CLI_RESOURCES / 'task_orchestrator_cli_video'
    D_TASK_ORCHESTRATOR_CLI_RESOURCES_WINDOWS = D_TASK_ORCHESTRATOR_CLI_RESOURCES / 'resources_windows'
    D_TASK_ORCHESTRATOR_CLI_VSTEST = D_TASK_ORCHESTRATOR_CLI / 'project_vstest'
    D_TASK_ORCHESTRATOR_CLI_FASTAPI = D_TASK_ORCHESTRATOR_CLI / 'project_fastapi'
    D_TASK_ORCHESTRATOR_CLI_CMAKE = D_TASK_ORCHESTRATOR_CLI / 'project_cmake'

    D_PKG_CLOUD = D_TASK_ORCHESTRATOR_CLI_FASTAPI / 'pkg_cloud'

    D_VIDEO_MERGED = D_PK_WORKING / "pk_video_merged"
    # D_PK_DOWNLOADING = D_PK_WORKING / "pk_downloading"
    D_HOW = D_PK_WORKING / "pk_how"
    D_ARCHIVED = D_PK_WORKING / "pk_archived"

    D_TASK_ORCHESTRATOR_CLI = D_DOWNLOADS / "task_orchestrator_cli"
    D_PK_MEMO = D_DOWNLOADS / "pk_memo"
    D_BUSINESS_DEMO = D_DOWNLOADS / "business_demo"

    D_ETC = Path("/etc") # WINDOWS 에서 WSL 경로 추론 시 필요.
else:
    D_ROOT = Path("/")
    D_ETC = Path("/etc")
    D_HOME = Path(environ.get('HOME')) # /home
    D_DOWNLOADS = D_HOME / 'Downloads'
    D_TASK_ORCHESTRATOR_CLI = D_DOWNLOADS / "task_orchestrator_cli"
    D_VENV = D_TASK_ORCHESTRATOR_CLI / '.venv_linux'
