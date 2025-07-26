import subprocess
import sys

from pkg_py.functions_split.get_list_contained_element import get_list_contained_element
from pkg_py.functions_split.get_pnxs_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.get_str_from_list import get_str_from_list
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.directories import D_TESTS


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
    ensure_printed(f"[RUNNING] {cmd}")
    result = subprocess.run(cmd_list)
    if result.returncode != 0:
        ensure_printed(f"[FAIL] 테스트 실패: {path}")
    else:
        ensure_printed(f"[PASS] 테스트 성공: {path}")


if __name__ == "__main__":
    test_files = get_pnxs_from_d_working(d_working=D_TESTS)
    test_suffix = 2025
    test_files_filtered = get_list_contained_element(working_list=test_files, suffix=f"_{test_suffix}")

    ensure_printed(f"[STARTED] TEST files of {D_TESTS}")

    tested_file_cnt = 0
    for file in test_files_filtered:
        ensure_printed(f"[DETECTED] {file}")
        run_pytest_file(file)
        tested_file_cnt += 1

    skipped_file_cnt = len(test_files) - tested_file_cnt

    ensure_printed(f"[ENDED] TEST VIA PYTEST {tested_file_cnt}EA files of {D_TESTS} (skipped {skipped_file_cnt} files of len({len(test_files)})")
