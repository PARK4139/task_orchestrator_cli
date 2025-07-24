import subprocess
import sys

from pkg_py.functions_split.get_list_contained_element import get_list_contained_element
from pkg_py.functions_split.get_pnx_list_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.get_str_from_list import get_str_from_list
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.pk_system_object.directories import D_TESTS


def run_pytest_file(path: str):
    cmd_list = ""
    # verbose_mode = True
    verbose_mode = False
    verbose_option = '-s'
    if verbose_mode:
        cmd_list = [sys.executable, "-m", "pytest", verbose_option, path]
    else:
        cmd_list = ["pytest", path]
    cmd = get_str_from_list(working_list=cmd_list, item_connector=" ")
    pk_print(f"[RUNNING] {cmd}")
    result = subprocess.run(cmd_list)
    if result.returncode != 0:
        pk_print(f"[FAIL] 테스트 실패: {path}")
    else:
        pk_print(f"[PASS] 테스트 성공: {path}")


if __name__ == "__main__":
    # TBD : 테스트 TODO.
    test_files = get_pnxs_from_d_working(d_working=D_TESTS)
    test_suffix = 2025
    test_files_filtered = get_list_contained_element(working_list=test_files, suffix=f"_{test_suffix}")

    pk_print(f"[STARTED] TEST files of {D_TESTS}")

    tested_file_cnt = 0
    for file in test_files_filtered:
        pk_print(f"[DETECTED] {file}")
        run_pytest_file(file)
        tested_file_cnt += 1

    skipped_file_cnt = len(test_files) - tested_file_cnt

    pk_print(f"[ENDED] TEST VIA PYTEST {tested_file_cnt}EA files of {D_TESTS} (skipped {skipped_file_cnt} files of len({len(test_files)})")
