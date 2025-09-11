from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.functions.ensure_taskbar_pinned_removed import ensure_taskbar_pinned_removed


@ensure_seconds_measured
def ensure_file_lnk_created() -> None:
    import os

    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES, D_TASK_ORCHESTRATOR_CLI
    from sources.objects.task_orchestrator_cli_files import F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD

    """바로가기 생성 함수 - 작업표시줄 제거 기능 포함"""
    
    # 1단계: 기존 작업표시줄 고정 제거
    print("1단계: 작업표시줄에서 기존 task_orchestrator_cli_launcher 제거 중...")
    if ensure_taskbar_pinned_removed("task_orchestrator_cli_launcher"):
        print(" 작업표시줄 제거 완료")
    else:
        print("️ 작업표시줄 제거 실패 (계속 진행)")
    
    # 잠시 대기 (작업표시줄 변경사항 반영)
    import time
    time.sleep(1)
    
    try:
        import win32com.client

        # F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED 파일이 존재하는지 확인
        if not os.path.exists(F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD):
            print(f"경고: {F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD} 파일이 존재하지 않습니다.")
            print("바로가기 생성을 건너뜁니다.")
            return

        shell = win32com.client.Dispatch("WScript.Shell")

        # 2단계: 바탕화면 바로가기 생성
        print("2단계: 바탕화면 바로가기 생성 중...")
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            if os.path.exists(desktop):
                shortcut_path = os.path.join(desktop, "task_orchestrator_cli_launcher.lnk")
                
                # 기존 바로가기 파일이 있다면 삭제
                if os.path.exists(shortcut_path):
                    try:
                        os.remove(shortcut_path)
                        print(f"기존 바탕화면 바로가기 삭제됨: {shortcut_path}")
                    except Exception as e:
                        print(f"기존 바탕화면 바로가기 삭제 실패: {e}")
                        # 삭제 실패 시에도 계속 진행
                
                shortcut = shell.CreateShortCut(shortcut_path)
                shortcut.Targetpath = str(F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD)
                
                # WorkingDirectory를 정확한 task_orchestrator_cli 루트 디렉토리로 설정
                # D_TASK_ORCHESTRATOR_CLI이 상대 경로일 수 있으므로 절대 경로로 변환
                if os.path.isabs(D_TASK_ORCHESTRATOR_CLI):
                    working_dir = D_TASK_ORCHESTRATOR_CLI
                else:
                    # 상대 경로인 경우 현재 디렉토리 기준으로 절대 경로 생성
                    working_dir = os.path.abspath(D_TASK_ORCHESTRATOR_CLI)
                
                # 경로가 올바른지 확인하고 수정
                if not os.path.exists(working_dir):
                    print(f"경고: D_TASK_ORCHESTRATOR_CLI 경로가 존재하지 않습니다: {working_dir}")
                    # 현재 스크립트 위치에서 task_orchestrator_cli 루트 찾기
                    current_dir = os.getcwd()
                    if "task_orchestrator_cli" in current_dir:
                        # 현재 디렉토리가 task_orchestrator_cli 하위인 경우
                        task_orchestrator_cli_root = current_dir[:current_dir.find("task_orchestrator_cli") + len("task_orchestrator_cli")]
                        working_dir = task_orchestrator_cli_root
                    else:
                        # USERPROFILE\Downloads\task_orchestrator_cli 경로 사용
                        working_dir = os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads', 'task_orchestrator_cli')
                
                # Windows 경로 형식으로 변환 (백슬래시 사용)
                working_dir = working_dir.replace('/', '\\')
                
                shortcut.WorkingDirectory = working_dir
                shortcut.save()
                print(f" 바탕화면 바로가기 생성됨: {shortcut_path}")
                print(f"  - 대상: {F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD}")
                print(f"  - 작업 디렉토리: {working_dir}")
                print(f"  - 작업 디렉토리 존재 여부: {os.path.exists(working_dir)}")
            else:
                print("바탕화면 경로를 찾을 수 없습니다.")
        except Exception as e:
            print(f"바탕화면 바로가기 생성 실패: {e}")

        # 3단계: 작업 디렉토리 바로가기 생성
        print("3단계: 작업 디렉토리 바로가기 생성 중...")
        try:
            shortcut_path = os.path.join(D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES, "task_orchestrator_cli_launcher.lnk")
            
            # 기존 바로가기 파일이 있다면 삭제
            if os.path.exists(shortcut_path):
                try:
                    os.remove(shortcut_path)
                    print(f"기존 작업 디렉토리 바로가기 삭제됨: {shortcut_path}")
                except Exception as e:
                    print(f"기존 작업 디렉토리 바로가기 삭제 실패: {e}")
                    # 삭제 실패 시에도 계속 진행
            
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = str(F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD)
            
            # WorkingDirectory를 정확한 task_orchestrator_cli 루트 디렉토리로 설정
            # D_TASK_ORCHESTRATOR_CLI이 상대 경로일 수 있으므로 절대 경로로 변환
            if os.path.isabs(D_TASK_ORCHESTRATOR_CLI):
                working_dir = D_TASK_ORCHESTRATOR_CLI
            else:
                # 상대 경로인 경우 현재 디렉토리 기준으로 절대 경로 생성
                working_dir = os.path.abspath(D_TASK_ORCHESTRATOR_CLI)
            
            # 경로가 올바른지 확인하고 수정
            if not os.path.exists(working_dir):
                print(f"경고: D_TASK_ORCHESTRATOR_CLI 경로가 존재하지 않습니다: {working_dir}")
                # 현재 스크립트 위치에서 task_orchestrator_cli 루트 찾기
                current_dir = os.getcwd()
                if "task_orchestrator_cli" in current_dir:
                    # 현재 디렉토리가 task_orchestrator_cli 하위인 경우
                    task_orchestrator_cli_root = current_dir[:current_dir.find("task_orchestrator_cli") + len("task_orchestrator_cli")]
                    working_dir = task_orchestrator_cli_root
                else:
                    # USERPROFILE\Downloads\task_orchestrator_cli 경로 사용
                    working_dir = os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads', 'task_orchestrator_cli')
            
            # Windows 경로 형식으로 변환 (백슬래시 사용)
            working_dir = working_dir.replace('/', '\\')
            
            shortcut.WorkingDirectory = working_dir
            shortcut.save()
            print(f" 작업 디렉토리 바로가기 생성됨: {shortcut_path}")
            print(f"  - 대상: {F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD}")
            print(f"  - 작업 디렉토리: {working_dir}")
            print(f"  - 작업 디렉토리 존재 여부: {os.path.exists(working_dir)}")
        except Exception as e:
            print(f"작업 디렉토리 바로가기 생성 실패: {e}")

        # 4단계: 작업표시줄 고정 안내
        print("\n4단계: 작업표시줄 고정 안내")
        print(" 작업표시줄에 고정하려면:")
        print("   1. 바탕화면 바로가기 우클릭 → '작업 표시줄에 고정'")
        print("   2. 또는 바로가기를 작업표시줄로 드래그")
        print("   3. 고정 후 Win + 1 단축키로 빠른 실행 가능")

    except ImportError as e:
        print(f"win32com.client 모듈을 가져올 수 없습니다: {e}")
        print("바로가기 생성은 선택사항이므로 계속 진행합니다.")
    except Exception as e:
        print(f"바로가기 생성 중 예상치 못한 오류: {e}")
        print("바로가기 생성은 선택사항이므로 계속 진행합니다.")


# 직접 실행 시 테스트
if __name__ == "__main__":
    print("바로가기 생성 테스트 시작...")
    print(f"현재 작업 디렉토리: {os.getcwd()}")
    
    # 경로 확인
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES, D_TASK_ORCHESTRATOR_CLI
    from sources.objects.task_orchestrator_cli_files import F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD
    
    print(f"D_TASK_ORCHESTRATOR_CLI: {D_TASK_ORCHESTRATOR_CLI}")
    print(f"D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES: {D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES}")
    print(f"F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED: {F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD}")
    print(f"F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED 존재 여부: {os.path.exists(F_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_CMD)}")
    
    # 바로가기 생성 실행
    ensure_file_lnk_created()
    print("바로가기 생성 테스트 완료.")
