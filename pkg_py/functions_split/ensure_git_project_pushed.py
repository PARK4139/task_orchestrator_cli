
#             "add: new feature for ~~",
#             "chore: update dependencies",
#             "chore: various improvements and updates across multiple files",
#             "docs: update README.md and improved project documentation",
#             "feat: add user profile page",
#             "fix: resolve issue with ~~",
#             "refactor: improve code readability in user module",
#             "refactor: improve code readability in ~~",
#             "refactor: restructure and update multiple files with improved messages and translations",
#             f"feat: auto pushed (made savepoint) by {SCRIPT_NAME} at {get_time_as_("%Y-%m-%d %H:%M")}",
# 0. git config set
# 1. git add
# 2. git commit
# 3. git push
# git commit msg templates
SCRIPT_NAME = Path(__file__).name
cmd = "git add ."
cmd = "git push"
cmd = f'git commit -m "{commit_message}"'
cmd = f'git config --global user.email "{user_email}"'
cmd = f'git config --global user.name "{user_name}"'
code, output = run_command(cmd, capture_output=True)
commit_message = None
commit_message = f"feat: auto pushed (made savepoint) by {SCRIPT_NAME} at {get_time_as_("%Y-%m-%d %H:%M")}"
commit_message = f"feat: auto pushed (made savepoint) by {SCRIPT_NAME}"
commit_message = input("commit_message=").strip()
commit_message = value
commit_number = get_next_commit_number()
def ensure_git_project_pushed(with_commit_massage=True):
duration = time.time() - start_time
editable = False
editable = True  # pk_option
elif "everything up-to-date" in output.lower():
else:
except:
fail_and_exit(start_time)
file_id = get_file_id(key_name, func_n)
func_n = inspect.currentframe().f_code.co_name
global step_counter
if LTA:
if any(protocol in output for protocol in ["To https://", "To http://", "To git@"]):
if commit_message == "":
if len(user_email.strip()) == 0:
if len(user_name.strip()) == 0:
if status == "FAILED":
if with_commit_massage == False:
key_name = "commit_message"
key_name = 'commit_message'
pass
pk_print(f'''[{PkMessages2025.DATA}] value={value} {'%%%FOO%%%' if LTA else ''}''')
pk_print(f'''commit_message={commit_message} {'%%%FOO%%%' if LTA else ''}''')
print(PK_UNDERLINE)
print(f"LOCAL LEPO : {PK_ANSI_COLOR_MAP['GREEN']}{os.getcwd()}{PK_ANSI_COLOR_MAP['RESET']}")
print(f"STARTED AT : {PK_ANSI_COLOR_MAP['GREEN']}{time.strftime('%Y-%m-%d %H:%M:%S')}{PK_ANSI_COLOR_MAP['RESET']}")
print(f"{PK_ANSI_COLOR_MAP['GREEN']}ALL PROCESS COMPLETED SUCCESSFULLY. TOTAL EXECUTION TIME: {duration:.2f} SECONDS {PK_ANSI_COLOR_MAP['RESET']}")
print(output.strip())
set_text_from_history_file("user_email", user_email)
set_text_from_history_file("user_name", user_name)
start_time = time.time()
status = print_status(step_counter + 1, cmd, code, output)
step_counter += 1
try:
user_email = get_text_from_history_file("user_email") or ""
user_email = input("user_email=").strip()
user_name = get_text_from_history_file("user_name") or ""
user_name = input("user_name=").strip()
value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=[], editable=editable)
value = value or ""
