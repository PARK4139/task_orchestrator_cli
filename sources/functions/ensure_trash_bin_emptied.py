from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_local_test_activate import LTA


@ensure_seconds_measured
def ensure_trash_bin_emptied():
    import os
    import platform
    import subprocess
    import logging
    import logging

    from sources.objects.pk_map_texts import PkTexts

    system_name = platform.system().lower()

    try:
        if system_name == "windows":
            # Windows 휴지통 비우기 (PowerShell)
            cmd = [
                "powershell",
                "-Command",
                'Clear-RecycleBin -Force -ErrorAction SilentlyContinue'
            ]
            subprocess.run(cmd, check=True)

        elif system_name == "linux":
            # Linux 휴지통 디렉토리 제거
            trash_dir = os.path.expanduser("~/.local/share/Trash")
            if os.path.exists(trash_dir):
                subprocess.run(["rm", "-rf", trash_dir], check=True)
                os.makedirs(trash_dir, exist_ok=True)

        elif system_name == "darwin":
            # macOS 휴지통 비우기
            subprocess.run(["rm", "-rf", os.path.expanduser("~/.Trash/*")], shell=True, check=True)

        else:
            logging.warning(f"[{PkTexts.OPERATION_FAILED}] 지원하지 않는 OS: {system_name}")
            return

        logging.debug(f"[{PkTexts.OPERATION_SUCCESS}] 휴지통이 비워졌습니다.")

    except Exception as e:
        logging.error(f"[{PkTexts.OPERATION_FAILED}] 휴지통 비우기 실패: {e}")


if __name__ == "__main__":
    if LTA:
        ensure_trash_bin_emptied()
