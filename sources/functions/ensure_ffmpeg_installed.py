from functools import lru_cache
import os
import subprocess
import logging
import logging
from pathlib import Path
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
import logging
from sources.objects.pk_map_texts import PkTexts

TAG_INFO = PkTexts.get_value_via_attr("INFO")
TAG_WARN = PkTexts.get_value_via_attr("WARNING")
TAG_ERROR = PkTexts.get_value_via_attr("ERROR")


@lru_cache(maxsize=1)
def ensure_ffmpeg_installed():
    """WSL/리눅스 환경에서 ffmpeg 설치 확인 및 설치"""
    
    # system_resources 디렉토리 경로
    system_resources_path = D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
    ffmpeg_path = system_resources_path / "ffmpeg"
    ffprobe_path = system_resources_path / "ffprobe"
    
    # 이미 설치되어 있는지 확인
    if ffmpeg_path.exists() and ffprobe_path.exists():
        logging.debug(f"{TAG_INFO} ffmpeg 및 ffprobe가 이미 system_resources에 설치되어 있습니다")
        return str(ffmpeg_path), str(ffprobe_path)
    
    logging.debug(f"{TAG_INFO} ffmpeg 설치 시작 (system_resources 디렉토리)")
    
    try:
        # system_resources 디렉토리 생성
        system_resources_path.mkdir(parents=True, exist_ok=True)
        
        # 시스템에 ffmpeg가 설치되어 있는지 확인
        try:
            result = subprocess.run(['which', 'ffmpeg'], capture_output=True, text=True)
            if result.returncode == 0:
                system_ffmpeg = result.stdout.strip()
                logging.debug(f"{TAG_INFO} 시스템 ffmpeg 발견: {system_ffmpeg}")
                
                # 시스템 ffmpeg를 system_resources로 복사
                subprocess.run(['cp', system_ffmpeg, str(ffmpeg_path)], check=True)
                logging.debug(f"{TAG_INFO} ffmpeg 복사 완료: {ffmpeg_path}")
            else:
                # 시스템에 ffmpeg가 없으면 apt로 설치
                logging.debug(f"{TAG_WARN} 시스템에 ffmpeg가 없습니다. apt로 설치를 시도합니다")
                install_ffmpeg_via_apt()
                return ensure_ffmpeg_installed()  # 재귀 호출로 재확인
                
        except subprocess.CalledProcessError:
            logging.debug(f"{TAG_WARN} ffmpeg 복사 실패, apt 설치를 시도합니다")
            install_ffmpeg_via_apt()
            return ensure_ffmpeg_installed()  # 재귀 호출로 재확인
        
        # ffprobe도 동일하게 처리
        try:
            result = subprocess.run(['which', 'ffprobe'], capture_output=True, text=True)
            if result.returncode == 0:
                system_ffprobe = result.stdout.strip()
                logging.debug(f"{TAG_INFO} 시스템 ffprobe 발견: {system_ffprobe}")
                
                subprocess.run(['cp', system_ffprobe, str(ffprobe_path)], check=True)
                logging.debug(f"{TAG_INFO} ffprobe 복사 완료: {ffprobe_path}")
            else:
                logging.debug(f"{TAG_WARN} 시스템에 ffprobe가 없습니다")
                
        except subprocess.CalledProcessError:
            logging.debug(f"{TAG_WARN} ffprobe 복사 실패")
        
        # 실행 권한 설정
        if ffmpeg_path.exists():
            os.chmod(ffmpeg_path, 0o755)
        if ffprobe_path.exists():
            os.chmod(ffprobe_path, 0o755)
        
        logging.debug(f"{TAG_INFO} ffmpeg 설치 완료")
        return str(ffmpeg_path), str(ffprobe_path)
        
    except Exception as e:
        logging.debug(f"{TAG_ERROR} ffmpeg 설치 실패: {e}")
        logging.error(f"ffmpeg 설치 오류: {e}")
        return None, None


def install_ffmpeg_via_apt():
    """apt를 사용하여 ffmpeg 설치"""
    try:
        logging.debug(f"{TAG_INFO} apt update 실행 중...")
        subprocess.run(['sudo', 'apt', 'update'], check=True)
        
        logging.debug(f"{TAG_INFO} ffmpeg 설치 중...")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'ffmpeg'], check=True)
        
        logging.debug(f"{TAG_INFO} ffmpeg apt 설치 완료")
        
    except subprocess.CalledProcessError as e:
        logging.debug(f"{TAG_ERROR} apt 설치 실패: {e}")
        raise
    except Exception as e:
        logging.debug(f"{TAG_ERROR} 예상치 못한 오류: {e}")
        raise


def is_ffmpeg_available():
    """ffmpeg 사용 가능 여부 확인"""
    try:
        result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
        return result.returncode == 0
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_ffmpeg_path():
    """ffmpeg 경로 반환 (설치 확인 포함)"""
    ffmpeg_path, ffprobe_path = ensure_ffmpeg_installed()
    return ffmpeg_path


def get_ffprobe_path():
    """ffprobe 경로 반환 (설치 확인 포함)"""
    ffmpeg_path, ffprobe_path = ensure_ffmpeg_installed()
    return ffprobe_path
