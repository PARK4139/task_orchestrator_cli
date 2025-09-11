#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ensure_file_found_simple_clean.py - 간단하고 깔끔한 파일 검색

특징:
1. 테스트 모드 제거 (불필요)
2. 상세한 검색 결과 로깅
3. 탭 자동완성 기반 사용자 인터페이스
4. 실용적이고 직관적인 기능만 포함
"""

import os
import sys
import logging
import time
from pathlib import Path
from typing import List, Dict, Any

def _get_lazy_imports():
    """지연 import"""
    try:
        import logging
        from sources.functions.ensure_value_completed import ensure_value_completed
        from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI
        return print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI
    except ImportError:
        def print(msg):
            print(msg)
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
        return print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI

def _setup_logging():
    """로깅 설정"""
    d_logs = _get_lazy_imports()[2]  # D_TASK_ORCHESTRATOR_CLI_LOGS
    d_logs.mkdir(parents=True, exist_ok=True)
    
    log_file = d_logs / "file_search_clean.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )

_setup_logging()

def ensure_file_found_simple_clean():
    """간단하고 깔끔한 파일 검색"""
    
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    logging.debug("🔍 파일 검색 시스템")
    logging.debug("=" * 40)
    
    # 1. 검색 경로 선택
    path_options = [
        f"현재 프로젝트 ({D_TASK_ORCHESTRATOR_CLI.nick_name})",
        "Downloads 폴더",
        "전체 C드라이브",
        "전체 D드라이브",
        "사용자 정의 경로",
        "도움말"
    ]
    
    path_choice = ensure_value_completed(
        key_hint="검색 경로: ",
        values=path_options
    )
    
    if path_choice == "도움말":
        _show_help()
        return
    
    # 검색 경로 설정
    if "현재 프로젝트" in path_choice:
        search_path = D_TASK_ORCHESTRATOR_CLI
    elif path_choice == "Downloads 폴더":
        search_path = Path.home() / "Downloads"
    elif path_choice == "전체 C드라이브":
        search_path = Path("C:/")
    elif path_choice == "전체 D드라이브":
        search_path = Path("D:/")
    elif path_choice == "사용자 정의 경로":
        custom_path = input("경로를 입력하세요: ").strip()
        search_path = Path(custom_path)
    
    if not search_path.exists():
        logging.debug(f"❌ 경로가 존재하지 않습니다: {search_path}")
        return
    
    # 2. 검색 방식 선택
    search_methods = [
        "파일명 검색 (빠름)",
        "파일 내용 포함 검색 (정확)",
        "fzf 실시간 검색 (대화형)",
        "Everything 검색 (초고속)"
    ]
    
    method = ensure_value_completed(
        key_hint="검색 방식: ",
        values=search_methods
    )
    
    # 3. 검색어 입력
    query_options = [
        "ensure_",
        "test_",
        "*.py",
        "*.md",
        "*.txt", 
        "renewal",
        "file_found",
        "task_orchestrator_cli",
        "사용자 입력"
    ]
    
    query = ensure_value_completed(
        key_hint="검색어: ",
        values=query_options
    )
    
    if query == "사용자 입력":
        query = input("검색어를 입력하세요: ").strip()
    
    if not query:
        logging.debug("검색어가 없습니다.")
        return
    
    # 4. 검색 실행
    logging.debug(f"🔍 검색 시작: '{query}' in {search_path}")
    
    start_time = time.time()
    
    if "파일명 검색" in method:
        results = _search_filenames(search_path, query)
    elif "내용 포함" in method:
        results = _search_with_content(search_path, query)
    elif "fzf" in method:
        results = _search_with_fzf(search_path, query)
    elif "Everything" in method:
        results = _search_with_everything(query)
    else:
        results = []
    
    end_time = time.time()
    search_duration = end_time - start_time
    
    # 5. 상세 검색 결과 로깅 (요청된 기능)
    _log_search_results(query, search_path, method, results, search_duration)
    
    # 6. 결과 표시 방식 선택
    if results:
        display_options = [
            "상위 10개만 보기",
            "모든 결과 보기",
            "fzf로 선택하기",
            "파일로 저장하기"
        ]
        
        display_choice = ensure_value_completed(
            key_hint="결과 표시: ",
            values=display_options
        )
        
        _display_results(results, display_choice, query)
    else:
        logging.debug("💡 검색 결과가 없습니다. 다른 검색어나 경로를 시도해보세요.")

def _log_search_results(query: str, search_path: Path, method: str, results: List[Dict[str, Any]], duration: float):
    """상세한 검색 결과 로깅 (요청된 기능)"""
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    # 기본 통계
    logging.info(f"📊 검색 완료 통계:")
    logging.info(f"   검색어: '{query}'")
    logging.info(f"   검색 경로: {search_path}")
    logging.info(f"   검색 방식: {method}")
    logging.info(f"   검색 결과: {len(results)}개")
    logging.info(f"   검색 시간: {duration:.3f}초")
    
    if duration > 0:
        search_rate = len(results) / duration
        logging.info(f"   검색 속도: {search_rate:.0f} results/sec")
    
    # 사용자에게도 표시
    logging.debug(f"🎯 검색 완료: '{query}'")
    logging.debug(f"📊 {len(results)}개 파일 발견 ({duration:.2f}초)")
    
    if results:
        # 파일 크기 통계
        total_size = sum(r.get('size', 0) for r in results)
        avg_size = total_size / len(results) if results else 0
        
        logging.info(f"   총 파일 크기: {total_size / (1024*1024):.1f} MB")
        logging.info(f"   평균 파일 크기: {avg_size / 1024:.1f} KB")
        
        # 파일 타입 분포
        extensions = {}
        for result in results:
            ext = Path(result['path']).suffix.lower()
            extensions[ext] = extensions.get(ext, 0) + 1
        
        logging.info(f"   파일 타입 분포: {dict(sorted(extensions.items(), key=lambda x: x[1], reverse=True))}")
        
        # 사용자에게 요약 표시
        logging.debug(f"📁 파일 타입: {len(extensions)}종류")
        logging.debug(f"💾 총 크기: {total_size / (1024*1024):.1f} MB")
        
        if duration > 0:
            logging.debug(f"⚡ 속도: {len(results)/duration:.0f} results/sec")
    
    else:
        logging.debug("💡 검색 팁:")
        logging.debug("  - 와일드카드: *.py, test_*, *config*")
        logging.debug("  - 부분 단어: file, found, renewal")
        logging.debug("  - 경로 포함: Downloads, task_orchestrator_cli")

def _search_filenames(search_path: Path, query: str) -> List[Dict[str, Any]]:
    """파일명 검색"""
    results = []
    files_scanned = 0
    
    try:
        for root, dirs, files in os.walk(search_path):
            # 시스템 디렉토리 제외
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'node_modules']]
            
            for file in files:
                files_scanned += 1
                
                # 검색 매칭
                match_found = False
                
                if query.startswith('*.'):
                    # 확장자 검색
                    extension = query[1:]
                    if file.endswith(extension):
                        match_found = True
                else:
                    # 텍스트 검색 (대소문자 무시)
                    if query.lower() in file.lower() or query.lower() in root.lower():
                        match_found = True
                
                if match_found:
                    try:
                        file_path = Path(root) / file
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
        logging.error(f"파일명 검색 오류: {e}")
    
    logging.info(f"파일명 검색: {files_scanned}개 파일 스캔, {len(results)}개 매칭")
    return results

def _search_with_content(search_path: Path, query: str) -> List[Dict[str, Any]]:
    """파일 내용 포함 검색"""
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
                        if file_path.stat().st_size < 1024 * 1024:  # 1MB 미만만
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
        logging.error(f"내용 검색 오류: {e}")
    
    logging.info(f"내용 검색: {files_scanned}개 파일 스캔, {content_matches}개 내용 매칭, 총 {len(results)}개 결과")
    return results

def _search_with_fzf(search_path: Path, query: str) -> List[Dict[str, Any]]:
    """fzf 실시간 검색"""
    import subprocess
    
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    logging.debug("📁 파일 목록 생성 중...")
    
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
        logging.debug("검색할 파일이 없습니다.")
        return []
    
    fzf_input = '\n'.join(files)
    
    # fzf 실행
    fzf_cmd = [
        'fzf',
        '--delimiter', '\t',
        '--with-nth', '1',
        '--preview', 'head -10 {1} 2>/dev/null || file {1}',
        '--preview-window', 'right:50%:wrap',
        '--query', query,
        '--header', f'검색: {search_path} | Enter: 선택, ESC: 취소',
        '--height', '80%',
        '--layout', 'reverse',
        '--prompt', '🔍 '
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
        logging.debug("❌ fzf를 찾을 수 없습니다.")
        logging.debug("💡 설치: choco install fzf (Windows) 또는 sudo apt install fzf (Linux)")
        return []
    except Exception as e:
        logging.error(f"fzf 검색 오류: {e}")
        return []

def _search_with_everything(query: str) -> List[Dict[str, Any]]:
    """Everything 검색"""
    import subprocess
    
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
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
        logging.debug("❌ Everything을 찾을 수 없습니다.")
        logging.debug("💡 다운로드: https://www.voidtools.com/")
        return []
    
    try:
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
        logging.error(f"Everything 검색 오류: {e}")
        return []

def _display_results(results: List[Dict[str, Any]], display_choice: str, query: str):
    """검색 결과 표시"""
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    if "상위 10개" in display_choice:
        _show_top_results(results[:10])
    elif "모든 결과" in display_choice:
        _show_all_results(results)
    elif "fzf로 선택" in display_choice:
        _show_with_fzf(results)
    elif "파일로 저장" in display_choice:
        _save_to_file(results, query)

def _show_top_results(results: List[Dict[str, Any]]):
    """상위 결과 표시"""
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    for i, result in enumerate(results, 1):
        size_mb = result['size'] / (1024 * 1024)
        mtime_str = time.strftime('%Y-%m-%d %H:%M', time.localtime(result['mtime']))
        
        logging.debug(f"{i:2d}. {result['name']}")
        logging.debug(f"📁 {result['dir']}")
        logging.debug(f"📊 {size_mb:.1f}MB, {mtime_str}")
        
        if 'match_type' in result:
            match_icon = "📝" if result['match_type'] == 'content' else "📄"
            logging.debug(f"{match_icon} {result['match_type']} 매칭")

def _show_all_results(results: List[Dict[str, Any]]):
    """모든 결과 표시"""
    _show_top_results(results)

def _show_with_fzf(results: List[Dict[str, Any]]):
    """fzf로 결과 표시"""
    import subprocess
    
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
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
        logging.debug("❌ fzf를 찾을 수 없습니다.")
    except Exception as e:
        logging.debug(f"❌ fzf 실행 오류: {e}")

def _save_to_file(results: List[Dict[str, Any]], query: str):
    """검색 결과를 파일로 저장"""
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    safe_query = query.replace('*', 'star').replace('/', '_').replace('\\', '_')
    filename = D_TASK_ORCHESTRATOR_CLI_LOGS / f"search_results_{safe_query}_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"파일 검색 결과: '{query}'\n")
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
        
        logging.debug(f"✅ 검색 결과 저장: {filename}")
        logging.info(f"검색 결과 파일 저장: {filename}")
        
    except Exception as e:
        logging.debug(f"❌ 파일 저장 실패: {e}")

def _show_help():
    """도움말"""
    print, ensure_value_completed, D_TASK_ORCHESTRATOR_CLI_LOGS, D_TASK_ORCHESTRATOR_CLI = _get_lazy_imports()
    
    help_text = """
