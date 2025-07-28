if __name__ == "__main__":
    from pkg_py.functions_split.ensure_files_renamed_and_filecontent_replaced import ensure_files_renamed_and_filecontent_replaced
    from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT, D_PKG_PY, D_PK_REFACTOR, D_PKG_WINDOWS, D_PKG_TXT, D_PKG_SH, D_SYSTEM_OBJECT

    d_targets = [  # pk_option
        # D_PROJECT,  # too slow for too many files exist. not recommanded
        D_PKG_TXT,
        D_PKG_WINDOWS,
        D_PKG_SH,
        D_PKG_PY,
        D_PK_FUNCTIONS_SPLIT,
        D_PK_REFACTOR,
        D_SYSTEM_OBJECT,
    ]
    # d_targets = [ # pk_option
    #     F_MEMO_HOW_PK,
    #     F_MEMO_WORK_PK,
    # ]

    target_extensions = [".py", ".cmd", ".bat", ".ps1", ".sh", ".bak", ".txt"]  # pk_option

    old_string = rf'ensure_spoken_v'  # pk_option
    new_string = rf'ensure_spoken_v'  # pk_option
    for d_target in d_targets:
        ensure_files_renamed_and_filecontent_replaced(d_target, old_string, new_string, target_extensions=target_extensions)
