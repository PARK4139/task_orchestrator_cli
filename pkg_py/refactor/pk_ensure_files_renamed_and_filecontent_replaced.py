from pkg_py.functions_split.ensure_files_renamed_and_filecontent_replaced import ensure_files_renamed_and_filecontent_replaced
from pkg_py.system_object.directories import D_FUNCTIONS_SPLIT, D_PKG_PY, D_REFACTOR

# 사용 예시
if __name__ == "__main__":
    d_target = D_PKG_PY
    oldstr = "ensure_console_paused"
    new_str = "ensure_console_paused"
    # new_str = "ensure_" + "losslesscut_reran"
    ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)

    d_target = D_FUNCTIONS_SPLIT
    ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)

    d_target = D_REFACTOR
    ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)

    # d_target = D_PK_SYSTEM_OBJECT
    # ensure_files_renamed_and_filecontent_replaced(d_target, oldstr, new_str)
