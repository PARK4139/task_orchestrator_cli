
code, log_output = run_command('git log -n 20 --pretty=format:%s', capture_output=True)
def get_next_commit_number():
for line in log_output.splitlines():
if code != 0:
if match:
match = re.match(r"\[(\d+)\]", line)
numbers = []
numbers.append(int(match.group(1)))
return 1
return max(numbers, default=0) + 1
