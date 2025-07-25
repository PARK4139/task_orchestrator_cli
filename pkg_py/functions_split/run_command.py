
def run_command(cmd: str, capture_output=False):
else:
except Exception as e:
if capture_output:
result = subprocess.run(cmd, shell=True)
result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
return 1, str(e)
return result.returncode, ""
return result.returncode, result.stdout + result.stderr
try:
