from sources.functions.ensure_seconds_measured import ensure_seconds_measured
import logging
from sources.objects.pk_local_test_activate import LTA
from pathlib import Path
import os
import json
import time
from datetime import datetime, timedelta


@ensure_seconds_measured
def ensure_youtube_cookies_managed(force_refresh=False):
    """
    YouTube 쿠키를 체계적으로 관리하는 메인 함수
    
    Args:
        force_refresh (bool): True일 경우 기존 쿠키를 백업하고 무조건 새로 생성
    
    Returns:
        bool: 쿠키 관리 성공 여부
    """
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
    
    cookie_dir = D_TASK_ORCHESTRATOR_CLI_SENSITIVE
    cookie_file = cookie_dir / "chrome_youtube_cookies.txt"
    cookie_meta_file = cookie_dir / "youtube_cookies_metadata.json"
    
    logging.debug("YouTube 쿠키 관리 시스템 시작")
    
    # 강제 갱신 모드인 경우
    if force_refresh:
        logging.debug("강제 갱신 모드: 기존 쿠키를 백업하고 새로 생성합니다.")
        return _force_refresh_cookies(cookie_file, cookie_meta_file)
    
    # 1. 쿠키 상태 진단
    cookie_status = _diagnose_cookie_status(cookie_file, cookie_meta_file)
    
    # 2. 쿠키 상태에 따른 처리
    if cookie_status == "valid":
        logging.debug("쿠키가 유효합니다.")
        return True
    elif cookie_status == "expired":
        logging.debug("️ 쿠키가 만료되었습니다. 갱신이 필요합니다.")
        return _refresh_cookies(cookie_file, cookie_meta_file)
    elif cookie_status == "missing":
        logging.debug("쿠키 파일이 없습니다. 새로 생성합니다.")
        return _create_new_cookies(cookie_file, cookie_meta_file)
    elif cookie_status == "invalid":
        logging.debug("️ 쿠키 파일이 손상되었습니다. 복구를 시도합니다.")
        return _repair_cookies(cookie_file, cookie_meta_file)
    
    return False


