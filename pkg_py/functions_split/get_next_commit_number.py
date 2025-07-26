


def get_next_commit_number():
    import re

    from pkg_py.functions_split.run_command import run_command
    code, log_output = run_command('git log -n 20 --pretty=format:%s', capture_output=True)
    if code != 0:
        return 1
    numbers = []
    for line in log_output.splitlines():
        match = re.match(r"\[(\d+)\]", line)
        if match:
            numbers.append(int(match.group(1)))
    return max(numbers, default=0) + 1


