def push_pnx_to_github(d_working, git_repo_url, commit_msg, branch_n):
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.pk_print import pk_print
    pk_colorama_init_once()
    pk_print(f'''commit_msg={commit_msg} {'%%%FOO%%%' if LTA else ''}''')
    if not is_internet_connected():
        return
    if not does_pnx_exist(pnx=d_working):
        ensure_pnx_made(pnx=d_working, mode='d')
    pk_chdir(d_dst=d_working)
    d_git = rf"{d_working}/.git"
    std_list = None
    state_done = [0, 0, 0, 0]
    while 1:
        if state_done[0] == 0:
            if not does_pnx_exist(pnx=d_git):
                std_list = cmd_to_os(cmd=rf'git init')
                continue
        state_done[0] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[1] == 0:
            std_list = cmd_to_os(cmd=rf'git add .')  # git add * 과는 약간 다름.
            # signiture_list = ["The following paths are ignored by one of your .gitignore files:"]
            if not len(std_list) == 0:
                pk_print(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
                continue
            # if not any(str_working in std_list for str_working in signiture_list):
            #     continue
        state_done[1] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[2] == 0:
            std_list = cmd_to_os(cmd=rf'git commit -m "{commit_msg}"')
            std_list = cmd_to_os(cmd=rf'git commit -m "{commit_msg}"')
            signiture_list = ["nothing to commit, working tree clean"]
            if not any(str_working in std_list for str_working in signiture_list):
                pk_print(str_working=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')
                continue
        state_done[2] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        if state_done[3] == 0:
            std_list = cmd_to_os(cmd=rf'git push origin {branch_n}')
            signiture_list = ["Everything up-to-date", "branch 'main' set up to track 'origin/main'."]
            if not any(str_working in std_list for str_working in signiture_list):
                continue
        state_done[3] = 1
        pk_print(f'''state_done={state_done} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
        break
