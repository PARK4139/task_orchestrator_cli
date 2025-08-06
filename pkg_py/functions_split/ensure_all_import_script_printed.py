import os
import inspect
from pathlib import Path
from collections import defaultdict, Counter
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.functions_split.get_modules_from_file import get_modules_from_file
from pkg_py.functions_split.ensure_modules_saved_from_file import ensure_modules_saved_from_file
from pkg_py.refactor.pk_ensure_modules_imported_proper import collect_import_lines_from_dir
from pkg_py.functions_split.get_pnxs_from_d_working import get_pnxs_from_d_working
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.system_object.directories import D_PKG_PY, D_PKG_CACHE_PRIVATE
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025


@ensure_seconds_measured
def ensure_all_import_script_printed(target_directory=None, show_statistics=True, group_by_type=True, save_to_file=True):
    """
    프로젝트 내의 모든 Python 파일에서 import 문들을 스캔하여 출력하는 함수
    기존 함수들을 활용하여 개선된 버전
    
    Args:
        target_directory: 스캔할 디렉토리 경로 (None이면 pkg_py 디렉토리)
        show_statistics: 통계 정보 출력 여부
        group_by_type: import 유형별로 그룹화하여 출력할지 여부  
        save_to_file: 결과를 파일로 저장할지 여부
    """
    func_n = inspect.currentframe().f_code.co_name
    
    # 기본 디렉토리 설정 - 기존 패턴 활용
    if target_directory is None:
        target_directory = D_PKG_PY
    else:
        target_directory = Path(target_directory)
    
    ensure_printed(f"[{PkMessages2025.IMPORT_SCRIPT_START}] {PK_ANSI_COLOR_MAP['CYAN']}함수명={func_n} {PK_ANSI_COLOR_MAP['RESET']}", print_color='cyan')
    ensure_printed(f" 스캔 디렉토리: {target_directory}", print_color='green')
    
    # 모드 선택 - 기존 패턴 활용
    if LTA:
        decision = "directory_scan_mode"
    else:
        decision = get_value_completed(
            key_hint=f"{PkMessages2025.MODE}=", 
            values=["directory_scan_mode", "file_by_file_mode", "single_file_mode"]
        )
    
    all_imports = []
    import_by_file = defaultdict(list)
    
    if decision == "directory_scan_mode":
        # 기존 collect_import_lines_from_dir 함수 활용
        ensure_printed(" 디렉토리 전체 스캔 모드", print_color='yellow')
        all_imports = collect_import_lines_from_dir(str(target_directory))
        
        # 파일별 세부 정보도 수집
        for py_file in Path(target_directory).rglob('*.py'):
            if should_skip_file(py_file):
                continue
            try:
                file_imports = get_modules_from_file(str(py_file))
                import_by_file[str(py_file)] = file_imports
            except Exception as e:
                ensure_printed(f"[{PkMessages2025.IMPORT_FILE_READ_ERROR}] {PK_ANSI_COLOR_MAP['RED']}파일={py_file} 오류={str(e)} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
                
    elif decision == "file_by_file_mode":
        # 각 파일을 개별적으로 처리 - 기존 패턴 활용
        ensure_printed(" 파일별 개별 처리 모드", print_color='yellow')
        pnxs = get_pnxs_from_d_working(d_working=str(target_directory))
        
        for pnx in pnxs:
            if is_f(pnx) and pnx.endswith('.py'):
                if should_skip_file(Path(pnx)):
                    continue
                    
                ensure_printed(f" 처리 중: {pnx}", print_color='white')
                try:
                    file_imports = get_modules_from_file(pnx)
                    import_by_file[pnx] = file_imports
                    all_imports.extend(file_imports)
                    
                    if save_to_file:
                        # 개별 파일의 import를 저장 - 기존 함수 활용
                        save_file = ensure_modules_saved_from_file(pnx)
                        ensure_printed(f" 저장됨: {save_file}", print_color='green')
                        
                except Exception as e:
                    ensure_printed(f"[{PkMessages2025.IMPORT_FILE_PROCESS_ERROR}] {PK_ANSI_COLOR_MAP['RED']}파일={pnx} 오류={str(e)} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
                    
    elif decision == "single_file_mode":
        # 단일 파일 모드
        ensure_printed(" 단일 파일 분석 모드", print_color='yellow')
        from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
        from pkg_py.functions_split.get_file_id import get_file_id
        
        key_name = 'target_file'
        file_id = get_file_id(key_name, func_n)
        target_file = get_value_via_fzf_or_history_routine(
            key_name=key_name, 
            file_id=file_id, 
            init_options=[str(target_directory)],
            editable=True
        )
        
        if is_f(target_file) and target_file.endswith('.py'):
            file_imports = get_modules_from_file(target_file)
            import_by_file[target_file] = file_imports
            all_imports = file_imports
            
            if save_to_file:
                save_file = ensure_modules_saved_from_file(target_file)
                ensure_pnx_opened_by_ext(save_file)
    
    # 통계 분석 및 분류
    standard_imports, third_party_imports, local_imports = classify_imports(all_imports)
    
    # 결과 출력
    print_analysis_results(
        all_imports, standard_imports, third_party_imports, local_imports,
        import_by_file, target_directory, show_statistics, group_by_type
    )
    
    # 전체 결과 파일로 저장
    if save_to_file and all_imports:
        save_all_imports_to_file(func_n, all_imports, standard_imports, third_party_imports, local_imports)
    
    ensure_printed(f"\n[{PkMessages2025.IMPORT_SCRIPT_COMPLETE}] {PK_ANSI_COLOR_MAP['CYAN']}함수명={func_n} {PK_ANSI_COLOR_MAP['RESET']}", print_color='cyan')


def should_skip_file(py_file):
    """건너뛸 파일 판별"""
    skip_patterns = ['__pycache__', '.git', '.venv', 'venv', 'node_modules', '.pytest_cache']
    return any(pattern in str(py_file) for pattern in skip_patterns)


def classify_imports(all_imports):
    """import를 유형별로 분류"""
    standard_imports = set()
    third_party_imports = set()  
    local_imports = set()
    
    # Python 표준 라이브러리 목록 확장
    standard_libs = {
        'os', 'sys', 'time', 'json', 'sqlite3', 'subprocess', 'threading', 'datetime',
        'random', 'math', 'hashlib', 'inspect', 'importlib', 're', 'string', 'pathlib',
        'collections', 'functools', 'itertools', 'base64', 'urllib', 'traceback',
        'pickle', 'csv', 'zipfile', 'shutil', 'tempfile', 'uuid', 'timeit', 'logging',
        'argparse', 'configparser', 'email', 'html', 'http', 'xml', 'socket', 'ssl',
        'asyncio', 'concurrent', 'multiprocessing', 'queue', 'weakref', 'copy', 
        'operator', 'typing', 'enum', 'dataclasses', 'contextlib', 'abc'
    }
    
    for imp in all_imports:
        # 모듈명 추출 개선
        if imp.startswith('from '):
            # "from module import something" 형태
            parts = imp.split()
            if len(parts) >= 2:
                module_name = parts[1].split('.')[0]
            else:
                continue
        elif imp.startswith('import '):
            # "import module" 형태  
            parts = imp.split()
            if len(parts) >= 2:
                module_name = parts[1].split('.')[0].split(' as ')[0]
            else:
                continue
        else:
            continue
            
        # 분류
        if module_name.startswith('pkg_py') or module_name.startswith('.'):
            local_imports.add(imp)
        elif module_name in standard_libs:
            standard_imports.add(imp)
        else:
            third_party_imports.add(imp)
    
    return standard_imports, third_party_imports, local_imports


def print_analysis_results(all_imports, standard_imports, third_party_imports, local_imports,
                         import_by_file, target_directory, show_statistics, group_by_type):
    """분석 결과 출력"""
    ensure_printed("=" * 80, print_color='cyan')
    ensure_printed(" 전체 IMPORT 스크립트 분석 결과", print_color='cyan') 
    ensure_printed("=" * 80, print_color='cyan')
    
    if show_statistics:
        print_import_statistics(all_imports, standard_imports, third_party_imports, local_imports)
    
    if group_by_type:
        print_imports_by_type(standard_imports, third_party_imports, local_imports)
    else:
        print_all_imports_sorted(all_imports)
    
    # 파일별 import 정보 (요약) - 기존 패턴 활용
    if import_by_file:
        ensure_printed("\n" + "=" * 80, print_color='cyan')
        ensure_printed(" 파일별 IMPORT 개수 TOP 10", print_color='cyan')  
        ensure_printed("=" * 80, print_color='cyan')
        
        file_import_counts = [(len(imports), file) for file, imports in import_by_file.items()]
        file_import_counts.sort(reverse=True)
        
        for i, (count, file) in enumerate(file_import_counts[:10]):
            try:
                relative_path = Path(file).relative_to(target_directory)
                ensure_printed(f"{i+1:2d}. {count:3d}개 - {relative_path}", print_color='green')
            except ValueError:
                # relative_to 실패시 절대 경로 표시
                ensure_printed(f"{i+1:2d}. {count:3d}개 - {Path(file).name}", print_color='green')


def save_all_imports_to_file(func_n, all_imports, standard_imports, third_party_imports, local_imports):
    """전체 import 결과를 파일로 저장 - 기존 패턴 활용"""
    save_file = os.path.join(D_PKG_CACHE_PRIVATE, f"{func_n}_full_analysis.txt")
    
    content_lines = []
    content_lines.append("=" * 80)
    content_lines.append(" 전체 IMPORT 스크립트 분석 결과")
    content_lines.append("=" * 80)
    content_lines.append("")
    
    # 통계 정보
    content_lines.append(f"전체 import 문 수: {len(all_imports):,}개")
    content_lines.append(f"고유 import 문 수: {len(set(all_imports)):,}개") 
    content_lines.append(f"표준 라이브러리: {len(standard_imports):,}개")
    content_lines.append(f"서드파티 라이브러리: {len(third_party_imports):,}개")
    content_lines.append(f"로컬 모듈: {len(local_imports):,}개")
    content_lines.append("")
    
    # 유형별 분류
    if standard_imports:
        content_lines.append(f" 표준 라이브러리 ({len(standard_imports)}개)")
        content_lines.append("-" * 50)
        for imp in sorted(standard_imports):
            content_lines.append(f"  {imp}")
        content_lines.append("")
    
    if third_party_imports:
        content_lines.append(f" 서드파티 라이브러리 ({len(third_party_imports)}개)")
        content_lines.append("-" * 50)
        for imp in sorted(third_party_imports):
            content_lines.append(f"  {imp}")
        content_lines.append("")
    
    if local_imports:
        content_lines.append(f" 로컬 모듈 ({len(local_imports)}개)")
        content_lines.append("-" * 50)
        for imp in sorted(local_imports):
            content_lines.append(f"  {imp}")
        content_lines.append("")
    
    # 기존 함수 활용하여 파일 저장
    ensure_list_written_to_f(content_lines, save_file, mode="w")
    ensure_printed(f" 전체 분석 결과 저장: {save_file}", print_color='cyan')
    
    return save_file


def print_import_statistics(all_imports, standard_imports, third_party_imports, local_imports):
    """import 통계 정보 출력"""
    ensure_printed("\n IMPORT 통계", print_color='yellow')
    ensure_printed("-" * 40, print_color='yellow')
    
    total_count = len(all_imports)
    unique_count = len(set(all_imports))
    
    ensure_printed(f"전체 import 문 수: {total_count:,}개", print_color='white')
    ensure_printed(f"고유 import 문 수: {unique_count:,}개", print_color='white')
    ensure_printed(f"표준 라이브러리: {len(standard_imports):,}개", print_color='blue')
    ensure_printed(f"서드파티 라이브러리: {len(third_party_imports):,}개", print_color='magenta')
    ensure_printed(f"로컬 모듈: {len(local_imports):,}개", print_color='green')
    
    # 가장 많이 사용된 import 문 TOP 10
    if all_imports:
        import_counter = Counter(all_imports)
        ensure_printed(f"\n 가장 많이 사용된 IMPORT TOP 10", print_color='red')
        ensure_printed("-" * 50, print_color='red')
        
        for i, (imp, count) in enumerate(import_counter.most_common(10)):
            ensure_printed(f"{i+1:2d}. {count:3d}회 - {imp}", print_color='white')


def print_imports_by_type(standard_imports, third_party_imports, local_imports):
    """import를 유형별로 분류하여 출력"""
    
    # 표준 라이브러리
    if standard_imports:
        ensure_printed(f"\n 표준 라이브러리 ({len(standard_imports)}개)", print_color='blue')
        ensure_printed("-" * 50, print_color='blue')
        for imp in sorted(standard_imports):
            ensure_printed(f"  {imp}", print_color='white')
    
    # 서드파티 라이브러리
    if third_party_imports:
        ensure_printed(f"\n 서드파티 라이브러리 ({len(third_party_imports)}개)", print_color='magenta')
        ensure_printed("-" * 50, print_color='magenta')
        for imp in sorted(third_party_imports):
            ensure_printed(f"  {imp}", print_color='white')
    
    # 로컬 모듈
    if local_imports:
        ensure_printed(f"\n 로컬 모듈 ({len(local_imports)}개)", print_color='green')
        ensure_printed("-" * 50, print_color='green')
        for imp in sorted(local_imports):
            ensure_printed(f"  {imp}", print_color='white')


def print_all_imports_sorted(all_imports):
    """모든 import를 정렬하여 출력"""
    unique_imports = sorted(set(all_imports))
    
    ensure_printed(f"\n 전체 고유 IMPORT 목록 ({len(unique_imports)}개)", print_color='cyan')
    ensure_printed("-" * 60, print_color='cyan')
    
    for imp in unique_imports:
        ensure_printed(f"  {imp}", print_color='white')


if __name__ == "__main__":
    # 테스트 실행
    ensure_all_import_script_printed()


