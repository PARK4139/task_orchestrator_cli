from pkg_py.functions_split import get_time_as_
from pkg_py.functions_split.ensure_d_size_stable import ensure_d_size_stable
from pkg_py.functions_split.ensure_input_preprocessed import ensure_input_preprocessed
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.push_pnx_to_github import push_pnx_to_github
from pkg_py.system_object.local_test_activate import LTA





def assist_to_upload_pnx_to_git(d_working, git_repo_url, branch_n):
    ensure_printed(f'''d_working={d_working} {'%%%FOO%%%' if LTA else ''}''')
    loop_cnt = 1
    while 1:
        try:
            if loop_cnt == 1:
                commit_msg = ensure_input_preprocessed(str_working=f"commit_msg=", upper_seconds_limit=60,
                                                       return_default=f"feat: make save point by auto at {get_time_as_('%Y-%m-%d %H:%M')}")
                push_pnx_to_github(d_working=d_working, git_repo_url=git_repo_url, commit_msg=commit_msg,
                                   branch_n=branch_n)
                loop_cnt = loop_cnt + 1
            if not ensure_d_size_stable(d_working, limit_seconds=30):
                if ensure_d_size_stable(d_working, limit_seconds=30):
                    ensure_printed(" change stable after  change detected")
                    commit_msg = ensure_input_preprocessed(str_working=f"commit_msg=", upper_seconds_limit=60,
                                                           return_default=f"feat: make save point by auto at {get_time_as_('%Y-%m-%d %H:%M')}")
                    push_pnx_to_github(d_working=d_working, git_repo_url=git_repo_url, commit_msg=commit_msg,
                                       branch_n=branch_n)
        except:
            import traceback
            ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            break