def _diagnose_cookie_status(cookie_file: Path, cookie_meta_file: Path) -> str:
    """
    쿠키 상태를 진단합니다.
    
    Returns:
        str: "valid", "expired", "missing", "invalid" 중 하나
    """
    # 쿠키 파일이 존재하지 않는 경우
    if not cookie_file.exists():
        return "missing"
    
    # 쿠키 파일이 비어있는 경우
    if cookie_file.stat().st_size == 0:
        return "invalid"
    
    # 메타데이터 파일이 존재하는 경우 만료 시간 확인
    if cookie_meta_file.exists():
        try:
            with open(cookie_meta_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            # 만료 시간 확인
            if 'expires_at' in metadata:
                expires_at = datetime.fromisoformat(metadata['expires_at'])
                if datetime.now() > expires_at:
                    return "expired"
            
            # 쿠키 파일 수정 시간 확인
            if 'file_modified' in metadata:
                file_modified = datetime.fromisoformat(metadata['file_modified'])
                if datetime.now() - file_modified > timedelta(days=7):
                    return "expired"
            
            return "valid"
        except (json.JSONDecodeError, KeyError, ValueError):
            return "invalid"
    
    # 메타데이터가 없는 경우 기본 검증
    return _validate_cookie_file_content(cookie_file)


def _validate_cookie_file_content(cookie_file: Path) -> str:
    """
    쿠키 파일 내용을 검증합니다.
    
    Returns:
        str: "valid" 또는 "invalid"
    """
    try:
        with open(cookie_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 최소한의 쿠키 데이터가 있는지 확인
        cookie_lines = [line for line in lines if line.strip() and not line.startswith('#')]
        
        if len(cookie_lines) < 3:  # 최소 3개의 쿠키가 있어야 함
            return "invalid"
        
        # YouTube 도메인 쿠키가 있는지 확인
        youtube_cookies = [line for line in cookie_lines if '.youtube.com' in line]
        if not youtube_cookies:
            return "invalid"
        
        return "valid"
    except Exception:
        return "invalid"


def _refresh_cookies(cookie_file: Path, cookie_meta_file: Path) -> bool:
    """
    만료된 쿠키를 갱신합니다.
    
    Returns:
        bool: 갱신 성공 여부
    """
    logging.debug("쿠키 갱신 중...")
    
    # 기존 쿠키 백업
    if cookie_file.exists():
        backup_file = cookie_file.parent / f"chrome_youtube_cookies_backup_{int(time.time())}.txt"
        try:
            cookie_file.rename(backup_file)
            logging.debug(f"기존 쿠키 백업: {backup_file.name}")
        except Exception as e:
            logging.debug(f"️ 백업 실패: {e}")
    
    # 새 쿠키 생성
    success = _create_new_cookies(cookie_file, cookie_meta_file)
    
    if success:
        logging.debug("쿠키 갱신 완료")
    else:
        # 백업에서 복구 시도
        if 'backup_file' in locals() and backup_file.exists():
            try:
                backup_file.rename(cookie_file)
                logging.debug("백업에서 쿠키 복구")
            except Exception as e:
                logging.debug(f"복구 실패: {e}")
    
    return success


def _create_new_cookies(cookie_file: Path, cookie_meta_file: Path) -> bool:
    """
    새로운 쿠키를 생성합니다.
    
    Returns:
        bool: 생성 성공 여부
    """
    logging.debug("🆕 새 쿠키 생성 중...")
    
    try:
        # 기존 쿠키 저장 함수 호출
        from sources.functions.save_chrome_youtube_cookies_to_f import save_chrome_youtube_cookies_to_f
        
        success = save_chrome_youtube_cookies_to_f()
        
        if success:
            # 메타데이터 생성
            _create_cookie_metadata(cookie_file, cookie_meta_file)
            logging.debug("새 쿠키 생성 완료")
            return True
        else:
            logging.debug("쿠키 생성 실패")
            return False
            
    except ImportError:
        logging.debug("browser_cookie3 라이브러리가 설치되지 않았습니다.")
        logging.debug("설치 방법: uv add browser-cookie3")
        return False
    except Exception as e:
        logging.debug(f"쿠키 생성 중 오류: {e}")
        return False


def _repair_cookies(cookie_file: Path, cookie_meta_file: Path) -> bool:
    """
    손상된 쿠키를 복구합니다.
    
    Returns:
        bool: 복구 성공 여부
    """
    logging.debug("쿠키 복구 시도 중...")
    
    # 백업 파일 찾기
    backup_files = list(cookie_file.parent.glob("chrome_youtube_cookies_backup_*.txt"))
    
    if backup_files:
        # 가장 최근 백업 사용
        latest_backup = max(backup_files, key=lambda f: f.stat().st_mtime)
        try:
            latest_backup.rename(cookie_file)
            logging.debug(f"백업에서 복구 완료: {latest_backup.name}")
            _create_cookie_metadata(cookie_file, cookie_meta_file)
            return True
        except Exception as e:
            logging.debug(f"백업 복구 실패: {e}")
    
    # 백업이 없는 경우 새로 생성
    logging.debug("🆕 백업이 없어 새 쿠키를 생성합니다.")
    return _create_new_cookies(cookie_file, cookie_meta_file)


def _create_cookie_metadata(cookie_file: Path, cookie_meta_file: Path):
    """
    쿠키 메타데이터를 생성합니다.
    """
    try:
        metadata = {
            'created_at': datetime.now().isoformat(),
            'file_modified': datetime.fromtimestamp(cookie_file.stat().st_mtime).isoformat(),
            'file_size': cookie_file.stat().st_size,
            'expires_at': (datetime.now() + timedelta(days=7)).isoformat(),  # 7일 후 만료
            'version': '1.0'
        }
        
        with open(cookie_meta_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        logging.debug(f"️ 메타데이터 생성 실패: {e}")


def backup_successful_cookies():
    """
    다운로드 성공 시에만 쿠키를 백업합니다.
    
    Returns:
        bool: 백업 성공 여부
    """
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_RECYLCE_BIN
    
    cookie_file = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "chrome_youtube_cookies.txt"
    backup_dir = Path(D_PK_RECYLCE_BIN) / "cookies_backup"
    
    # 백업 디렉토리 생성
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    if not cookie_file.exists():
        return False
    
    try:
        # 백업 파일명 생성 (타임스탬프 포함)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = backup_dir / f"youtube_cookies_success_{timestamp}.txt"
        
        # 쿠키 파일 복사
        import shutil
        shutil.copy2(cookie_file, backup_file)
        
        # 백업 메타데이터 생성
        backup_meta = backup_dir / f"youtube_cookies_success_{timestamp}.json"
        metadata = {
            'backup_time': datetime.now().isoformat(),
            'original_file': str(cookie_file),
            'backup_file': str(backup_file),
            'file_size': cookie_file.stat().st_size,
            'success_type': 'download_success',
            'version': '1.0'
        }
        
        with open(backup_meta, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        
        return True
        
    except Exception as e:
        logging.debug(f"쿠키 백업 실패: {e}")
        return False


def restore_cookies_from_backup(backup_timestamp: str = None):
    """
    백업된 쿠키를 복원합니다.
    
    Args:
        backup_timestamp (str): 복원할 백업의 타임스탬프 (None이면 가장 최근 백업)
    
    Returns:
        bool: 복원 성공 여부
    """
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_PK_RECYLCE_BIN
    
    cookie_file = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "chrome_youtube_cookies.txt"
    backup_dir = Path(D_PK_RECYLCE_BIN) / "cookies_backup"
    
    if not backup_dir.exists():
        logging.debug("백업 디렉토리가 존재하지 않습니다.")
        return False
    
    try:
        if backup_timestamp:
            # 특정 타임스탬프의 백업 사용
            backup_file = backup_dir / f"youtube_cookies_success_{backup_timestamp}.txt"
        else:
            # 가장 최근 백업 찾기
            backup_files = list(backup_dir.glob("youtube_cookies_success_*.txt"))
            if not backup_files:
                logging.debug("백업된 쿠키가 없습니다.")
                return False
            
            backup_file = max(backup_files, key=lambda f: f.stat().st_mtime)
        
        if not backup_file.exists():
            logging.debug(f"백업 파일을 찾을 수 없습니다: {backup_file.name}")
            return False
        
        # 백업에서 복원
        import shutil
        shutil.copy2(backup_file, cookie_file)
        
        logging.debug(f"쿠키 복원 완료: {backup_file.name}")
        return True
        
    except Exception as e:
        logging.debug(f"쿠키 복원 실패: {e}")
        return False


def test_cookie_validation(cookie_file_path: str = None) -> bool:
    """
    쿠키 유효성을 테스트합니다.
    
    Args:
        cookie_file_path: 테스트할 쿠키 파일 경로 (None이면 기본 경로 사용)
    
    Returns:
        bool: 쿠키 유효성 테스트 결과
    """
    if cookie_file_path is None:
        from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
        cookie_file = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "chrome_youtube_cookies.txt"
    else:
        cookie_file = Path(cookie_file_path)
    
    logging.debug("쿠키 유효성 테스트 시작")
    
    # 간단한 YouTube API 테스트
    try:
        import yt_dlp
        
        ydl_opts = {
            'cookiefile': str(cookie_file),
            'quiet': True,
            'extract_flat': True,
            'no_warnings': True
        }
        
        # 테스트용 간단한 YouTube URL (연령 제한 없는 동영상)
        test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Rick Roll
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(test_url, download=False)
            
            if info and 'id' in info:
                logging.debug("쿠키 유효성 테스트 통과")
                return True
            else:
                logging.debug("쿠키 유효성 테스트 실패")
                return False
                
    except Exception as e:
        logging.debug(f"쿠키 테스트 중 오류: {e}")
        return False


