import ast
import inspect
import logging
import re
import traceback
from pathlib import Path
from pkg_py.functions_split.backup_workspace import backup_workspace
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_elapsed_time_logged import ensure_elapsed_time_logged
from pkg_py.functions_split.ensure_start_time_logged import ensure_start_time_logged
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
from pkg_py.functions_split.pk_initialize_and_customize_logging_config import pk_initialize_and_customize_logging_config
from pkg_py.functions_split.restore_workspace_from_latest_archive import restore_workspace_from_latest_archive
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
from pkg_py.pk_system_object.directories import D_PKG_ARCHIVED, D_FUNCTIONS_SPLIT
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE


def extract_imports_from_code(code):
    """코드 전체에서 import문 추출(set 반환)"""
    import_lines = set()
    for line in code.splitlines():
        if line.strip().startswith("import ") or line.strip().startswith("from "):
            import_lines.add(line.strip())
    return import_lines


def extract_imports_from_functions(code):
    """함수 내부 import문 추출(set 반환)"""
    imports = set()
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                for n in ast.walk(node):
                    if isinstance(n, (ast.Import, ast.ImportFrom)):
                        imports.add(ast.get_source_segment(code, n))
    except Exception:
        pass
    return imports


def collect_imports_from_dir(directory):
    all_imports = set()
    for pyfile in Path(directory).rglob('*.py'):
        try:
            code = pyfile.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                code = pyfile.read_text(encoding='cp949')
            except Exception as e:
                print(f"[SKIP] {pyfile} (decode error: {e})")
                continue
        except Exception as e:
            print(f"[SKIP] {pyfile} (other error: {e})")
            continue
        all_imports |= extract_imports_from_code(code)
    return all_imports


def insert_imports_to_code(code, general_imports, lazy_imports, main_imports):
    """import문을 위치별로 삽입"""
    lines = code.splitlines()
    # 1. general: 파일 최상단 기존 import문 아래
    first_non_import = 0
    for i, line in enumerate(lines):
        if not (line.strip().startswith("import ") or line.strip().startswith("from ")):
            first_non_import = i
            break
    new_lines = []
    # general import 삽입
    new_lines.extend(sorted(general_imports))
    # 기존 import문 스킵
    while lines and (lines[0].strip().startswith("import ") or lines[0].strip().startswith("from ")):
        lines.pop(0)
    # 나머지 코드
    new_lines.extend(lines)
    code = "\n".join(new_lines)

    # 2. lazy: 함수 내부에 삽입
    if lazy_imports:
        def insert_lazy_imports(code, lazy_imports):
            # 함수 정의 바로 아래에 삽입
            pattern = re.compile(r'(def\s+\w+\s*\(.*?\)\s*:)')

            def replacer(match):
                return f"{match.group(1)}\n    " + "\n    ".join(sorted(lazy_imports))

            return pattern.sub(replacer, code)

        code = insert_lazy_imports(code, lazy_imports)

    # 3. main: if __name__ == "__main__": 블록 바로 아래에 삽입
    if main_imports:
        pattern = re.compile(r'(if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:)')

        def main_replacer(match):
            return f"{match.group(1)}\n    " + "\n    ".join(sorted(main_imports))

        code = pattern.sub(main_replacer, code)
    return code


# 1. d_import_path_reference 내 모든 .py 파일에서 import문 추출
# 아래 함수는 이미 위에 정의되어 있으므로, 중복 정의를 삭제하세요.
# def collect_imports_from_dir(directory):
#     all_imports = set()
#     for pyfile in Path(directory).rglob('*.py'):
#         code = pyfile.read_text(encoding='utf-8')
#         all_imports |= extract_imports_from_code(code)
#     return all_imports

 


