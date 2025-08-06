from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_file_lnk_created() -> None:
    import os

    from pkg_py.system_object.directories import D_PKG_WINDOWS, D_PK_SYSTEM
    from pkg_py.system_object.files import F_ALIAS_CMD

    """바로가기 생성 함수 - 더 안정적인 버전"""
    try:
        import win32com.client

        # F_ALIAS_CMD 파일이 존재하는지 확인
        if not os.path.exists(F_ALIAS_CMD):
            print(f"경고: {F_ALIAS_CMD} 파일이 존재하지 않습니다.")
            print("바로가기 생성을 건너뜁니다.")
            return

        shell = win32com.client.Dispatch("WScript.Shell")

        # 바탕화면 바로가기 생성
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            if os.path.exists(desktop):
                shortcut_path = os.path.join(desktop, "pk_system_launcher.lnk")
                shortcut = shell.CreateShortCut(shortcut_path)
                shortcut.Targetpath = F_ALIAS_CMD
                shortcut.WorkingDirectory = D_PK_SYSTEM
                shortcut.save()
                print(f"바탕화면 바로가기 생성됨: {shortcut_path}")
            else:
                print("바탕화면 경로를 찾을 수 없습니다.")
        except Exception as e:
            print(f"바탕화면 바로가기 생성 실패: {e}")

        # 작업 디렉토리 바로가기 생성
        try:
            shortcut_path = os.path.join(D_PKG_WINDOWS, "pk_system_launcher.lnk")
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = F_ALIAS_CMD
            shortcut.WorkingDirectory = D_PK_SYSTEM
            shortcut.save()
            print(f"작업 디렉토리 바로가기 생성됨: {shortcut_path}")
        except Exception as e:
            print(f"작업 디렉토리 바로가기 생성 실패: {e}")

    except ImportError as e:
        print(f"win32com.client 모듈을 가져올 수 없습니다: {e}")
        print("바로가기 생성은 선택사항이므로 계속 진행합니다.")
    except Exception as e:
        print(f"바로가기 생성 중 예상치 못한 오류: {e}")
        print("바로가기 생성은 선택사항이므로 계속 진행합니다.")
