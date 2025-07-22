import inspect
import logging
import os
import os.path
import os.path
import traceback

from pkg_py.functions_split.backup_workspace import backup_workspace
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.get_str_from_f import get_str_from_f
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.pk_initialize_and_customize_logging_config import pk_initialize_and_customize_logging_config
from pkg_py.functions_split.restore_workspace_from_latest_archive import restore_workspace_from_latest_archive
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_directories import D_PKG_ARCHIVED
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE


def clean_import_block(block: str) -> str:
    result_lines = []
    for line in block.strip().splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            stripped = stripped[1:].strip()  # Remove comment characters
        result_lines.append(stripped)
    return "\n".join(result_lines)


def pk_ensure_modules_import_to_python_files():
    func_name = inspect.currentframe().f_code.co_name
    d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\split_functions"
    d_backup_root = os.path.join(D_PKG_PY, "..", "pkg_archived")
    f_module_template = os.path.join(D_PKG_PY, "refactor", "pk_template_modules.py")
    # 6. 파일 처리 (프리뷰 모드에서는 실제 파일 수정 없이 출력만)
    loop_cnt = 1
    while True:
        # 1. 파일 경로 확인
        if not os.path.isdir(d_working):
            logging.warning(f"[{PkMessages2025.PATH_NOT_FOUND}] {d_working}")
            return

        # 2. 사용자가 작성한 임포트 블록 가져오기
        raw_import_block = get_str_from_f(f=f_module_template)
        cleaned_import_block = clean_import_block(raw_import_block)

        # 3. 사용자 입력으로 preview 모드 선택
        preview_mode = get_value_completed(
            key_hint=f"{PkMessages2025.MODE}=",
            values=[PkMessages2025.PREVIEW, f"{PkMessages2025.DEFAULT} {PkMessages2025.EXECUTION}"]
        ) == PkMessages2025.PREVIEW

        # 4. .py 파일 경로 가져오기
        py_files = [f for f in os.listdir(d_working) if f.endswith('.py')]
        full_paths = [os.path.join(d_working, f) for f in py_files]

        if not full_paths:
            logging.info(f"[{PkMessages2025.LISTED}] No .py files found.")
            return

        # 5. 백업 수행 (실제 실행 모드에서만)
        archive_path = None
        if not preview_mode:
            archive_path = backup_workspace(d_working, d_backup_root, func_name)

        for root, _, files in os.walk(d_working):
            for file in files:
                if not file.endswith(".py"):
                    continue

                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # 임포트 블록이 이미 존재하는지 확인
                if all(line in content for line in cleaned_import_block.splitlines()):
                    logging.info(f"[{PkMessages2025.SKIPPED}] already contains imports: {file_path}")
                    continue

                # 프리뷰 모드일 경우 수정 예시만 출력
                if preview_mode:
                    logging.info(f"[{PkMessages2025.PREVIEW}] will insert imports into: {file_path}")
                else:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(cleaned_import_block + "\n\n" + content)
                    logging.info(f"[{PkMessages2025.INSERTED}] imports added to: {file_path}")
                loop_cnt += 1

        # 7. 후속 서비스 (삭제 또는 복원)
        if not preview_mode:
            decision = get_value_completed(
                key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
                values=[PkMessages2025.SATISFIED, PkMessages2025.REVERT],
            )
            if decision == PkMessages2025.SATISFIED:
                logging.info(f"[{PkMessages2025.SATISFIED}]")
                logging.info(f"[{PkMessages2025.DONE}] import injection {'(preview)' if preview_mode else '(executed)'}")
                # ensure_pk_system_exit_silent() # pk_option
                continue
            elif decision == PkMessages2025.REVERT:
                restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)  # REVERT 실행
                logging.info(f"[{PkMessages2025.DONE}] {PkMessages2025.REVERT}")


def main():
    try:
        pk_initialize_and_customize_logging_config(__file__)
        pk_ensure_modules_import_to_python_files()
    except Exception as e:
        ensure_do_exception_routine(traceback=traceback, exception=e)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)


if __name__ == "__main__":
    main()
