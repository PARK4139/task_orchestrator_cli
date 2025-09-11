#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ensure_file_found_renewal_simple_v2.py - 수정된 안정 버전

특징:
1. 복잡한 볼륨 발견 없이 직접 경로 스캔
2. 상세한 검색 결과 로깅
3. 탭 자동완성 기반 사용자 인터페이스
4. 테스트 모드 완전 구현
5. UnboundLocalError 문제 해결
"""

import os
import sys
import logging
import time
from pathlib import Path
from typing import Optional, List, Dict, Any

def _get_lazy_imports():
    """지연 import - print 변수 충돌 문제 해결"""
    try:
        import logging
        from sources.functions.ensure_value_completed import ensure_value_completed
        from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI
        return ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI
    except ImportError:
        def ensure_value_completed(key_hint, values):
            print(f"{key_hint}")
            for i, value in enumerate(values, 1):
                print(f"  {i}. {value}")
            choice = input("선택: ").strip()
            try:
                return values[int(choice) - 1]
            except (ValueError, IndexError):
                return choice if choice in values else values[0]
        
        D_TASK_ORCHESTRATOR_CLI_LOGS = Path.cwd() / "logs"
        D_TASK_ORCHESTRATOR_CLI = Path.cwd()
        return ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI

def _setup_logging():
    """로깅 설정"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    D_TASK_ORCHESTRATOR_CLI_LOGS.mkdir(parents=True, exist_ok=True)
    
    log_file = D_TASK_ORCHESTRATOR_CLI_LOGS / "file_search_simple.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )

_setup_logging()

def ensure_file_found_renewal_simple():
    """간단한 대화형 파일 검색"""
    
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("🔍 간단한 파일 검색 시스템")
    print(PK_UNDERLINE)
    
    # 1. 모드 선택
    available_modes = [
        "현재 프로젝트 검색",
        "Downloads 폴더 검색", 
        "전체 C드라이브 검색",
        "사용자 정의 경로 검색",
        "테스트 모드 (안전 검증)",
        "도움말"
    ]
    
    mode = ensure_value_completed(
        key_hint="검색 모드 선택: ",
        values=available_modes
    )
    
    if mode == "도움말":
        _show_simple_help()
        return
    
    # 2. 검색 경로 설정
    if mode == "현재 프로젝트 검색":
        search_path = D_TASK_ORCHESTRATOR_CLI
    elif mode == "Downloads 폴더 검색":
        search_path = Path.home() / "Downloads"
    elif mode == "전체 C드라이브 검색":
        search_path = Path("C:/")
    elif mode == "사용자 정의 경로 검색":
        path_options = [
            str(D_TASK_ORCHESTRATOR_CLI),
            str(Path.home() / "Downloads"),
            str(Path.home() / "Documents"),
            "C:/",
            "D:/",
            "사용자 입력"
        ]
        
        path_choice = ensure_value_completed(
            key_hint="검색할 경로: ",
            values=path_options
        )
        
        if path_choice == "사용자 입력":
            custom_path = input("경로를 입력하세요: ").strip()
            search_path = Path(custom_path)
        else:
            search_path = Path(path_choice)
    else:  # 테스트 모드
        _run_test_mode()
        return
    
    # 3. 검색 방식 선택
    search_methods = [
        "파일명만 검색 (빠름)",
        "파일 내용도 검색 (느림)",
        "fzf 실시간 검색",
        "Everything 사용 (가장 빠름)"
    ]
    
    method = ensure_value_completed(
        key_hint="검색 방식: ",
        values=search_methods
    )
    
    # 4. 검색어 입력
    search_query = ensure_value_completed(
        key_hint="검색어: ",
        values=[
            "ensure_",
            "test_",
            "*.py",
            "*.md", 
            "renewal",
            "file_found",
            "사용자 입력"
        ]
    )
    
    if search_query == "사용자 입력":
        search_query = input("검색어를 입력하세요: ").strip()
    
    if not search_query:
        print("검색어가 없습니다.")
        return
    
    # 5. 검색 실행
    print(f"🔍 검색 시작: '{search_query}' in {search_path}")
    
    start_time = time.time()
    
    if method == "파일명만 검색 (빠름)":
        results = _search_filenames_only(search_path, search_query)
    elif method == "파일 내용도 검색 (느림)":
        results = _search_with_content(search_path, search_query)
    elif method == "fzf 실시간 검색":
        results = _search_with_fzf(search_path, search_query)
    elif method == "Everything 사용 (가장 빠름)":
        results = _search_with_everything(search_query)
    else:
        results = []
    
    end_time = time.time()
    search_duration = end_time - start_time
    
    # 상세 검색 결과 로깅
    logging.info(f"📊 검색 완료 통계:")
    logging.info(f"   검색어: '{search_query}'")
    logging.info(f"   검색 경로: {search_path}")
    logging.info(f"   검색 방식: {method}")
    logging.info(f"   검색 결과: {len(results)}개")
    logging.info(f"   검색 시간: {search_duration:.3f}초")
    
    if results:
        # 결과별 상세 정보 로깅
        total_size = sum(r.get('size', 0) for r in results)
        avg_size = total_size / len(results) if results else 0
        
        logging.info(f"   총 파일 크기: {total_size / (1024*1024):.1f} MB")
        logging.info(f"   평균 파일 크기: {avg_size / 1024:.1f} KB")
        
        # 파일 타입별 통계
        extensions = {}
        for result in results:
            ext = Path(result['path']).suffix.lower()
            extensions[ext] = extensions.get(ext, 0) + 1
        
        logging.info(f"   파일 타입 분포: {dict(sorted(extensions.items(), key=lambda x: x[1], reverse=True))}")
    
    # 사용자에게 결과 표시
    print(f"🎯 검색 완료: {len(results)}개 파일 발견 ({search_duration:.2f}초)")
    
    if not results:
        print("💡 검색 결과가 없습니다. 다른 검색어나 경로를 시도해보세요.")
        return
    
    # 6. 결과 표시 방식 선택
    display_options = [
        "상위 10개만 보기",
        "모든 결과 보기",
        "fzf로 선택하기",
        "파일로 저장하기"
    ]
    
    display_choice = ensure_value_completed(
        key_hint="결과 표시 방식: ",
        values=display_options
    )
    
    if display_choice == "상위 10개만 보기":
        _display_top_results(results[:10])
    elif display_choice == "모든 결과 보기":
        _display_all_results(results)
    elif display_choice == "fzf로 선택하기":
        _display_with_fzf(results)
    elif display_choice == "파일로 저장하기":
        _save_results_to_file(results, search_query)

