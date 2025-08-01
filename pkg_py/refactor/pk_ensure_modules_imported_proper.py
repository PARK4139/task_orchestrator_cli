import inspect
import logging
import os
import re
import shutil
import traceback
from datetime import datetime
from pathlib import Path

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.initialize_and_customize_logging_config import initialize_and_customize_logging_config
from pkg_py.system_object.directories import D_ARCHIVED, D_PKG_PY
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.files import F_PK_WORKSPACE_PY
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE


# def extract_imports_from_code(code):
#     return {line.strip() for line in code.splitlines()
#             if line.strip().startswith("import ") or line.strip().startswith("from ")}
#
#
# def extract_imports_from_functions(code):
#     imports = set()
#     try:
#         tree = ast.parse(code)
#         for node in ast.walk(tree):
#             if isinstance(node, ast.FunctionDef):
#                 for n in ast.walk(node):
#                     if isinstance(n, (ast.Import, ast.ImportFrom)):
#                         src = ast.get_source_segment(code, n)
#                         if src:
#                             imports.add(src)
#     except Exception:
#         pass
#     return imports
#
#
# def collect_imports_from_dir(directory):
#     all_imports = set()
#     for pyfile in Path(directory).rglob('*.py'):
#         try:
#             code = pyfile.read_text(encoding='utf-8')
#         except UnicodeDecodeError:
#             try:
#                 code = pyfile.read_text(encoding='cp949')
#             except Exception as e:
#                 logging.warning(f"[SKIP] {pyfile} (decode error: {e})")
#                 continue
#         except Exception as e:
#             logging.warning(f"[SKIP] {pyfile} (other error: {e})")
#             continue
#         all_imports |= extract_imports_from_code(code)
#     return all_imports
#
#
# def insert_imports_to_code(code, general_imports, lazy_imports, main_imports):
#     lines = code.splitlines()
#     new_lines = []
#
#     # 1. general import 삽입
#     new_lines.extend(sorted(general_imports))
#     while lines and (lines[0].strip().startswith("import ") or lines[0].strip().startswith("from ")):
#         lines.pop(0)
#     new_lines.extend(lines)
#     code = "\n".join(new_lines)
#
#     # 2. lazy imports
#     if lazy_imports:
#         def insert_lazy_imports(code, lazy_imports):
#             pattern = re.compile(r'(def\s+\w+\s*\(.*?\)\s*:)')
#             return pattern.sub(lambda m: f"{m.group(1)}\n    " + "\n    ".join(sorted(lazy_imports)), code)
#
#         code = insert_lazy_imports(code, lazy_imports)
#
#     # 3. main imports
#     if main_imports:
#         pattern = re.compile(r'(if\s+__name__\s*==\s*[\'"]__main__[\'"]\s*:)')
#         code = pattern.sub(lambda m: f"{m.group(1)}\n    " + "\n    ".join(sorted(main_imports)), code)
#     return code
#
#
# def get_new_code(code, reference_imports):
#     file_imports = extract_imports_from_code(code)
#     func_imports = extract_imports_from_functions(code)
#     general_imports = reference_imports | file_imports
#     lazy_imports = func_imports - general_imports
#     main_imports = general_imports
#     return insert_imports_to_code(code, general_imports, lazy_imports, main_imports)
#
#
# def pk_ensure_modules_imported_proper():
#     while True:
#         func_n = inspect.currentframe().f_code.co_name
#         if LTA:
#             d_working = D_PK_FUNCTIONS_SPLIT
#             d_import_path_reference = D_PROJECT
#             import_location = "lazy_import_location"
#             exec_mode = PkMessages2025.PREVIEW
#         else:
#             d_working = get_values_from_historical_file_routine(
#                 file_id=get_file_id("d_working", func_n),
#                 key_hint='d_working=',
#                 options_default=[get_pnx_os_style(D_WORKSPACE)]
#             )
#             d_import_path_reference = get_values_from_historical_file_routine(
#                 file_id=get_file_id("d_import_path_reference", func_n),
#                 key_hint='d_import_path_reference=',
#                 options_default=[D_PKG_PY]
#             )
#             import_location = get_values_from_historical_file_routine(
#                 file_id=get_file_id("lazy_import_location", func_n),
#                 key_hint='lazy_import_location=',
#                 options_default=["general_import_location", "lazy_import_location"]
#             )
#             exec_mode = get_value_completed(
#                 key_hint=f"{PkMessages2025.MODE}=",
#                 values=[PkMessages2025.PREVIEW, PkMessages2025.EXECUTION]
#             ).strip()
#
#         dry_run = exec_mode == PkMessages2025.PREVIEW
#         d_working = str(Path(d_working).resolve())
#         d_import_path_reference = str(Path(d_import_path_reference).resolve())
#
#         logging.info(f"[{func_n}] mode: {exec_mode}, dry_run: {dry_run}")
#         archive_path = None
#
#         if not dry_run:
#             logging.info("backup_workspace 진입")
#             archive_path = backup_workspace(D_PKG_ARCHIVED, d_working, func_n)
#             logging.info("backup_workspace 종료")
#
#         try:
#             start_time = pk_ensure_start_time_logged()
#             reference_imports = collect_imports_from_dir(d_import_path_reference)
#
#             # 🔥 제외할 디렉토리 설정 (.venv 등)
#             EXCLUDED_DIRS = ['.venv', '__pycache__']
#
#             pyfiles = [
#                 f for f in Path(d_working).rglob('*.py')
#                 if not any(excluded in str(f) for excluded in EXCLUDED_DIRS)
#             ]
#             total_files = len(pyfiles)
#             logging.info(f"[INFO] 파일 수: {total_files}")
#
#             if total_files > 1000:
#                 proceed = input("파일이 1000개를 초과합니다. 계속 진행하시겠습니까? (y/n): ")
#                 if proceed.lower() != 'y':
#                     logging.info("사용자 요청으로 중단")
#                     return
#
#             preview_changes = []
#             for idx, pyfile in enumerate(pyfiles, 1):
#                 logging.info(f"[{idx}/{total_files}] checking: {pyfile}")
#                 try:
#                     code = pyfile.read_text(encoding='utf-8')
#                     new_code = get_new_code(code, reference_imports)
#                     if new_code != code:
#                         preview_changes.append(f"=== {pyfile} ===\n{new_code}\n")
#                 except Exception as e:
#                     logging.warning(f"[IMPORT ORGANIZE FAIL] {pyfile}: {e}")
#
#             if preview_changes:
#                 preview_path = Path(d_working) / "preview_import_changes.txt"
#                 preview_path.write_text("\n\n".join(preview_changes), encoding="utf-8")
#                 logging.info(f"[INFO] preview 저장됨: {preview_path}")
#                 if dry_run or input("위 내용을 실제로 적용하시겠습니까? (y/n): ").lower() != 'y':
#                     logging.info("사용자 요청으로 중단")
#                     return
#
#             # 실제 적용
#             for idx, pyfile in enumerate(pyfiles, 1):
#                 logging.info(f"[{idx}/{total_files}] applying: {pyfile}")
#                 try:
#                     code = pyfile.read_text(encoding='utf-8')
#                     new_code = get_new_code(code, reference_imports)
#                     if new_code != code:
#                         pyfile.write_text(new_code, encoding='utf-8')
#                         logging.info(f"[IMPORT ORGANIZED] {pyfile}")
#                 except Exception as e:
#                     logging.warning(f"[IMPORT ORGANIZE FAIL] {pyfile}: {e}")
#
#             elapsed_time = pk_ensure_elapsed_time_logged(start_time)
#
#         except Exception as e:
#             if archive_path:
#                 logging.error("예외 발생 → 백업 복원 시도")
#                 restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
#             raise
#
#         if not dry_run:
#             decision = get_value_completed(
#                 key_hint=f"{PkMessages2025.AFTER_SERVICE}=",
#                 values=[f"{PkMessages2025.ORIGIN} {PkMessages2025.DELETE}", PkMessages2025.REVERT],
#             )
#             if decision == PkMessages2025.REVERT:
#                 restore_workspace_from_latest_archive(D_PKG_ARCHIVED, d_working)
#
#         logging.info(f"[{func_n}] 완료")
#
#         if LTA:
#             pk_ensure_console_debuggable(ipdb=ipdb)
#         pk_ensure_console_cleared()

