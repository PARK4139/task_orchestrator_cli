import subprocess
import re
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_list_deduplicated import get_list_deduplicated
from pkg_py.functions_split.get_list_removed_element_empty import get_list_removed_empty
from pkg_py.functions_split.get_list_striped_element import get_list_striped_element

def get_image_names_from_tasklist():
    """
    tasklist 명령어의 결과에서 이미지명을 수집하고 중복을 제거한 리스트를 반환
    
    Returns:
        list: 이미지명 리스트 (중복 제거됨)
    """
    try:
        # tasklist 명령어 실행 (인코딩 오류 방지)
        try:
            result = subprocess.run(['tasklist', '/FO', 'CSV'], 
                                  capture_output=True, 
                                  text=True, 
                                  encoding='cp949')  # Windows 한국어 인코딩
        except UnicodeDecodeError:
            # cp949 실패 시 기본 인코딩으로 재시도
            result = subprocess.run(['tasklist', '/FO', 'CSV'], 
                                  capture_output=True, 
                                  text=True, 
                                  encoding='utf-8', 
                                  errors='ignore')
        
        if result.returncode != 0:
            ensure_printed(f"❌ tasklist 명령어 실행 실패: {result.stderr}", print_color="red")
            return []
        
        if not result.stdout:
            ensure_printed("⚠️ tasklist 명령어 결과가 비어있습니다.", print_color="yellow")
            return []
        
        lines = result.stdout.strip().split('\n')
        
        # 첫 번째 줄은 헤더이므로 제외
        if lines and lines[0].startswith('"Image Name"'):
            lines = lines[1:]
        
        image_names = []
        
        for line in lines:
            if line.strip():
                # CSV 형식에서 첫 번째 컬럼(이미지명) 추출
                # "Image Name","PID","Session Name","Session#","Mem Usage"
                # "chrome.exe","1234","Console","1","123,456 K"
                
                # CSV 파싱 (쉼표로 분리하되 따옴표 안의 쉼표는 무시)
                parts = re.findall(r'"([^"]*)"', line)
                if parts:
                    image_name = parts[0].strip()  # 첫 번째 컬럼이 이미지명
                    if image_name and image_name.lower() != 'image name':
                        image_names.append(image_name)
        
        # 중복 제거 및 정렬
        if image_names:
            # 빈 문자열 제거
            image_names = get_list_removed_empty(image_names)
            
            # 앞뒤 공백 제거
            image_names = get_list_striped_element(image_names)
            
            # 중복 제거
            image_names = get_list_deduplicated(image_names)
            
            # 알파벳 순으로 정렬
            image_names.sort(key=str.lower)
            
            ensure_printed(f"📋 tasklist에서 {len(image_names)}개의 고유한 이미지명을 수집했습니다.", print_color="green")
        else:
            ensure_printed("⚠️ tasklist에서 이미지명을 찾을 수 없습니다.", print_color="yellow")
        
        return image_names
        
    except Exception as e:
        ensure_printed(f"❌ tasklist 처리 중 오류 발생: {e}", print_color="red")
        return []

def get_list_from_tasklist_with_pid():
    """
    tasklist 명령어의 결과에서 이미지명과 PID를 함께 수집
    
    Returns:
        list: (이미지명, PID) 튜플 리스트
    """
    try:
        # tasklist 명령어 실행 (인코딩 오류 방지)
        try:
            result = subprocess.run(['tasklist', '/FO', 'CSV'], 
                                  capture_output=True, 
                                  text=True, 
                                  encoding='cp949')  # Windows 한국어 인코딩
        except UnicodeDecodeError:
            # cp949 실패 시 기본 인코딩으로 재시도
            result = subprocess.run(['tasklist', '/FO', 'CSV'], 
                                  capture_output=True, 
                                  text=True, 
                                  encoding='utf-8', 
                                  errors='ignore')
        
        if result.returncode != 0:
            ensure_printed(f"❌ tasklist 명령어 실행 실패: {result.stderr}", print_color="red")
            return []
        
        if not result.stdout:
            ensure_printed("⚠️ tasklist 명령어 결과가 비어있습니다.", print_color="yellow")
            return []
        
        lines = result.stdout.strip().split('\n')
        
        # 첫 번째 줄은 헤더이므로 제외
        if lines and lines[0].startswith('"Image Name"'):
            lines = lines[1:]
        
        process_info = []
        
        for line in lines:
            if line.strip():
                # CSV 파싱
                parts = re.findall(r'"([^"]*)"', line)
                if len(parts) >= 2:
                    image_name = parts[0].strip()
                    pid = parts[1].strip()
                    
                    if image_name and image_name.lower() != 'image name':
                        process_info.append((image_name, pid))
        
        # 중복 제거 (이미지명 기준)
        unique_processes = {}
        for image_name, pid in process_info:
            if image_name not in unique_processes:
                unique_processes[image_name] = pid
        
        # 정렬
        sorted_processes = sorted(unique_processes.items(), key=lambda x: x[0].lower())
        
        ensure_printed(f"📋 tasklist에서 {len(sorted_processes)}개의 고유한 프로세스를 수집했습니다.", print_color="green")
        
        return sorted_processes
        
    except Exception as e:
        ensure_printed(f"❌ tasklist 처리 중 오류 발생: {e}", print_color="red")
        return []