def _search_filenames_only(search_path: Path, query: str) -> List[Dict[str, Any]]:
    """파일명만 검색"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    results = []
    files_scanned = 0
    
    try:
        for root, dirs, files in os.walk(search_path):
            # 제외할 디렉토리
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'node_modules']]
            
            for file in files:
                files_scanned += 1
                
                # 검색어 매칭 (대소문자 무시)
                if query.lower() in file.lower() or query.lower() in root.lower():
                    file_path = Path(root) / file
                    try:
                        stat = file_path.stat()
                        results.append({
                            'path': str(file_path),
                            'name': file,
                            'size': stat.st_size,
                            'mtime': stat.st_mtime,
                            'dir': root
                        })
                    except Exception:
                        continue
    
    except Exception as e:
        logging.error(f"Filename search failed: {e}")
    
    logging.info(f"파일명 검색: {files_scanned}개 파일 스캔, {len(results)}개 매칭")
    return results

def _search_with_content(search_path: Path, query: str) -> List[Dict[str, Any]]:
    """파일 내용 포함 검색"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    results = []
    files_scanned = 0
    content_matches = 0
    
    text_extensions = ['.py', '.txt', '.md', '.json', '.yaml', '.yml', '.toml', '.cfg', '.ini', '.log']
    
    try:
        for root, dirs, files in os.walk(search_path):
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'node_modules']]
            
            for file in files:
                files_scanned += 1
                file_path = Path(root) / file
                
                # 파일명 매칭
                name_match = query.lower() in file.lower() or query.lower() in root.lower()
                content_match = False
                
                # 텍스트 파일인 경우 내용도 검색
                if file_path.suffix.lower() in text_extensions:
                    try:
                        if file_path.stat().st_size < 1024 * 1024:  # 1MB 미만 파일만
                            content = file_path.read_text(encoding='utf-8', errors='ignore')
                            if query.lower() in content.lower():
                                content_match = True
                                content_matches += 1
                    except Exception:
                        pass
                
                if name_match or content_match:
                    try:
                        stat = file_path.stat()
                        results.append({
                            'path': str(file_path),
                            'name': file,
                            'size': stat.st_size,
                            'mtime': stat.st_mtime,
                            'dir': root,
                            'match_type': 'content' if content_match else 'filename'
                        })
                    except Exception:
                        continue
    
    except Exception as e:
        logging.error(f"Content search failed: {e}")
    
    logging.info(f"내용 검색: {files_scanned}개 파일 스캔, {content_matches}개 내용 매칭, 총 {len(results)}개 결과")
    return results

