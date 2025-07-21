from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os


def download_f_from_gitlab(f_nx_remote_src, d_local_dst, gitlab_repo_url):
    'gitlab_repo_url : 192.168...'

    while 1:
        pk_chdir(d_local_dst)
        cmd_to_os(cmd=f'git init')
        cmd = rf"git remote add -f origin http://{gitlab_repo_url}"
        std_list = cmd_to_os(cmd=cmd)

        cmd_to_os(cmd=f'git fetch')
        cmd_to_os(cmd=f'git checkout origin/main -- {f_nx_remote_src}')
        # cmd_to_os(cmd = f'git remote remove origin') # 로그인 실패시 # todo

        # todo
        # f_remote_src = 현재 디렉토리의 + f_nx_remote_src
        # if not does_pnx_exist(pnx=f_remote_src):
        #     continue
        # if does_pnx_exist(pnx=f_remote_src):
        #     break
