import os
from pkg_py.system_object.files import D_PKG_IMAGE_AND_VIDEO_AND_SOUND
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_spoken import ensure_spoken

def create_time_wav_components():
    """시간 관련 WAV 구성 요소 생성"""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'AUDIO_COMPONENT_CREATED': '기본 구성 요소 생성',
                'AUDIO_COMPONENT_FAILED': '기본 구성 요소 생성 실패',
                'AUDIO_COMPONENTS_COMPLETE': '시간 관련 WAV 구성 요소 생성 완료',
                'AUDIO_TIME_EXPRESSION_CREATED': '시간 표현 생성',
                'AUDIO_TIME_EXPRESSION_FAILED': '시간 표현 생성 실패',
                'AUDIO_SPECIFIC_COMPONENTS_COMPLETE': '특정 시간 구성 요소 생성 완료',
                'AUDIO_WAV_COMPONENTS_START': '시간 관련 WAV 구성 요소 생성 시작',
                'AUDIO_ALL_COMPONENTS_EXIST': '모든 시간 구성 요소가 존재합니다',
                'AUDIO_MISSING_COMPONENTS': '누락된 구성 요소들이 있습니다. 생성을 시작합니다',
                'AUDIO_ALL_COMPONENTS_COMPLETE': '모든 시간 구성 요소 생성이 완료되었습니다',
                'AUDIO_SOME_COMPONENTS_FAILED': '일부 구성 요소 생성에 실패했습니다'
            })()

        from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND
        from pkg_py.functions_split.ensure_ffmpeg_installed_to_pkg_windows import ensure_ffmpeg_installed_to_pkg_windows
        
        # FFmpeg 설정
        ffmpeg_path, ffprobe_path = ensure_ffmpeg_installed_to_pkg_windows()
        if ffmpeg_path and ffprobe_path:
            AudioSegment.converter = ffmpeg_path
            AudioSegment.ffprobe = ffprobe_path
        
        # 기본 시간 구성 요소 생성
        time_components = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
            "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
            "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
            "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"
        ]
        
        created_count = 0
        existing_count = 0
        
        for component in time_components:
            filename = f"{component}.wav"
            file_path = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, filename)
            
            if not os.path.exists(file_path):
                try:
                    # 간단한 비프음 생성 (1초, 440Hz)
                    audio = AudioSegment.sine(frequency=440, duration=1000)
                    audio.export(file_path, format="wav")
                    created_count += 1
                    ensure_printed(f"[{PkMessages2025.AUDIO_COMPONENT_CREATED}] {PK_ANSI_COLOR_MAP['GREEN']}파일명={filename} {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
                except Exception as e:
                    ensure_printed(f"[{PkMessages2025.AUDIO_COMPONENT_FAILED}] {PK_ANSI_COLOR_MAP['RED']}파일명={filename} 오류={e} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
            else:
                existing_count += 1
        
        ensure_printed(f"[{PkMessages2025.AUDIO_COMPONENTS_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}새로생성={created_count}개 기존={existing_count}개 {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
        
        return {
            'created_count': created_count,
            'existing_count': existing_count,
            'total_count': created_count + existing_count
        }
        
    except Exception as e:
        ensure_printed(f"[{PkMessages2025.AUDIO_COMPONENT_FAILED}] {PK_ANSI_COLOR_MAP['RED']}오류={e} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
        return None


def create_specific_time_components():
    """특정 시간 표현 생성 (시, 분, 초 등)"""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'AUDIO_TIME_EXPRESSION_CREATED': '시간 표현 생성',
                'AUDIO_TIME_EXPRESSION_FAILED': '시간 표현 생성 실패',
                'AUDIO_SPECIFIC_COMPONENTS_COMPLETE': '특정 시간 구성 요소 생성 완료'
            })()

        from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND
        
        time_expressions = [
            "시", "분", "초", "시간", "분간", "초간",
            "오전", "오후", "아침", "점심", "저녁", "밤",
            "지금", "이제", "곧", "잠시", "조금", "많이"
        ]
        
        created_count = 0
        
        for expression in time_expressions:
            filename = f"{expression}.wav"
            file_path = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, filename)
            
            if not os.path.exists(file_path):
                try:
                    # 간단한 비프음 생성 (1초, 440Hz)
                    audio = AudioSegment.sine(frequency=440, duration=1000)
                    audio.export(file_path, format="wav")
                    created_count += 1
                    ensure_printed(f"[{PkMessages2025.AUDIO_TIME_EXPRESSION_CREATED}] {PK_ANSI_COLOR_MAP['GREEN']}표현={expression} {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
                except Exception as e:
                    ensure_printed(f"[{PkMessages2025.AUDIO_TIME_EXPRESSION_FAILED}] {PK_ANSI_COLOR_MAP['RED']}표현={expression} 오류={e} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
        
        ensure_printed(f"[{PkMessages2025.AUDIO_SPECIFIC_COMPONENTS_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}생성수={created_count}개 {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
        
        return {
            'created_count': created_count,
            'total_expressions': len(time_expressions)
        }
        
    except Exception as e:
        ensure_printed(f"[{PkMessages2025.AUDIO_TIME_EXPRESSION_FAILED}] {PK_ANSI_COLOR_MAP['RED']}오류={e} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
        return None


def ensure_time_wav_components():
    """시간 관련 WAV 구성 요소가 모두 존재하는지 확인하고 없으면 생성"""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'AUDIO_WAV_COMPONENTS_START': '시간 관련 WAV 구성 요소 생성 시작',
                'AUDIO_ALL_COMPONENTS_EXIST': '모든 시간 구성 요소가 존재합니다',
                'AUDIO_MISSING_COMPONENTS': '누락된 구성 요소들이 있습니다. 생성을 시작합니다',
                'AUDIO_ALL_COMPONENTS_COMPLETE': '모든 시간 구성 요소 생성이 완료되었습니다',
                'AUDIO_SOME_COMPONENTS_FAILED': '일부 구성 요소 생성에 실패했습니다'
            })()

        from pkg_py.system_object.directories import D_PKG_IMAGE_AND_VIDEO_AND_SOUND
        
        ensure_printed(f"[{PkMessages2025.AUDIO_WAV_COMPONENTS_START}]", print_color='cyan')
        
        # 필요한 구성 요소 목록
        required_components = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
            "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
            "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
            "40", "41", "42", "43", "44", "45", "46", "47", "48", "49",
            "50", "51", "52", "53", "54", "55", "56", "57", "58", "59",
            "시", "분", "초", "시간", "분간", "초간",
            "오전", "오후", "아침", "점심", "저녁", "밤",
            "지금", "이제", "곧", "잠시", "조금", "많이"
        ]
        
        # 누락된 구성 요소 확인
        missing_components = []
        for component in required_components:
            filename = f"{component}.wav"
            file_path = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, filename)
            if not os.path.exists(file_path):
                missing_components.append(component)
        
        if not missing_components:
            ensure_printed(f"[{PkMessages2025.AUDIO_ALL_COMPONENTS_EXIST}]", print_color='green')
            return True
        else:
            ensure_printed(f"[{PkMessages2025.AUDIO_MISSING_COMPONENTS}]", print_color='yellow')
            
            # 누락된 구성 요소 생성
            success_count = 0
            failed_count = 0
            
            for component in missing_components:
                filename = f"{component}.wav"
                file_path = os.path.join(D_PKG_IMAGE_AND_VIDEO_AND_SOUND, filename)
                
                try:
                    # 간단한 비프음 생성 (1초, 440Hz)
                    audio = AudioSegment.sine(frequency=440, duration=1000)
                    audio.export(file_path, format="wav")
                    success_count += 1
                except Exception as e:
                    failed_count += 1
            
            if failed_count == 0:
                ensure_printed(f"[{PkMessages2025.AUDIO_ALL_COMPONENTS_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}성공={success_count}개 {PK_ANSI_COLOR_MAP['RESET']}", print_color='green')
                return True
            else:
                ensure_printed(f"[{PkMessages2025.AUDIO_SOME_COMPONENTS_FAILED}] {PK_ANSI_COLOR_MAP['RED']}성공={success_count}개 실패={failed_count}개 {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
                return False
                
    except Exception as e:
        ensure_printed(f"[{PkMessages2025.AUDIO_SOME_COMPONENTS_FAILED}] {PK_ANSI_COLOR_MAP['RED']}오류={e} {PK_ANSI_COLOR_MAP['RESET']}", print_color='red')
        return False 