def collect_import_lines_from_dir(d_working: str, encoding_list=('utf-8', 'cp949')):
    imports = set()

    for pyfile in Path(d_working).rglob("*.py"):
        try:
            for encoding in encoding_list:
                try:
                    text = pyfile.read_text(encoding=encoding)
                    break
                except Exception:
                    continue
            else:
                continue  # 모든 인코딩 실패

            lines = text.splitlines()
            in_multiline_import = False
            import_block = []

            for line in lines:
                stripped = line.strip()
                if in_multiline_import:
                    import_block.append(stripped)
                    if ')' in stripped:
                        imports.add(" ".join(import_block))
                        in_multiline_import = False
                        import_block = []
                elif stripped.startswith("import ") or stripped.startswith("from "):
                    if stripped.endswith("("):
                        in_multiline_import = True
                        import_block = [stripped]
                    else:
                        imports.add(stripped)

        except Exception as e:
            print(f"[SKIP] {pyfile} - {e}")

    return sorted(imports)


def step1_save_imports_to_txt(func_n, d_working: str):
    imports = collect_import_lines_from_dir(d_working)
    output_path = Path(d_working) / f"{func_n}.txt"
    output_path.write_text("\n".join(imports), encoding="utf-8")
    print(f"[STEP1] import lines saved to: {output_path}")
    return output_path


