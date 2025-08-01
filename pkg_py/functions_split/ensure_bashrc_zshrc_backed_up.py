import os
import shutil
import platform
import subprocess
from datetime import datetime


def detect_os():
    """운영체제를 감지하는 함수"""
    from pkg_py.functions_split.get_os_n import get_os_n
    
    os_type = get_os_n()
    
    # WSL 환경인지 추가 확인
    if os_type == "linux":
        if os.path.exists("/proc/version"):
            with open("/proc/version", "r") as f:
                version_info = f.read().lower()
                if "microsoft" in version_info or "wsl" in version_info:
                    return "wsl"
        return "linux"
    elif os_type == "windows":
        # Windows에서 WSL이 실행 중인지 확인
        try:
            result = subprocess.run(['wsl', 'echo', 'wsl'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and 'wsl' in result.stdout:
                return "wsl"
            else:
                return "windows"
        except:
            return "windows"
    else:
        return os_type


def detect_os_for_testing():
    """테스트용 운영체제 감지 함수 - Windows로 강제 설정"""
    return "windows"


def get_backup_files_by_os():
    """운영체제에 따라 백업할 파일 목록을 반환"""
    os_type = detect_os()
    
    if os_type == "wsl" or os_type == "linux":
        # Linux/WSL 환경
        return [
            os.path.expanduser("~/.bashrc"),
            os.path.expanduser("~/.zshrc"),
            os.path.expanduser("~/.profile"),
            os.path.expanduser("~/.bash_profile"),
            os.path.expanduser("~/.bash_aliases"),
            os.path.expanduser("~/.inputrc"),
            os.path.expanduser("~/.vimrc"),
            os.path.expanduser("~/.gitconfig"),
            os.path.expanduser("~/.ssh/config"),
            os.path.expanduser("~/.tmux.conf")
        ]
    elif os_type == "windows":
        # Windows 환경 - bashrc, zshrc 제외
        return [
            os.path.expanduser("~/Documents/PowerShell/Microsoft.PowerShell_profile.ps1"),
            os.path.expanduser("~/Documents/WindowsPowerShell/Microsoft.PowerShell_profile.ps1"),
            os.path.expanduser("~/.gitconfig"),
            os.path.expanduser("~/AppData/Roaming/Code/User/settings.json"),
            os.path.expanduser("~/AppData/Roaming/Code/User/keybindings.json"),
            os.path.expanduser("~/AppData/Roaming/Code/User/snippets"),
            os.path.expanduser("~/AppData/Roaming/Code/User/extensions"),
            os.path.expanduser("~/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json")
        ]
    else:
        # 기타 환경
        return []


def get_backup_directory_by_os():
    """운영체제에 따라 백업 디렉토리를 반환"""
    os_type = detect_os()
    
    if os_type == "wsl" or os_type == "linux":
        # Linux/WSL 환경
        return os.path.join(os.path.expanduser("~"), "Downloads", "pk_system", "pkg_ide_backup")
    elif os_type == "windows":
        # Windows 환경
        return os.path.join(os.path.expanduser("~"), "Downloads", "pk_system", "pkg_ide_backup")
    else:
        # 기타 환경
        return os.path.join(os.path.expanduser("~"), "Downloads", "pk_system", "pkg_ide_backup")


def ensure_bashrc_zshrc_backed_up(custom_suffix=None):
    """운영체제에 따라 적절한 파일들을 백업하는 함수"""
    # 운영체제 감지
    os_type = detect_os()
    print(f"🔍 감지된 운영체제: {os_type}")
    
    # 백업 대상 파일들
    backup_files = get_backup_files_by_os()
    
    # 백업 디렉토리
    backup_dir = get_backup_directory_by_os()
    
    # 타임스탬프 생성
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 사용자 정의 suffix가 있으면 사용, 없으면 기본값
    if custom_suffix:
        suffix = custom_suffix
    else:
        suffix = timestamp
    
    backed_up_files = []
    
    for file_path in backup_files:
        if os.path.exists(file_path):
            # 파일명 추출
            filename = os.path.basename(file_path)
            
            # 백업 파일명 생성
            backup_filename = f"{filename}.bak.{suffix}"
            backup_path = os.path.join(backup_dir, backup_filename)
            
            try:
                # 백업 디렉토리가 없으면 생성
                os.makedirs(backup_dir, exist_ok=True)
                
                # 파일 복사
                shutil.copy2(file_path, backup_path)
                
                backed_up_files.append(backup_path)
                print(f"✅ 백업 완료: {filename} -> {backup_filename}")
                
            except Exception as e:
                print(f"❌ 백업 실패: {filename} - {str(e)}")
        else:
            print(f"⚠️ 파일이 존재하지 않음: {file_path}")
    
    return backed_up_files


if __name__ == "__main__":
    import sys
    
    # 명령행 인수에서 custom suffix 받기
    custom_suffix = None
    if len(sys.argv) > 1:
        custom_suffix = sys.argv[1]
        print(f"📝 사용자 정의 suffix 사용: {custom_suffix}")
    
    # 테스트 실행
    backed_up_files = ensure_bashrc_zshrc_backed_up(custom_suffix=custom_suffix)
    
    if backed_up_files:
        print(f"✅ 총 {len(backed_up_files)}개 파일 백업 완료")
    else:
        print("⚠️ 백업할 파일이 없습니다") 