def _search_with_fzf(search_path: Path, query: str) -> List[Dict[str, Any]]:
    """fzf를 사용한 실시간 검색"""
    import subprocess
    
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("📁 파일 목록 생성 중...")
    
    # 파일 목록 생성
    files = []
    for root, dirs, filenames in os.walk(search_path):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv']]
        
        for filename in filenames:
            file_path = Path(root) / filename
            try:
                stat = file_path.stat()
                size_kb = stat.st_size / 1024
                mtime_str = time.strftime('%Y-%m-%d %H:%M', time.localtime(stat.st_mtime))
                files.append(f"{file_path}\t{size_kb:.1f}KB\t{mtime_str}")
            except Exception:
                continue
    
    if not files:
        print("검색할 파일이 없습니다.")
        return []
    
    fzf_input = '\n'.join(files)
    
    # fzf 실행
    fzf_cmd = [
        'fzf',
        '--delimiter', '\t',
        '--with-nth', '1',
        '--preview', 'head -10 {1} 2>/dev/null || file {1}',
        '--preview-window', 'right:50%:wrap',
        '--query', query,  # 초기 검색어 설정
        '--header', f'검색: {search_path} | CTRL-C: 취소',
        '--height', '80%',
        '--layout', 'reverse',
        '--prompt', '🔍 파일 선택: '
    ]
    
    try:
        result = subprocess.run(fzf_cmd, input=fzf_input, text=True, capture_output=True)
        
        if result.returncode == 0 and result.stdout.strip():
            selected_files = result.stdout.strip().split('\n')
            
            results = []
            for file_line in selected_files:
                file_path = file_line.split('\t')[0]
                try:
                    stat = Path(file_path).stat()
                    results.append({
                        'path': file_path,
                        'name': Path(file_path).name,
                        'size': stat.st_size,
                        'mtime': stat.st_mtime,
                        'dir': str(Path(file_path).parent)
                    })
                except Exception:
                    continue
            
            logging.info(f"fzf 검색: {len(files)}개 파일 중 {len(results)}개 선택")
            return results
        else:
            logging.info("fzf 검색: 선택 취소")
            return []
            
    except FileNotFoundError:
        print("❌ fzf를 찾을 수 없습니다.")
        print("💡 설치: choco install fzf (Windows) 또는 sudo apt install fzf (Linux)")
        return []
    except Exception as e:
        logging.error(f"fzf search failed: {e}")
        return []

def _search_with_everything(query: str) -> List[Dict[str, Any]]:
    """Everything을 사용한 검색"""
    import subprocess
    
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    # Everything 경로 확인
    everything_paths = [
        r"C:\Program Files\Everything\Everything.exe",
        r"C:\Program Files (x86)\Everything\Everything.exe"
    ]
    
    everything_exe = None
    for path in everything_paths:
        if os.path.exists(path):
            everything_exe = path
            break
    
    if not everything_exe:
        print("❌ Everything을 찾을 수 없습니다.")
        return []
    
    try:
        # Everything 명령줄 검색
        cmd = f'"{everything_exe}" -s "{query}" -a -f -sort -no-gui'
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=30,
            creationflags=subprocess.CREATE_NO_WINDOW
        )
        
        if result.returncode == 0 and result.stdout.strip():
            file_paths = result.stdout.strip().split('\n')
            
            results = []
            for file_path in file_paths:
                try:
                    path_obj = Path(file_path)
                    if path_obj.exists():
                        stat = path_obj.stat()
                        results.append({
                            'path': file_path,
                            'name': path_obj.name,
                            'size': stat.st_size,
                            'mtime': stat.st_mtime,
                            'dir': str(path_obj.parent)
                        })
                except Exception:
                    continue
            
            logging.info(f"Everything 검색: {len(file_paths)}개 경로 중 {len(results)}개 유효한 파일")
            return results
        else:
            logging.info("Everything 검색: 결과 없음")
            return []
            
    except Exception as e:
        logging.error(f"Everything search failed: {e}")
        return []

