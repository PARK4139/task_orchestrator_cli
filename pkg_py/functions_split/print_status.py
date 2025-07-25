
def print_status(step_num: int, cmd: str, code: int, output: str) -> str:
elif "everything up-to-date" in output.lower():
elif "nothing to commit" in output.lower():
else:
if code == 0:
label, color = "FAILED", PK_ANSI_COLOR_MAP['RED']
label, color = "SKIPPED", PK_ANSI_COLOR_MAP['YELLOW']
label, color = "SUCCESS", PK_ANSI_COLOR_MAP['GREEN']
print(f"[ {color}{label}{PK_ANSI_COLOR_MAP['RESET']} ] [{step_num}] {cmd}")
return label