🔍 파일 검색 시스템 사용법

📁 검색 경로:
  - 현재 프로젝트: 빠르고 정확한 프로젝트 내 검색
  - Downloads: 다운로드 파일 검색
  - C/D드라이브: 전체 시스템 검색
  - 사용자 정의: 원하는 경로 직접 지정

🔍 검색 방식:
  - 파일명 검색: 가장 빠름, 파일/폴더명만 검색
  - 내용 포함 검색: 정확함, 파일 내용까지 검색
  - fzf 실시간: 대화형, 실시간 필터링 및 미리보기
  - Everything: 초고속, Windows 전용 인덱싱 검색

🎯 검색어 예시:
  - 확장자: *.py, *.txt, *.md
  - 접두사: ensure_, test_, pk_
  - 키워드: renewal, file, found, config
  - 경로: Downloads, Documents, task_orchestrator_cli

⌨️ fzf 사용법:
  - 타이핑: 실시간 필터링
  - ↑/↓: 선택 이동
  - Enter: 선택 확인
  - ESC: 취소

📊 검색 결과 정보:
  - 파일 개수 및 크기 통계
  - 파일 타입 분포
  - 검색 속도 및 시간
  - 매칭 방식 (파일명/내용)
"""
    
    logging.debug(help_text)

if __name__ == "__main__":
    ensure_file_found_simple_clean()
