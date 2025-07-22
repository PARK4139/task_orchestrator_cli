import inspect
import logging
import os
import os.path
import re
import traceback

from pkg_py.functions_split.backup_workspace import backup_workspace
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_list_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.pk_initialize_and_customize_logging_config import pk_initialize_and_customize_logging_config
from pkg_py.functions_split.restore_workspace_from_latest_archive import restore_workspace_from_latest_archive
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.refactor.A300_pk_ensure_modules_imported_front import clean_import_block


def move_import_to_function_start(body_lines, indent_level):
    """본문 중간에 있는 import 문을 함수 시작 부분으로 이동"""
    imports = []
    non_import_lines = []

    # 임포트 문을 함수 본문에서 분리
    for line in body_lines:
        if re.match(r'^\s*(import|from\s+\w+\s+import)\b', line.strip()):
            imports.append(line.strip())
        else:
            non_import_lines.append(line)

    # 적절한 들여쓰기를 적용한 import 문 생성
    formatted_imports = [f"{' ' * indent_level}{imp}\n" for imp in imports]
    return formatted_imports + non_import_lines


def pk_ensure_modules_imported_lazy_once(f_working, D_PKG_ARCHIVED, preview=False):
    """모듈 임포트를 lazy하게 업데이트하고 백업 및 복원 기능 추가"""
    # 백업
    func_n = inspect.currentframe().f_code.co_name
    archive_path = backup_workspace(D_PKG_ARCHIVED, f_working, func_n)

    with open(file=f_working, mode='r', encoding=Encoding.UTF8.value) as f_obj:
        lines = f_obj.readlines()

    updated_lines = []
    inside_function = False
    function_body = []
    function_indent = 0

    # 1. 사용자 임포트 블록 가져오기
    f_module_template = os.path.join(D_PKG_PY, "refactor", "pk_template_modules.py")
    cleaned_import_block = clean_import_block(f_module_template)

    # 파일의 각 라인 처리
    for line in lines:
        stripped_line = line.strip()
        indent_level = len(line) - len(stripped_line)

        if stripped_line.startswith("def ") and stripped_line.endswith(":"):
            if inside_function:
                # 함수 종료 시점 처리: import 정리
                cleaned_body = move_import_to_function_start(function_body, function_indent + 4)
                updated_lines.extend(cleaned_body)
                function_body = []

            # 새로운 함수 시작
            inside_function = True
            function_indent = indent_level
            updated_lines.append(line)
        elif inside_function:
            if indent_level <= function_indent and stripped_line:
                # 함수 종료 시점 처리
                cleaned_body = move_import_to_function_start(function_body, function_indent + 4)
                updated_lines.extend(cleaned_body)
                function_body = []

                # 새로운 블록이 시작된 경우
                inside_function = False
                updated_lines.append(line)
            else:
                function_body.append(line)
        else:
            updated_lines.append(line)

    # 마지막 함수 처리
    if inside_function:
        cleaned_body = move_import_to_function_start(function_body, function_indent + 4)
        updated_lines.extend(cleaned_body)

    # 미리보기 모드에서는 실제 파일 수정 없이 출력만
    if preview:
        logging.info(f"[{PkMessages2025.PREVIEW}] 수정된 파일 내용 미리보기: '{f_working}'")
        logging.info(f"[{PkMessages2025.PREVIEW}] 추가될 임포트 블록: \n{cleaned_import_block}")
        for line in updated_lines:
            logging.info(line.strip())
    else:
        # 실제 수정이 실행 모드에서만 수행됨
        with open(file=f_working, mode='w', encoding=Encoding.UTF8.value) as f_out:
            f_out.writelines(updated_lines)

        logging.info(f"[{PkMessages2025.INSERTED}] 수정된 파일이 '{f_working}'에 저장되었습니다.")

    # REVERT 기능
    decision = get_value_completed(
        key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
        values=[rf"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}", PkMessages2025.REVERT],
    )

    if decision == PkMessages2025.REVERT:
        restore_workspace_from_latest_archive(D_PKG_ARCHIVED, f_working)
    else:
        logging.info(f"백업이 '{archive_path}'에 저장되었습니다.")


def pk_ensure_modules_imported_lazy():
    from enum import Enum
    encoding: Enum

    # 작업 디렉토리 설정
    d_working = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_py\workspace"
    D_PKG_ARCHIVED = rf"{os.environ['USERPROFILE']}\Downloads\pk_system\pkg_archived"

    # 실행 모드 설정 (프리뷰 또는 실제 실행 모드)
    exec_mode = get_value_completed(
        key_hint=f"{PkMessages2025.MODE}=",
        values=[PkMessages2025.PREVIEW, f"{PkMessages2025.DEFAULT} {PkMessages2025.EXECUTION}"]
    ).strip()

    preview = exec_mode == PkMessages2025.PREVIEW

    # .py 파일을 하나씩 처리
    for f_working in get_pnxs_from_d_working(d_working=d_working):
        if is_f(f_working):
            if get_nx(f_working) != "__init__.py" and get_nx(f_working) != "pk_woring.py":
                pk_ensure_modules_imported_lazy_once(f_working, D_PKG_ARCHIVED, preview)


if __name__ == "__main__":
    try:
        pk_initialize_and_customize_logging_config(__file__)
        pk_ensure_modules_imported_lazy()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
