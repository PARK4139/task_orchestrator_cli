from sources.functions.ensure_seconds_measured import ensure_seconds_measured
import logging
from sources.objects.pk_local_test_activate import LTA
from pathlib import Path
import os
import json
import time
import subprocess
from datetime import datetime, timedelta


@ensure_seconds_measured
def ensure_youtube_cookies_managed_v2(force_refresh=False):
    """
    YouTube 쿠키를 체계적으로 관리하는 메인 함수 v2 - yt-dlp의 --cookies-from-browser 옵션 사용
    
    Args:
        force_refresh (bool): True일 경우 기존 쿠키를 백업하고 무조건 새로 생성
    
    Returns:
        bool: 쿠키 관리 성공 여부
    """
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
    
    cookie_dir = D_TASK_ORCHESTRATOR_CLI_SENSITIVE
    cookie_file = cookie_dir / "chrome_youtube_cookies.txt"
    cookie_meta_file = cookie_dir / "youtube_cookies_metadata_v2.json"
    
    logging.debug("YouTube 쿠키 관리 시스템 v2 시작")
    
    # 강제 갱신 모드인 경우
    if force_refresh:
        logging.debug("강제 갱신 모드: 기존 쿠키를 백업하고 새로 생성합니다.")
        return _force_refresh_cookies_v2(cookie_file, cookie_meta_file)
    
    # 1. 쿠키 상태 진단
    cookie_status = _diagnose_cookie_status_v2(cookie_file, cookie_meta_file)
    
    # 2. 쿠키 상태에 따른 처리
    if cookie_status == "valid":
        logging.debug("쿠키가 유효합니다.")
        return True
    elif cookie_status == "expired":
        logging.debug("️ 쿠키가 만료되었습니다. 갱신이 필요합니다.")
        return _refresh_cookies_v2(cookie_file, cookie_meta_file)
    elif cookie_status == "missing":
        logging.debug("쿠키 파일이 없습니다. 새로 생성합니다.")
        return _create_new_cookies_v2(cookie_file, cookie_meta_file)
    elif cookie_status == "invalid":
        logging.debug("️ 쿠키 파일이 손상되었습니다. 복구를 시도합니다.")
        return _repair_cookies_v2(cookie_file, cookie_meta_file)
    
    return False


def _diagnose_cookie_status_v2(cookie_file: Path, cookie_meta_file: Path) -> str:
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
    return _validate_cookie_file_content_v2(cookie_file)


def _validate_cookie_file_content_v2(cookie_file: Path) -> str:
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


def _refresh_cookies_v2(cookie_file: Path, cookie_meta_file: Path) -> bool:
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
    success = _create_new_cookies_v2(cookie_file, cookie_meta_file)
    
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


def _create_new_cookies_v2(cookie_file: Path, cookie_meta_file: Path) -> bool:
    """
    새로운 쿠키를 생성합니다 - yt-dlp의 --cookies-from-browser 옵션 사용
    
    Returns:
        bool: 생성 성공 여부
    """
    logging.debug("🆕 새 쿠키 생성 중 (브라우저에서 직접 추출)...")
    
    try:
        # yt-dlp를 사용하여 Chrome에서 직접 쿠키 추출
        cmd = [
            "yt-dlp",
            "--cookies-from-browser", "chrome",
            "--cookies", str(cookie_file),
            "--print", "id",  # 실제 다운로드 없이 정보만 추출
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # 테스트용 URL
        ]
        
        logging.debug(f"실행 명령: {' '.join(cmd)}")
        
        # 명령 실행
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            # 쿠키 파일이 생성되었는지 확인
            if cookie_file.exists() and cookie_file.stat().st_size > 0:
                # 메타데이터 생성
                _create_cookie_metadata_v2(cookie_file, cookie_meta_file)
                logging.debug("새 쿠키 생성 완료 (브라우저에서 직접 추출)")
                return True
            else:
                logging.debug("쿠키 파일이 생성되지 않았습니다.")
                return False
        else:
            logging.debug(f"yt-dlp 실행 실패: {result.stderr}")
            
            # 대안: 기존 방식으로 시도
            logging.debug("대안 방식으로 쿠키 생성 시도...")
            return _create_cookies_fallback_v2(cookie_file, cookie_meta_file)
            
    except subprocess.TimeoutExpired:
        logging.debug("쿠키 생성 시간 초과")
        return _create_cookies_fallback_v2(cookie_file, cookie_meta_file)
    except FileNotFoundError:
        logging.debug("yt-dlp가 설치되지 않았습니다.")
        logging.debug("설치 방법: uv add yt-dlp")
        return _create_cookies_fallback_v2(cookie_file, cookie_meta_file)
    except Exception as e:
        logging.debug(f"쿠키 생성 중 오류: {e}")
        return _create_cookies_fallback_v2(cookie_file, cookie_meta_file)


def _create_cookies_fallback_v2(cookie_file: Path, cookie_meta_file: Path) -> bool:
    """
    대안 방식으로 쿠키를 생성합니다.
    
    Returns:
        bool: 생성 성공 여부
    """
    logging.debug("대안 방식: 기존 쿠키 저장 함수 사용")
    
    try:
        # 기존 쿠키 저장 함수 호출
        from sources.functions.save_chrome_youtube_cookies_to_f import save_chrome_youtube_cookies_to_f
        
        success = save_chrome_youtube_cookies_to_f()
        
        if success:
            # 메타데이터 생성
            _create_cookie_metadata_v2(cookie_file, cookie_meta_file)
            logging.debug("대안 방식으로 쿠키 생성 완료")
            return True
        else:
            logging.debug("대안 방식으로도 쿠키 생성 실패")
            return False
            
    except ImportError:
        logging.debug("browser_cookie3 라이브러리가 설치되지 않았습니다.")
        logging.debug("설치 방법: uv add browser-cookie3")
        return False
    except Exception as e:
        logging.debug(f"대안 쿠키 생성 중 오류: {e}")
        return False