def _run_test_mode():
    """테스트 모드 실행"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("🧪 테스트 모드 시작")
    print("=" * 40)
    
    test_options = [
        "검색 알고리즘 성능 테스트",
        "fzf 인터페이스 테스트",
        "파일 타입별 검색 테스트",
        "대용량 디렉토리 테스트",
        "오류 처리 테스트"
    ]
    
    test_choice = ensure_value_completed(
        key_hint="테스트 종류: ",
        values=test_options
    )
    
    if test_choice == "검색 알고리즘 성능 테스트":
        _test_search_performance()
    elif test_choice == "fzf 인터페이스 테스트":
        _test_fzf_interface()
    elif test_choice == "파일 타입별 검색 테스트":
        _test_file_type_search()
    elif test_choice == "대용량 디렉토리 테스트":
        _test_large_directory()
    elif test_choice == "오류 처리 테스트":
        _test_error_handling()

def _test_search_performance():
    """검색 성능 테스트"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("⚡ 검색 성능 테스트")
    
    test_queries = ["ensure_", "test_", "*.py", "file", "renewal"]
    test_path = D_TASK_ORCHESTRATOR_CLI
    
    for query in test_queries:
        print(f"\n🔍 테스트 검색어: '{query}'")
        
        # 성능 측정
        start_time = time.time()
        results = _search_filenames_only(test_path, query)
        end_time = time.time()
        
        duration = end_time - start_time
        rate = len(results) / (duration + 1e-9)
        
        print(f"   결과: {len(results)}개")
        print(f"   시간: {duration:.3f}초")
        print(f"   속도: {rate:.0f} results/sec")
        
        # 성능 평가
        if duration < 0.1:
            print("   평가: 🚀 매우 빠름")
        elif duration < 1.0:
            print("   평가: ⚡ 빠름")
        elif duration < 5.0:
            print("   평가: 🐌 보통")
        else:
            print("   평가: 🐢 느림")

def _test_fzf_interface():
    """fzf 인터페이스 테스트"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("🎨 fzf 인터페이스 테스트")
    
    # 테스트 데이터 생성
    test_files = []
    for py_file in (D_TASK_ORCHESTRATOR_CLI / "resources" / "functions").glob("*.py"):
        test_files.append(str(py_file))
    
    if test_files:
        results = _search_with_fzf(D_TASK_ORCHESTRATOR_CLI, "ensure_")
        print(f"✅ fzf 테스트 완료: {len(results)}개 선택")
    else:
        print("❌ 테스트할 파일이 없습니다.")

def _display_top_results(results: List[Dict[str, Any]]):
    """상위 결과 표시"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    for i, result in enumerate(results, 1):
        size_mb = result['size'] / (1024 * 1024)
        mtime_str = time.strftime('%Y-%m-%d %H:%M', time.localtime(result['mtime']))
        
        print(f"{i:2d}. {result['name']}")
        print(f"    📁 {result['dir']}")
        print(f"    📊 {size_mb:.1f}MB, {mtime_str}")

def _display_with_fzf(results: List[Dict[str, Any]]):
    """fzf로 결과 표시"""
    import subprocess
    
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    if not results:
        return
    
    # fzf 입력 데이터 준비
    fzf_lines = []
    for result in results:
        size_mb = result['size'] / (1024 * 1024)
        mtime_str = time.strftime('%Y-%m-%d %H:%M', time.localtime(result['mtime']))
        fzf_lines.append(f"{result['path']}\t{size_mb:.1f}MB\t{mtime_str}")
    
    fzf_input = '\n'.join(fzf_lines)
    
    try:
        subprocess.run([
            'fzf',
            '--delimiter', '\t',
            '--with-nth', '1',
            '--preview', 'head -20 {1} 2>/dev/null || file {1}',
            '--header', f'검색 결과: {len(results)}개 파일',
            '--height', '80%'
        ], input=fzf_input, text=True)
        
    except FileNotFoundError:
        print("❌ fzf를 찾을 수 없습니다.")
    except Exception as e:
        print(f"❌ fzf 실행 오류: {e}")

