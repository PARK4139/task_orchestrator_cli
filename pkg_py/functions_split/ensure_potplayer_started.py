from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
import subprocess
import psutil

def ensure_potplayer_started():
    """
    PotPlayer를 단일 인스턴스로 시작하는 함수
    이미 실행 중이면 새로 시작하지 않음
    """
    try:
        # PotPlayer 프로세스 확인
        potplayer_running = False
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if 'PotPlayer' in proc.info['name']:
                    potplayer_running = True
                    ensure_printed(f" PotPlayer가 이미 실행 중입니다 (PID: {proc.info['pid']})", print_color="green")
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        if not potplayer_running:
            # PotPlayer 시작
            cmd = f'"{F_POT_PLAYER_MINI_64_EXE}"'
            ensure_printed(f" PotPlayer를 시작합니다...", print_color="cyan")
            
            # 백그라운드에서 실행
            subprocess.Popen(cmd, shell=True)
            ensure_printed(f" PotPlayer가 시작되었습니다", print_color="green")
        else:
            ensure_printed(f"ℹ️ PotPlayer가 이미 실행 중입니다", print_color="yellow")
            
    except Exception as e:
        ensure_printed(f" PotPlayer 시작 실패: {e}", print_color="red")
        raise Exception(f"PotPlayer 시작 실패: {e}")

def is_potplayer_running():
    """PotPlayer가 실행 중인지 확인"""
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if 'PotPlayer' in proc.info['name']:
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
    except Exception:
        return False

def get_potplayer_process():
    """실행 중인 PotPlayer 프로세스 정보 반환"""
    try:
        for proc in psutil.process_iter(['pid', 'name', 'create_time']):
            try:
                if 'PotPlayer' in proc.info['name']:
                    return proc
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return None
    except Exception:
        return None 