def _repair_cookies_v2(cookie_file: Path, cookie_meta_file: Path) -> bool:
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
            _create_cookie_metadata_v2(cookie_file, cookie_meta_file)
            return True
        except Exception as e:
            logging.debug(f"백업 복구 실패: {e}")
    
    # 백업이 없는 경우 새로 생성
    logging.debug("🆕 백업이 없어 새 쿠키를 생성합니다.")
    return _create_new_cookies_v2(cookie_file, cookie_meta_file)


def _force_refresh_cookies_v2(cookie_file: Path, cookie_meta_file: Path) -> bool:
    """
    강제로 쿠키를 새로 생성합니다.
    
    Returns:
        bool: 생성 성공 여부
    """
    logging.debug("강제 쿠키 갱신 중...")
    
    # 기존 쿠키 백업
    if cookie_file.exists():
        backup_file = cookie_file.parent / f"chrome_youtube_cookies_force_refresh_{int(time.time())}.txt"
        try:
            cookie_file.rename(backup_file)
            logging.debug(f"기존 쿠키 백업: {backup_file.name}")
        except Exception as e:
            logging.debug(f"️ 백업 실패: {e}")
    
    # 새 쿠키 생성
    return _create_new_cookies_v2(cookie_file, cookie_meta_file)


def _create_cookie_metadata_v2(cookie_file: Path, cookie_meta_file: Path):
    """
    쿠키 메타데이터를 생성합니다.
    """
    try:
        metadata = {
            'created_at': datetime.now().isoformat(),
            'file_modified': datetime.fromtimestamp(cookie_file.stat().st_mtime).isoformat(),
            'file_size': cookie_file.stat().st_size,
            'expires_at': (datetime.now() + timedelta(days=7)).isoformat(),  # 7일 후 만료
            'version': '2.0',
            'method': 'cookies-from-browser'
        }
        
        with open(cookie_meta_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        logging.debug(f"️ 메타데이터 생성 실패: {e}")


def test_cookie_validation_v2(cookie_file_path: str = None) -> bool:
    """
    쿠키 유효성을 테스트합니다 - v2 방식
    
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
    
    logging.debug("쿠키 유효성 테스트 v2 시작")
    
    # yt-dlp를 사용한 실제 테스트
    try:
        cmd = [
            "yt-dlp",
            "--cookies", str(cookie_file),
            "--print", "id,title",
            "--quiet",
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # 테스트용 URL
        ]
        
        logging.debug("테스트 명령 실행 중...")
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            logging.debug("쿠키 유효성 테스트 v2 통과")
            logging.debug(f"출력: {result.stdout.strip()}")
            return True
        else:
            logging.debug("쿠키 유효성 테스트 v2 실패")
            logging.debug(f"오류: {result.stderr.strip()}")
            return False
            
    except Exception as e:
        logging.debug(f"쿠키 테스트 중 오류: {e}")
        return False


def get_yt_dlp_cookies_options(cookie_file_path: str = None) -> dict:
    """
    yt-dlp에서 사용할 수 있는 쿠키 옵션들을 반환합니다.
    
    Args:
        cookie_file_path: 쿠키 파일 경로 (None이면 기본 경로 사용)
    
    Returns:
        dict: 쿠키 관련 yt-dlp 옵션들
    """
    if cookie_file_path is None:
        from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
        cookie_file = D_TASK_ORCHESTRATOR_CLI_SENSITIVE / "chrome_youtube_cookies.txt"
    else:
        cookie_file = Path(cookie_file_path)
    
    options = {}
    
    # 1. 기본 쿠키 파일 옵션
    if cookie_file.exists() and cookie_file.stat().st_size > 0:
        options['cookiefile'] = str(cookie_file)
        options['cookies'] = str(cookie_file)
    
    # 2. 브라우저에서 직접 쿠키 추출 옵션
    options['cookies_from_browser'] = 'chrome'
    
    # 3. 추가 인증 옵션들
    options['user_agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    options['add_headers'] = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-us,en;q=0.5',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Connection': 'keep-alive',
    }
    
    return options


if __name__ == "__main__":
    # 테스트 실행
    if LTA:
        logging.debug("LTA 모드: 실제 실행 건너뜀")
        logging.debug("테스트를 실행하려면 LTA = False로 설정하세요.")
    else:
        logging.debug("YouTube 쿠키 관리 시스템 v2 테스트 시작")
        
        # 1. 쿠키 관리
        success = ensure_youtube_cookies_managed_v2()
        
        if success:
            logging.debug("쿠키 관리 성공")
            
            # 2. 쿠키 유효성 테스트
            test_success = test_cookie_validation_v2()
            
            if test_success:
                logging.debug("모든 쿠키 관리 작업이 성공적으로 완료되었습니다.")
            else:
                logging.debug("️ 쿠키 유효성 테스트에 실패했습니다.")
        else:
            logging.debug("쿠키 관리에 실패했습니다.")