def pk_ensure_modules_imported_proper():
    while True:
        func_n = inspect.currentframe().f_code.co_name
        if LTA:
            d_working = D_FUNCTIONS_SPLIT
            d_import_path_reference = D_PROJECT
            import_location = "lazy_import_location"
            # exec_mode = PkMessages2025.PREVIEW
            exec_mode = PkMessages2025.EXECUTION
        else:
            key_name = "d_working"
            d_working = get_values_from_historical_file_routine(
                file_id=get_file_id(key_name, func_n),
                key_hint=f'{key_name}=',
                options_default=[D_FUNCTIONS_SPLIT]
            )
            key_name = "d_import_path_reference"
            d_import_path_reference = get_values_from_historical_file_routine(
                file_id=get_file_id(key_name, func_n),
                key_hint=f'{key_name}=',
                options_default=[D_PROJECT]
            )
            key_name = "lazy_import_location"
            import_location = get_values_from_historical_file_routine(
                file_id=get_file_id(key_name, func_n),
                key_hint=f'{key_name}=',
                options_default=["general_import_location", "lazy_import_location"]
            )
            exec_mode = get_value_completed(
                key_hint=f"{PkMessages2025.MODE}=",
                values=[PkMessages2025.PREVIEW, PkMessages2025.EXECUTION]
            ).strip()

        dry_run = exec_mode == PkMessages2025.PREVIEW

        # 0. 경로 정규화
        d_working = str(Path(d_working).resolve())
        d_import_path_reference = str(Path(d_import_path_reference).resolve())

        logging.info(f"[{func_n}] mode: {exec_mode}, dry_run: {dry_run}")
        archive_path = None

        if dry_run:
            pass
        else:
            # 0. backup
            logging.info("backup_workspace 진입")
            archive_path = backup_workspace(D_PKG_ARCHIVED, d_working, func_n)
            logging.info("backup_workspace 종료")
            # 2. organize modules import location
            try:
                start_time = ensure_start_time_logged()
                reference_imports = collect_imports_from_dir(d_import_path_reference)
                logging.info(f"import organize loop start: d_working={d_working}")
                pyfiles = list(Path(d_working).rglob('*.py'))
                total_files = len(pyfiles)
                print(f"[INFO] d_working 내 파일 수: {total_files}")
                if total_files > 1000:
                    proceed = input("파일이 1000개를 초과합니다. 계속 진행하시겠습니까? (y/n): ")
                    if proceed.lower() != 'y':
                        print("작업을 중단합니다.")
                        return

                preview_changes = []
                for idx, pyfile in enumerate(pyfiles, 1):
                    logging.info(f"[{idx}/{total_files}] checking file: {pyfile}")
                    try:
                        code = pyfile.read_text(encoding='utf-8')
                        file_imports = extract_imports_from_code(code)
                        func_imports = extract_imports_from_functions(code)
                        general_imports = reference_imports | file_imports
                        lazy_imports = func_imports - general_imports
                        main_imports = general_imports
                        new_code = insert_imports_to_code(
                            code,
                            general_imports=general_imports,
                            lazy_imports=lazy_imports,
                            main_imports=main_imports
                        )
                        if new_code != code:
                            preview_changes.append(f"=== {pyfile} ===\n{new_code}\n")
                        else:
                            logging.info(f"no change for {pyfile}")
                    except Exception as e:
                        logging.warning(f"[IMPORT ORGANIZE FAIL] {pyfile}: {e}")
                # 미리보기 파일로 저장
                if preview_changes:
                    preview_path = Path(d_working) / "preview_import_changes.txt"
                    with open(preview_path, "w", encoding="utf-8") as f:
                        f.write("\n\n".join(preview_changes))
                    print(f"[INFO] 변경될 import 내용을 {preview_path}에 저장했습니다.")
                    confirm = input("위 내용을 실제로 적용하시겠습니까? (y/n): ")
                    if confirm.lower() != 'y':
                        print("작업을 중단합니다.")
                        return
                # 실제 적용
                for idx, pyfile in enumerate(pyfiles, 1):
                    logging.info(f"[{idx}/{total_files}] applying changes to: {pyfile}")
                    try:
                        code = pyfile.read_text(encoding='utf-8')
                        file_imports = extract_imports_from_code(code)
                        func_imports = extract_imports_from_functions(code)
                        general_imports = reference_imports | file_imports
                        lazy_imports = func_imports - general_imports
                        main_imports = general_imports
                        new_code = insert_imports_to_code(
                            code,
                            general_imports=general_imports,
                            lazy_imports=lazy_imports,
                            main_imports=main_imports
                        )
                        if new_code != code:
                            if dry_run:
                                logging.info(f"[PREVIEW][IMPORT ORGANIZED] {pyfile}")
                            else:
                                pyfile.write_text(new_code, encoding='utf-8')
                                logging.info(f"[IMPORT ORGANIZED] {pyfile}")
                        else:
                            logging.info(f"no change for {pyfile}")
                    except Exception as e:
                        logging.warning(f"[IMPORT ORGANIZE FAIL] {pyfile}: {e}")
                elapsed_time = ensure_elapsed_time_logged(start_time)
            except Exception as e:
                # 예외 발생 시 자동 복구
                if archive_path:
                    restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_import_path_reference)
                raise

            if dry_run:
                pass
            else:
                # 3. after service
                if not dry_run:
                    decision = get_value_completed(
                        key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
                        values=[f"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}", PkMessages2025.REVERT],
                    )
                    if decision == f"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}":
                        # 원본 삭제(필요 시 구현)
                        pass
                    else:
                        # 복구
                        restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_import_path_reference)

        logging.info(f"[{func_n}] Finished with mode={exec_mode}, dry_run={dry_run}")

        if LTA:
            ensure_console_debuggable()

        ensure_console_cleared()

if __name__ == "__main__":
    try:
        pk_initialize_and_customize_logging_config(__file__=__file__)
        pk_ensure_modules_imported_proper()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
