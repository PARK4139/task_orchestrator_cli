from pkg_py.functions_split import ensure_printed
from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_files_renamed_and_filecontent_replaced import ensure_files_renamed_and_filecontent_replaced
from pkg_py.functions_split.get_pnxs_from_d_working import get_pnxs_from_d_working
from pkg_py.system_object.directories import D_PK_SYSTEM
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025

if __name__ == "__main__":
    # d_targets = [  # pk_option
    #     D_PROJECT,  # too slow for too many files exist. not recommanded
    # ]

    # d_targets = [ # pk_option
    #     F_MEMO_HOW_PK,
    #     F_MEMO_WORK_PK,
    # ]

    # d_targets = [  # pk_option
    #     D_PKG_CACHE_PRIVATE,
    #     D_PKG_WINDOWS,
    #     D_PKG_LINUX,
    #     D_PKG_PY,
    #     D_PK_FUNCTIONS_SPLIT,
    #     D_PK_REFACTOR,
    #     D_SYSTEM_OBJECT,
    # ]

    d_targets = get_pnxs_from_d_working(d_working=D_PK_SYSTEM, only_dirs=True, with_walking=True)  # pk_option

    ignored_directory_names = [".venv", ".venv_linux", "__pycache__"]  # DONE : 필터검증

    # target_extensions = [".py", ".cmd", ".bat", ".ps1", ".sh", ".bak", ".txt"]  # pk_option
    target_extensions = [".py", ".cmd", ".bat", ".ps1", ".sh", ".bak", ".txt", ".md", ".zshrc", ".bashrc"]  # pk_option

    # old_string = rf'_optimized' * 2  # pk_option
    old_string = rf'_optimized'  # pk_option
    new_string = rf'_optimized'  # pk_option

    # TODO
    # old_string = rf'push_pnx_to_github'  # pk_option # 하드코딩 유지
    # double_object_verb = rf'ensure' # pk_option # 하드코딩 유지
    # object = rf'pnx' # 하드코딩말고 old_string에서 형태소 분석으로 목적어(object)를 추출하여 초기화
    # verb = rf'push' # 하드코딩말고 old_string에서 형태소 분석으로 동사(verb)를 추출하여 초기화
    # past_participle = rf'{verb}ed' # past participle 는 경우에 따라 ed 가 아닌 경우가 있어. 더 정확한 처리가 필요.
    # past_participle_and_decorating_word = old_string.replace(rf"_{object}_", "_").replace(verb, past_participle)
    # new_string = double_object_verb.removeprefix("_").removesuffix("_") + "_" + object.removeprefix("_").removesuffix("_") + "_" + past_participle_and_decorating_word.removeprefix("_").removesuffix("_")
    # ensure_printed(f'''[{PkMessages2025.DATA}] new_string={new_string} {'%%%FOO%%%' if LTA else ''}''')
    # ensure_console_debuggable(ipdb=ipdb)

    # mode = 3 # pk_option
    # s = rf'pk_ensure_venv_path_config_updated'
    # if mode == 1:
    #     old_string = s
    #     new_string = rf'pk_ensure_drag_changed_printed '
    # elif mode == 2: # deduplicate mode
    #     new_string = rf'at_time_promised'
    #     old_string = rf'{new_string}_{new_string}'
    # elif mode == 3:
    #     old_string = s[3:] if s.startswith("pk_") else s
    #     prefix = rf"pk_ensure"
    #     object = rf"venv_path_config"
    #     verb = rf"updateed"
    #     suffix = "_" + rf"via_google"
    #     suffix = ""
    #     new_string = rf"{prefix}_{object}_{verb}{suffix}"

    # pk_option : upper
    # for d_target in d_targets:
    #     ensure_files_renamed_and_filecontent_replaced(d_target, old_string.upper(), new_string.upper(), target_extensions=target_extensions, ignored_directory_names = ignored_directory_names)

    # pk_option : upper
    # for d_target in d_targets:
    #     ensure_files_renamed_and_filecontent_replaced(d_target, old_string.lower(), new_string.lower(), target_extensions=target_extensions, ignored_directory_names=ignored_directory_names)

    # pk_option : keep cases
    for d_target in d_targets:
        ensure_files_renamed_and_filecontent_replaced(d_target, old_string, new_string, target_extensions=target_extensions, ignored_directory_names=ignored_directory_names)
