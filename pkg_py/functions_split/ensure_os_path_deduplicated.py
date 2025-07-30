import os
import winreg
import subprocess
import sys

def ensure_os_path_deduplicated():
    """Windows 환경변수 PATH 정리"""
    
    # 시스템 PATH와 사용자 PATH 모두 가져오기
    system_path = get_system_path()
    user_path = get_user_path()
    
    print(f"📋 시스템 PATH 항목 수: {len(system_path.split(';')) if system_path else 0}")
    print(f"📋 사용자 PATH 항목 수: {len(user_path.split(';')) if user_path else 0}")
    
    # 모든 PATH 병합
    all_paths = system_path + ";" + user_path if user_path else system_path
    path_list = all_paths.split(";")
    
    # 중복 제거 및 정리
    seen = set()
    clean_path = []
    
    for path in path_list:
        norm = os.path.normpath(path.strip())
        if not norm:
            continue
        if "user" in norm.lower() and "pk_system" not in norm.lower():  # 다른 사용자 경로 제거 (pk_system 제외)
            continue
        if norm not in seen:
            seen.add(norm)
            clean_path.append(norm)
    
    # 필수 경로 재정렬 (시스템, .venv, pk_system 우선)
    priority = ["system32", ".venv", "pk_system"]
    def sort_key(p):
        for i, keyword in enumerate(priority):
            if keyword.lower() in p.lower():
                return i
        return len(priority)
    
    clean_path.sort(key=sort_key)
    
    # 병합
    new_path = ";".join(clean_path)
    
    # 사용자 환경변수에만 저장 (시스템 환경변수는 관리자 권한 필요)
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        print("✅ 사용자 PATH 환경변수가 정리되었습니다.")
        
        # 환경변수 변경 알림
        broadcast_environment_change()
        
        print(" 새 터미널을 열어서 환경변수 변경사항을 확인하세요.")
        print("📝 또는 다음 명령어로 현재 세션에 적용:")
        print("   refreshenv")
        
    except Exception as e:
        print(f"❌ 환경변수 정리 실패: {e}")

def get_system_path():
    """시스템 환경변수 PATH 가져오기"""
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                           r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment", 
                           0, winreg.KEY_READ) as key:
            try:
                system_path, _ = winreg.QueryValueEx(key, "Path")
                return system_path
            except FileNotFoundError:
                return ""
    except Exception:
        return ""

def get_user_path():
    """사용자 환경변수 PATH 가져오기"""
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ) as key:
            try:
                user_path, _ = winreg.QueryValueEx(key, "Path")
                return user_path
            except FileNotFoundError:
                return ""
    except Exception:
        return ""

def broadcast_environment_change():
    """환경변수 변경을 시스템에 알림"""
    try:
        # WM_SETTINGCHANGE 메시지 브로드캐스트
        import ctypes
        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x001A
        SMTO_ABORTIFHUNG = 0x0002
        result = ctypes.windll.user32.SendMessageTimeoutW(
            HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment", 
            SMTO_ABORTIFHUNG, 5000, ctypes.byref(ctypes.c_ulong())
        )
        if result:
            print("✅ 환경변수 변경 알림이 전송되었습니다.")
        else:
            print("⚠️ 환경변수 변경 알림 전송 실패")
    except Exception as e:
        print(f"⚠️ 환경변수 변경 알림 실패: {e}")

if __name__ == "__main__":
    ensure_os_path_deduplicated()
