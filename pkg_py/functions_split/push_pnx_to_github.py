def push_pnx_to_github(d_working, git_repo_url, commit_msg, branch_n):
    import os

    from pkg_py.functions_split import ensure_pnx_made
    from pkg_py.functions_split.is_internet_connected import is_internet_connected

    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed
    ensure_printed(f'''commit_msg={commit_msg} {'%%%FOO%%%' if LTA else ''}''')
    if not is_internet_connected():
        return
    if not does_pnx_exist(pnx=d_working):
        ensure_pnx_made(pnx=d_working, mode='d')
    os.chdir(d_working)
    git_local_repo_checkfile = rf"{d_working}/.git"
    std_list = None
    state_done = [0, 0, 0, 0]

    while 1:
        if state_done[0] == 0:
            if not does_pnx_exist(pnx=git_local_repo_checkfile):
                std_list = ensure_command_excuted_to_os(cmd=rf'git init')
                continue
        state_done[0] = 1
        ensure_printed(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[1] == 0:
            std_list = ensure_command_excuted_to_os(cmd=rf'git add .')  # git add * 과는 약간 다름.
            # signiture_list = ["The following paths are ignored by one of your .gitignore files:"]
            if not len(std_list) == 0:
                ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
                continue
            # if not any(str_working in std_list for str_working in signiture_list):
            #     continue
        state_done[1] = 1
        ensure_printed(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[2] == 0:
            std_list = ensure_command_excuted_to_os(cmd=rf'git commit -m "{commit_msg}"')
            std_list = ensure_command_excuted_to_os(cmd=rf'git commit -m "{commit_msg}"')
            signiture_list = ["nothing to commit, working tree clean"]
            if not any(str_working in std_list for str_working in signiture_list):
                ensure_printed(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
                continue
        state_done[2] = 1
        ensure_printed(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[3] == 0:
            std_list = ensure_command_excuted_to_os(cmd=rf'git push origin {branch_n}')
            signiture_list = ["Everything up-to-date", "branch 'main' set up to track 'origin/main'."]
            if not any(str_working in std_list for str_working in signiture_list):
                continue
        state_done[3] = 1
        ensure_printed(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        break
