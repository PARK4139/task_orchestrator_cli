def get_clipboard_text():
    try:
        import subprocess
        result = subprocess.run(
            ["powershell", "-command", "Get-Clipboard"],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"[ERROR] 클립보드 읽기 실패: {e}"


