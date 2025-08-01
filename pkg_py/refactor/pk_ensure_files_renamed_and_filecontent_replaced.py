import traceback

from pkg_py.system_object.directories import D_PROMPTS_FOR_AI, D_SYSTEM_OBJECT, D_PK_REFACTOR, D_PK_FUNCTIONS_SPLIT, D_PKG_PY, D_PKG_LINUX, D_PKG_WINDOWS, D_PKG_TXT
from pkg_py.system_object.directories_reuseable import D_PROJECT

if __name__ == "__main__":
    from pkg_py.functions_split.ensure_files_renamed_and_filecontent_replaced import ensure_files_renamed_and_filecontent_replaced

    # d_targets = [  # pk_option
    #     D_PROJECT,  # too slow for too many files exist. not recommanded
    # ]

    # d_targets = [ # pk_option
    #     F_MEMO_HOW_PK,
    #     F_MEMO_WORK_PK,
    # ]

    d_targets = [  # pk_option
        D_PKG_TXT,
        D_PKG_WINDOWS,
        D_PKG_LINUX,
        D_PKG_PY,
        D_PK_FUNCTIONS_SPLIT,
        D_PK_REFACTOR,
        D_SYSTEM_OBJECT,
        D_PROMPTS_FOR_AI,
    ]

    target_extensions = [".py", ".cmd", ".bat", ".ps1", ".sh", ".bak", ".txt"]  # pk_option

    old_string = rf'PKG_VIDEO'  # pk_option
    new_string = rf'PKG_VIDEO'  # pk_option

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


    for d_target in d_targets:
        ensure_files_renamed_and_filecontent_replaced(d_target, old_string, new_string, target_extensions=target_extensions)