from pkg_py.functions_split.open_pnx_by_ext import pk_ensure_pnx_opened_by_ext


def step2_open_txt_file_for_editing(f_txt: Path):
    print(f"[STEP2] opening {f_txt} for editing...")
    pk_ensure_pnx_opened_by_ext(str(f_txt))


def step3_confirm_editing_done() -> bool:
    response = get_value_completed(
        key_hint="편집을 완료하셨습니까? (y/n)=",
        values=["y", "n"]
    ).lower()
    return response == "y"


def step4_announce_start_applying():
    print("\n" + "=" * 60)
    print("📌 편집된 import 내용을 기반으로 적용을 시작합니다.")
    print("=" * 60 + "\n")


def step5_backup_f_working(f_working: str, d_backup_target: str) -> str:
    if not os.path.exists(f_working):
        raise FileNotFoundError(f"[ERROR] 파일이 존재하지 않습니다: {f_working}")
    if not os.path.isfile(f_working):
        raise IsADirectoryError(f"[ERROR] 디렉토리가 아닌 파일만 지원합니다: {f_working}")

    # 파일 이름 및 타임스탬프 설정
    base_name = os.path.splitext(os.path.basename(f_working))[0]
    timestamp = datetime.now().strftime("%Y_%m_%d_%H%M")
    archive_basename = os.path.join(d_backup_target, f"{base_name}_{timestamp}")
    archive_output = archive_basename + ".tar.bz2"

    # 임시 디렉토리 생성 및 파일 복사
    temp_dir = os.path.join(d_backup_target, f"__temp_for_backup__{timestamp}")
    os.makedirs(temp_dir, exist_ok=True)
    shutil.copy2(f_working, os.path.join(temp_dir, os.path.basename(f_working)))

    # 압축 수행
    os.makedirs(d_backup_target, exist_ok=True)
    shutil.make_archive(
        base_name=archive_basename,
        format='bztar',
        root_dir=temp_dir,
        base_dir="."
    )

    # 임시 디렉토리 삭제
    shutil.rmtree(temp_dir)

    logging.info(f"[{PkMessages2025.COMPRESSED}] {archive_output}")
    print(f"[STEP5] 📦 백업 완료: {archive_output}")
    return archive_output


def step6_preview_lazy_import_applied_code(code: str, lazy_imports: list[str]) -> str:
    def insert_lazy_imports(code: str, lazy_imports: list[str]) -> str:
        pattern = re.compile(r'(def\s+\w+\s*\(.*?\)\s*:)')

        def replacer(match):
            return f"{match.group(1)}\n    " + "\n    ".join(sorted(lazy_imports))

        return pattern.sub(replacer, code)

    preview_code = insert_lazy_imports(code, lazy_imports)
    return preview_code


def pk_ensure_modules_imported_proper():
    func_n = inspect.currentframe().f_code.co_name

    initialize_and_customize_logging_config(__file__=__file__)
    d_working = D_PKG_PY

    # 1단계: import 수집 및 저장
    f_txt = step1_save_imports_to_txt(d_working=d_working, func_n=func_n)

    # 2단계: txt 자동 열기
    step2_open_txt_file_for_editing(f_txt)

    # 3단계: 편집 완료 여부 확인
    if not step3_confirm_editing_done():
        print("[INFO] 사용자가 편집을 완료하지 않아 작업을 종료합니다.")
        exit(0)

    # 4단계: 적용 시작 안내
    step4_announce_start_applying()

    f_working = F_PK_WORKSPACE_PY
    d_backup_target = D_ARCHIVED
    backup_path = step5_backup_f_working(f_working, d_backup_target)

    # 1. f_working 내용 읽기
    with open(f_working, encoding='utf-8') as f:
        original_code = f.read()

    # 2. lazy import 목록 읽기
    lazy_imports = open(f_txt, encoding='utf-8').read().splitlines()

    # 3. PREVIEW 코드 생성
    preview_code = step6_preview_lazy_import_applied_code(original_code, lazy_imports)

    # 4. PREVIEW 저장 및 열기
    preview_path = f"{os.path.splitext(f_working)[0]}_preview.py"
    with open(preview_path, "w", encoding='utf-8') as f:
        f.write(preview_code)

    print(f"[STEP6] 👀 PREVIEW 저장 완료: {preview_path}")
    pk_ensure_pnx_opened_by_ext(preview_path)


if __name__ == "__main__":
    try:
        pk_ensure_modules_imported_proper()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        pk_ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)

