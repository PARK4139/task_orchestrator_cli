step_counter = 1


def ensure_git_project_pushed(with_commit_massage=True):
    import inspect
    import os
    import time
    from pathlib import Path

    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.fail_and_exit import fail_and_exit
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_next_commit_number import get_next_commit_number
    from pkg_py.functions_split.get_text_from_history_file import get_text_from_history_file
    from pkg_py.functions_split.get_time_as_ import get_time_as_
    from pkg_py.functions_split.get_value_via_fzf_or_history_routine import get_value_via_fzf_or_history_routine
    from pkg_py.functions_split.print_status import print_status
    from pkg_py.functions_split.run_command import run_command
    from pkg_py.functions_split.set_text_from_history_file import set_text_from_history_file
    from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
    from pkg_py.system_object.etc import PK_UNDERLINE
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025

    SCRIPT_NAME = Path(__file__).name
    func_n = inspect.currentframe().f_code.co_name

    global step_counter
    start_time = time.time()
    print(PK_UNDERLINE)
    print(f"LOCAL LEPO : {PK_ANSI_COLOR_MAP['GREEN']}{os.getcwd()}{PK_ANSI_COLOR_MAP['RESET']}")
    print(f"STARTED AT : {PK_ANSI_COLOR_MAP['GREEN']}{time.strftime('%Y-%m-%d %H:%M:%S')}{PK_ANSI_COLOR_MAP['RESET']}")

    # 0. git config set
    user_email = get_text_from_history_file("user_email") or ""
    user_name = get_text_from_history_file("user_name") or ""

    if len(user_email.strip()) == 0:
        user_email = input("user_email=").strip()
        cmd = f'git config --global user.email "{user_email}"'
        code, output = run_command(cmd, capture_output=True)
        print(output.strip())
        set_text_from_history_file("user_email", user_email)
        status = print_status(step_counter + 1, cmd, code, output)
        if status == "FAILED":
            fail_and_exit(start_time)
        step_counter += 1

    if len(user_name.strip()) == 0:
        user_name = input("user_name=").strip()
        cmd = f'git config --global user.name "{user_name}"'
        code, output = run_command(cmd, capture_output=True)
        print(output.strip())
        set_text_from_history_file("user_name", user_name)
        status = print_status(step_counter + 1, cmd, code, output)
        if status == "FAILED":
            fail_and_exit(start_time)
        step_counter += 1

    # 1. git add
    print(PK_UNDERLINE)
    cmd = "git add ."
    code, output = run_command(cmd, capture_output=True)
    print(output.strip())
    status = print_status(step_counter + 1, cmd, code, output)
    if status == "FAILED":
        fail_and_exit(start_time)
    step_counter += 1

    # 2. git commit
    print(PK_UNDERLINE)
    commit_number = get_next_commit_number()
    commit_message = None
    if with_commit_massage == False:
        commit_message = f"feat: auto pushed (made savepoint) by {SCRIPT_NAME} at {get_time_as_("%Y-%m-%d %H:%M")}"
    else:
        key_name = "commit_message"
        try:
            key_name = 'commit_message'
            func_n = inspect.currentframe().f_code.co_name
            file_id = get_file_id(key_name, func_n)
            if LTA:
                editable = True  # pk_option
            else:
                editable = False
            value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=[], editable=editable)
            ensure_printed(f'''[{PkMessages2025.DATA}] value={value} {'%%%FOO%%%' if LTA else ''}''')
            value = value or ""
            commit_message = value
            if commit_message == "":
                commit_message = f"feat: auto pushed (made savepoint) by {SCRIPT_NAME} at {get_time_as_("%Y-%m-%d %H:%M")}"
            ensure_printed(f'''commit_message={commit_message} {'%%%FOO%%%' if LTA else ''}''')
        except:
            commit_message = input("commit_message=").strip()
            if commit_message == "":
                commit_message = f"feat: auto pushed (made savepoint) by {SCRIPT_NAME}"
            ensure_printed(f'''commit_message={commit_message} {'%%%FOO%%%' if LTA else ''}''')

    cmd = f'git commit -m "{commit_message}"'
    code, output = run_command(cmd, capture_output=True)
    print(output.strip())
    status = print_status(step_counter + 1, cmd, code, output)
    if status == "FAILED":
        fail_and_exit(start_time)
    step_counter += 1

    # 3. git push
    print(PK_UNDERLINE)
    cmd = "git push"
    code, output = run_command(cmd, capture_output=True)
    print(output.strip())
    status = print_status(step_counter + 1, cmd, code, output)
    if status == "FAILED":
        fail_and_exit(start_time)
    step_counter += 1

    print(PK_UNDERLINE)
    if any(protocol in output for protocol in ["To https://", "To http://", "To git@"]):
        pass
    elif "everything up-to-date" in output.lower():
        pass
    else:
        fail_and_exit(start_time)

    duration = time.time() - start_time
    print(f"{PK_ANSI_COLOR_MAP['GREEN']}ALL PROCESS COMPLETED SUCCESSFULLY. TOTAL EXECUTION TIME: {duration:.2f} SECONDS {PK_ANSI_COLOR_MAP['RESET']}")

    return {
        "state": True
    }