def get_list_from_tasklist_filtered(filter_keywords=None):
    """
    tasklist 명령어의 결과에서 특정 키워드로 필터링된 이미지명 리스트 반환
    
    Args:
        filter_keywords (list): 필터링할 키워드 리스트 (기본값: None, 모든 프로세스)
    
    Returns:
        list: 필터링된 이미지명 리스트
    """
    all_processes = get_image_names_from_tasklist()
    
    if not filter_keywords:
        return all_processes
    
    filtered_processes = []
    filter_keywords_lower = [kw.lower() for kw in filter_keywords]
    
    for process in all_processes:
        process_lower = process.lower()
        for keyword in filter_keywords_lower:
            if keyword in process_lower:
                filtered_processes.append(process)
                break
    
    ensure_printed(f"🔍 키워드 {filter_keywords}로 필터링하여 {len(filtered_processes)}개의 프로세스를 찾았습니다.", print_color="cyan")
    
    return filtered_processes

def get_pids_by_process_name(process_img_n):
    """
    프로세스명으로 PID 리스트를 반환 (기존 get_pids 함수 개선)
    
    Args:
        process_img_n (str): 프로세스 이미지명
    
    Returns:
        list: PID 리스트
    """
    try:
        import re
        from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
        from pkg_py.functions_split.get_list_leaved_element_pattern import get_list_leaved_element_pattern
        
        cmd = f"tasklist | findstr {process_img_n}"
        std_list = ensure_command_excuted_to_os(cmd=cmd)
        pids = get_list_leaved_element_pattern(items=std_list, pattern=r'^\S+\s+(\d+)\s+[A-Za-z]')
        
        ensure_printed(f"🔍 프로세스 '{process_img_n}'에서 {len(pids)}개의 PID를 찾았습니다.", print_color="cyan")
        return pids
        
    except Exception as e:
        ensure_printed(f"❌ PID 검색 중 오류 발생: {e}", print_color="red")
        return []

def get_pid_by_window_title(window_title_seg):
    """
    윈도우 타이틀로 PID를 찾는 함수 (기존 get_pid_by_window_title_via_tasklist 함수 개선)
    
    Args:
        window_title_seg (str): 윈도우 타이틀 일부
    
    Returns:
        str or list: PID 또는 PID 리스트
    """
    try:
        cmd = rf'tasklist'
        lines = ensure_command_excuted_to_os(cmd=cmd)
        matching_lines = None
        
        for line in lines:
            if window_title_seg in line:
                matching_lines = line
                break

        if not matching_lines:
            ensure_printed(f"⚠️ 윈도우 타이틀 '{window_title_seg}'을 포함하는 프로세스를 찾을 수 없습니다.", print_color="yellow")
            return None

        pids = []
        parts = matching_lines.split()
        if len(parts) > 1 and window_title_seg in parts[0]:
            pids.append(parts[1])

        if len(pids) == 1:
            ensure_printed(f"✅ 윈도우 타이틀 '{window_title_seg}'의 PID: {pids[0]}", print_color="green")
            return pids[0]
        else:
            ensure_printed(f"📋 윈도우 타이틀 '{window_title_seg}'의 PID들: {pids}", print_color="cyan")
            return pids
            
    except Exception as e:
        ensure_printed(f"❌ 윈도우 타이틀 PID 검색 중 오류 발생: {e}", print_color="red")
        return None

def get_process_name_by_pid(pid):
    """
    PID로 프로세스명을 찾는 함수 (기존 get_process_name_by_pid 함수 개선)
    
    Args:
        pid (int or str): 프로세스 ID
    
    Returns:
        str or None: 프로세스명 또는 None
    """
    try:
        from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
        
        data = ensure_command_excuted_to_os(cmd=f'tasklist | findstr "{pid}"')
        if data and len(data) > 0:
            process_name = data[0].split(" ")[0]
            ensure_printed(f"✅ PID {pid}의 프로세스명: {process_name}", print_color="green")
            return process_name
        else:
            ensure_printed(f"⚠️ PID {pid}에 해당하는 프로세스를 찾을 수 없습니다.", print_color="yellow")
            return None
            
    except Exception as e:
        ensure_printed(f"❌ 프로세스명 검색 중 오류 발생: {e}", print_color="red")
        return None

def get_process_info_by_window_title(window_title_seg):
    """
    윈도우 타이틀로 프로세스 정보를 찾는 함수
    
    Args:
        window_title_seg (str): 윈도우 타이틀 일부
    
    Returns:
        list: 프로세스 정보 리스트 [(pid, name, exe), ...]
    """
    try:
        pid = get_pid_by_window_title(window_title_seg)
        if not pid:
            return []
        
        if isinstance(pid, list):
            # 여러 PID가 있는 경우
            process_info_list = []
            for p in pid:
                process_info = get_process_info_by_pid(p)
                if process_info:
                    process_info_list.append(process_info)
            return process_info_list
        else:
            # 단일 PID인 경우
            process_info = get_process_info_by_pid(pid)
            return [process_info] if process_info else []
            
    except Exception as e:
        ensure_printed(f"❌ 윈도우 타이틀 프로세스 정보 검색 중 오류 발생: {e}", print_color="red")
        return [] 