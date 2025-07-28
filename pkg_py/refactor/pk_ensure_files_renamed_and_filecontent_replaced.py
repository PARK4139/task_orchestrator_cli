from pkg_py.functions_split.ensure_files_renamed_and_filecontent_replaced import ensure_files_renamed_and_filecontent_replaced
from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT, D_PKG_PY, D_PK_REFACTOR, D_PKG_WINDOWS, D_PKG_TXT, D_PKG_SH, D_PK_SYSTEM_OBJECT

# example
if __name__ == "__main__":
    d_targets = [
        # D_PROJECT, # pk_option # 너무파일이 많아 느림. 사용하지 않는 것을 추천
        D_PKG_TXT,  # pk_option
        D_PKG_WINDOWS,  # pk_option
        D_PKG_SH , # pk_option
        D_PKG_PY,  # pk_option
        D_PK_FUNCTIONS_SPLIT,
        D_PK_REFACTOR,
        D_PK_SYSTEM_OBJECT,
    ]

    target_extensions = [".py", ".cmd", ".bat", ".ps1", ".sh", ".bak", ".txt"]  # pk_option

    old_string = rf'ensure_colorama_initialized_once' # pk_option
    new_string = rf'ensure_colorama_initialized_once' # pk_option

    for d_target in d_targets:
        ensure_files_renamed_and_filecontent_replaced(d_target, old_string, new_string, target_extensions=target_extensions)
