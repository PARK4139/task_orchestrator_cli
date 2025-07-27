from pkg_py.functions_split.ensure_files_renamed_and_filecontent_replaced import ensure_files_renamed_and_filecontent_replaced
from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT, D_PKG_PY, D_PK_REFACTOR, D_PKG_WINDOWS, D_PKG_TXT

# 사용 예시
if __name__ == "__main__":
    d_targets = [
        # D_PROJECT, # pk_option # 너무파일이 많아 느림. 사용하지 않는 것을 추천
        D_PKG_TXT,  # pk_option
        D_PKG_WINDOWS,  # pk_option
        # D_PKG_SH , # pk_option
        D_PKG_PY,  # pk_option
        D_PK_FUNCTIONS_SPLIT,
        D_PK_REFACTOR,
        # D_PK_SYSTEM_OBJECT,
    ]

    target_extensions = [".py", ".cmd", ".bat", ".ps1", ".sh"]  # pk_option
    oldstr = rf'testtesttest'
    new_str = rf'G:\Downloads'
    # new_str = "ensure_" + "losslesscut_reran"

    for d_target in d_targets:
        ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str, target_extensions=target_extensions)
