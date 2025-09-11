import logging
from sources.objects.pk_local_test_activate import LTA


def get_enabled_wsl_distros():
    """
    WSL에서 사용 가능한 배포판 목록을 가져옵니다.
    
    Returns:
        list: 배포판 정보가 담긴 딕셔너리 리스트
    """
    import subprocess
    import os
    import re
    
    try:
        # WSL이 실제로 설치되어 있는지 먼저 확인
        if not os.path.exists(r"C:\Windows\System32\wsl.exe"):
            logging.debug("WSL executable not found")
            return []
            
        result = subprocess.run(['wsl', '-l', '-v'], capture_output=True, text=True)
        
        if result.returncode != 0:
            logging.debug(f"WSL command failed with return code: {result.returncode}")
            if result.stderr:
                logging.debug(f"WSL error: {result.stderr}")
            return []
            
        output = result.stdout
        if not output.strip():
            logging.debug("WSL command returned empty output")
            return []
            
        # null 문자 제거 및 정리
        cleaned_output = output.replace('\x00', '').strip()
        lines = cleaned_output.splitlines()
        for line in lines:
            logging.debug(f"Raw WSL output: {line}")
        
        distros = []
        for line in lines:
            if line.strip():
                # WSL 배포판 정보 파싱
                parts = line.split()
                logging.debug(f"Parsing line: '{line}' -> parts: {parts}")
                
                # 헤더 라인 건너뛰기
                if parts[0] in ['NAME', 'STATE', 'VERSION'] or len(parts) < 3:
                    logging.debug(f"Skipping header line: {line}")
                    continue
                
                if len(parts) >= 3:
                    # * 표시가 있는 경우 처리
                    if parts[0] == '*':
                        # * Ubuntu    Running         2 형태
                        name = parts[1]
                        state = parts[2]
                        version = parts[3] if len(parts) > 3 else "?"
                    else:
                        # Ubuntu    Running         2 형태
                        name = parts[0]
                        state = parts[1]
                        version = parts[2] if len(parts) > 2 else "?"
                    
                    # null 문자 제거
                    name = name.replace('\x00', '').strip()
                    state = state.replace('\x00', '').strip()
                    version = version.replace('\x00', '').strip()
                    
                    if name and name not in ['NAME', 'STATE', 'VERSION']:  # 유효한 배포판 이름인지 확인
                        distro_info = {
                            'name': name,
                            'state': state,
                            'version': version
                        }
                        distros.append(distro_info)
                        logging.debug(f"Added distro: {distro_info}")

        logging.debug(f"Found {len(distros)} WSL distros")
        return distros
        
    except FileNotFoundError:
        logging.debug("WSL command not found")
        return []
    except Exception as e:
        logging.debug(f"Failed to get WSL distros: {e}")
        return []