def _save_results_to_file(results: List[Dict[str, Any]], query: str):
    """검색 결과를 파일로 저장"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    filename = D_TASK_ORCHESTRATOR_CLI_LOGS / f"search_results_{query.replace('*', 'star')}_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"검색 결과: '{query}'\n")
            f.write(f"검색 시간: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"총 결과: {len(results)}개\n")
            f.write("=" * 80 + "\n\n")
            
            for i, result in enumerate(results, 1):
                size_mb = result['size'] / (1024 * 1024)
                mtime_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result['mtime']))
                
                f.write(f"{i:4d}. {result['name']}\n")
                f.write(f"       경로: {result['path']}\n")
                f.write(f"       크기: {size_mb:.1f}MB\n")
                f.write(f"       수정: {mtime_str}\n")
                if 'match_type' in result:
                    f.write(f"       매칭: {result['match_type']}\n")
                f.write("\n")
        
        print(f"✅ 검색 결과가 저장되었습니다: {filename}")
        logging.info(f"Search results saved to: {filename}")
        
    except Exception as e:
        print(f"❌ 파일 저장 실패: {e}")

def _test_file_type_search():
    """파일 타입별 검색 테스트"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("📄 파일 타입별 검색 테스트")
    
    test_extensions = ["*.py", "*.md", "*.json", "*.toml", "*.txt"]
    
    for ext in test_extensions:
        print(f"\n🔍 테스트: {ext}")
        start_time = time.time()
        results = _search_filenames_only(D_TASK_ORCHESTRATOR_CLI, ext.replace('*', ''))
        duration = time.time() - start_time
        print(f"   결과: {len(results)}개 파일 ({duration:.3f}초)")

def _test_large_directory():
    """대용량 디렉토리 테스트"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("🗂️ 대용량 디렉토리 테스트")
    
    large_paths = [
        Path("C:/Windows"),
        Path("C:/Program Files"),
        Path.home() / "Downloads"
    ]
    
    for path in large_paths:
        if path.exists():
            print(f"\n📁 테스트 경로: {path}")
            start_time = time.time()
            
            # 제한된 검색 (안전성을 위해)
            file_count = 0
            try:
                for root, dirs, files in os.walk(path):
                    dirs[:] = dirs[:5]  # 최대 5개 하위 디렉토리만
                    file_count += len(files)
                    if file_count > 10000:  # 10000개 파일 제한
                        break
            except Exception as e:
                print(f"   오류: {e}")
                continue
            
            duration = time.time() - start_time
            print(f"   스캔된 파일: {file_count}개")
            print(f"   소요 시간: {duration:.3f}초")
            print(f"   처리 속도: {file_count/(duration+1e-9):.0f} files/sec")

def _test_error_handling():
    """오류 처리 테스트"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    print("⚠️ 오류 처리 테스트")
    
    # 1. 존재하지 않는 경로 테스트
    print("\n1. 존재하지 않는 경로 테스트")
    fake_path = Path("C:/NonExistentDirectory123456")
    results = _search_filenames_only(fake_path, "test")
    print(f"   결과: {len(results)}개 (예상: 0개)")
    
    # 2. 권한 없는 경로 테스트
    print("\n2. 권한 제한 경로 테스트")
    restricted_path = Path("C:/System Volume Information")
    if restricted_path.exists():
        results = _search_filenames_only(restricted_path, "test")
        print(f"   결과: {len(results)}개")
    else:
        print("   해당 경로가 존재하지 않음")
    
    # 3. 빈 검색어 테스트
    print("\n3. 빈 검색어 테스트")
    results = _search_filenames_only(D_TASK_ORCHESTRATOR_CLI, "")
    print(f"   결과: {len(results)}개")

def _display_all_results(results: List[Dict[str, Any]]):
    """모든 결과 표시"""
    _display_top_results(results)

def _show_simple_help():
    """간단한 도움말"""
    ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    help_text = """
🔍 간단한 파일 검색 시스템

🚀 사용법:
  1. 검색 모드 선택 (탭으로 자동완성)
  2. 검색 방식 선택
  3. 검색어 입력
  4. 결과 확인

📁 검색 모드:
  - 현재 프로젝트: 빠르고 정확
  - Downloads: 다운로드 파일 검색
  - C드라이브: 전체 시스템 검색
  - 사용자 정의: 원하는 경로 지정

🔍 검색 방식:
  - 파일명만: 가장 빠름
  - 내용 포함: 정확하지만 느림
  - fzf 실시간: 대화형 검색
  - Everything: 시스템 전체 초고속

🧪 테스트 모드:
  - 안전한 기능 검증
  - 실제 시스템 영향 없음
  - 성능 측정 및 벤치마킹
"""
    
    print(help_text)

if __name__ == "__main__":
    ensure_file_found_renewal_simple()
