
)
["powershell", "-command", "Get-Clipboard"],
capture_output=True, text=True, check=True
def get_clipboard_text():
except Exception as e:
import subprocess
result = subprocess.run(
return f"[ERROR] 클립보드 읽기 실패: {e}"
return result.stdout.strip()
try:
