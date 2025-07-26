


def print_status(step_num: int, cmd: str, code: int, output: str) -> str:
    from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
    if code == 0:
        label, color = "SUCCESS", PK_ANSI_COLOR_MAP['GREEN']
    elif "nothing to commit" in output.lower():
        label, color = "SKIPPED", PK_ANSI_COLOR_MAP['YELLOW']
    elif "everything up-to-date" in output.lower():
        label, color = "SKIPPED", PK_ANSI_COLOR_MAP['YELLOW']
    else:
        label, color = "FAILED", PK_ANSI_COLOR_MAP['RED']

    print(f"[ {color}{label}{PK_ANSI_COLOR_MAP['RESET']} ] [{step_num}] {cmd}")
    return label


