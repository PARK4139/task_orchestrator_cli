def ensure_everything_path_changed():
    """Everything 경로 변경 감지 및 DB 업데이트"""
    import os
    import json
    import time
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_everything_exe_database_reindex import ensure_everything_exe_database_reindex
    
    def get_everything_paths():
        """Everything이 인덱싱하는 경로들을 가져오기"""
        try:
            # Everything 설정 파일에서 경로 정보 읽기
            everything_ini = os.path.expanduser(r"~\AppData\Roaming\Everything\Everything.ini")
            if not os.path.exists(everything_ini):
                ensure_printed("Everything 설정 파일이 없습니다. 기본 경로를 사용합니다.", print_color='yellow')
                # 기본 경로 반환
                return ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\"]
            
            paths = []
            with open(everything_ini, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('include_folder='):
                        path = line.split('=', 1)[1].strip()
                        if path and os.path.exists(path):
                            paths.append(path)
            
            # 경로가 없으면 기본 경로 사용
            if not paths:
                ensure_printed("Everything 설정에 경로가 없습니다. 기본 경로를 사용합니다.", print_color='yellow')
                return ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\"]
            
            return paths
        except Exception as e:
            ensure_printed(f"Everything 경로 읽기 실패: {e}", print_color='red')
            return ["C:\\", "D:\\", "E:\\", "F:\\", "G:\\", "H:\\"]
    
    def save_paths_cache(paths):
        """경로 정보를 캐시에 저장"""
        try:
            cache_file = os.path.expanduser(r"~\AppData\Roaming\Everything\paths_cache.json")
            cache_data = {
                "paths": paths,
                "timestamp": time.time()
            }
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            ensure_printed(f"경로 캐시 저장 실패: {e}", print_color='red')
    
    def load_paths_cache():
        """캐시에서 경로 정보 로드"""
        try:
            cache_file = os.path.expanduser(r"~\AppData\Roaming\Everything\paths_cache.json")
            if os.path.exists(cache_file):
                with open(cache_file, 'r', encoding='utf-8') as f:
                    cache_data = json.load(f)
                    return cache_data.get("paths", [])
            return []
        except Exception:
            return []
    
    def paths_changed(current_paths, cached_paths):
        """경로가 변경되었는지 확인"""
        if len(current_paths) != len(cached_paths):
            return True
        
        current_set = set(current_paths)
        cached_set = set(cached_paths)
        
        return current_set != cached_set
    
    # 현재 경로 가져오기
    current_paths = get_everything_paths()
    ensure_printed(f"현재 Everything 경로: {current_paths}", print_color='cyan')
    
    # 캐시된 경로 가져오기
    cached_paths = load_paths_cache()
    
    # 경로 변경 확인
    if paths_changed(current_paths, cached_paths):
        ensure_printed("Everything 경로가 변경되었습니다.", print_color='cyan')
        ensure_printed(f"이전 경로: {cached_paths}", print_color='yellow')
        ensure_printed(f"현재 경로: {current_paths}", print_color='yellow')
        
        # DB 재구축 실행
        if ensure_everything_exe_database_reindex():
            # 성공하면 새로운 경로 정보 캐시에 저장
            save_paths_cache(current_paths)
            ensure_printed("경로 변경에 따른 DB 업데이트가 완료되었습니다.", print_color='green')
            return True
        else:
            ensure_printed("DB 업데이트가 실패했습니다.", print_color='red')
            return False
    else:
        ensure_printed("Everything 경로가 변경되지 않았습니다.", print_color='green')
        return True 