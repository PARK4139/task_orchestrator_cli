import win32con
import tomllib
from pkg_py.system_object.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def run_project_docker_base(f, dockerfile_script_list):
    import os

    # ensure wsl
    config_remote_os = {}
    wsl_distro_n = "Ubuntu-24.04"
    config_remote_os['os_distro_n'] = wsl_distro_n
    config_remote_os['ip'] = get_wsl_ip(wsl_distro_n)
    config_remote_os['port'] = ensure_and_get_wsl_port(wsl_distro_n)
    config_remote_os['user_n'] = get_wsl_user_n(wsl_distro_n)
    config_remote_os['pw'] = get_wsl_pw(wsl_distro_n)
    config_remote_os['local_ssh_public_key'] = os.path.join(D_HOME, ".ssh", "id_ed25519.pub")
    config_remote_os['local_ssh_private_key'] = os.path.expanduser("~/.ssh/id_ed25519")
    ensure_wsl_distro_installed(wsl_distro_n=wsl_distro_n)
    ensure_wsl_distro_session(wsl_distro_n=wsl_distro_n)

    ip = config_remote_os['ip']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']

    ensure_ssh_public_key_to_remote_os(**config_remote_os)
    ensure_remote_os_as_nopasswd(**config_remote_os)
    if LTA:
        ensure_printed(f'''{STAMP_TRY_GUIDE} ssh -p {port} {user_n}@{ip} {'%%%FOO%%%' if LTA else ''}''')

    # make dockerfile
    ensure_pnx_made(pnx=f, mode='f')

    # write dockerfile
    ensure_dockerfile_writen(f=f, f_dockerfile_script_list=dockerfile_script_list)

    # send dockerfile via scp
    cmd_to_remote_os(
        cmd=f'scp -av --delete -e "ssh -i ~/.ssh/id_ed25519" {D_PROJECT} {user_n}@{ip}:~/Downloads/{get_nx(D_PROJECT)}',
        **config_remote_os)
    # mkr. # todo

    # send dockerfile via rsync
    # install_ubuntu_pkg_to_remote_os_via_apt(ubuntu_pkg_n='rsync', **config_remote_os)
    D_PROJECT = get_pnx_wsl_unix_style(pnx=D_PROJECT_FASTAPI)
    # cmd_to_remote_os(cmd=f'rsync -av --delete -e "ssh -i ~/.ssh/id_ed25519" {d_project} {user_n}@{ip}:~/Downloads/{get_nx(d_project)}', **config_remote_os)
    # cmd_to_remote_os(cmd=f'rsync -av --delete {d_project} ~/Downloads/', **config_remote_os)

    # import ipdb
    # ipdb.set_trace()
    # while 1:
    #     # todo: 등록된 함수명 조회 with idx
    #     # print_pk_func_list_with_idx()
    #     # if user_cmd = "f 13":
    #     #     pk_copy(str_working=pk_input())
    #     import ipdb
    #     ipdb.set_trace()
    #     # ctrl v

    # install docker deamon
    # install_ubuntu_pkg_to_remote_os_via_apt(ubuntu_pkg_n='docker', **config_remote_os)

    # start docker deamon
    cmd_to_remote_os(cmd=f'sudo service docker start', **config_remote_os)

    # edit dockerfile
    # if LTA:
    #     cmd_to_os(cmd=rf'code "{f}"')

    # build docker
    f_nx = get_nx(f)
    f_n = get_n(f)
    f_docker_img_n = rf'{f_n}'
    f_docker_tag_version = rf''  # 생략 시 latest
    # f_docker_tag_version=rf':1.0'
    f_docker_tag_n = rf'{f_docker_img_n}{f_docker_tag_version}'
    cmd_to_remote_os(cmd=rf"docker build -t {f_docker_tag_n} -f ~/Downloads/{os.path.basename(D_PROJECT)}/{f_nx} .",
                     **config_remote_os)
    std_out_str, std_err_str = cmd_to_remote_os(cmd=rf"ls ~/Downloads/{os.path.basename(D_PROJECT)}/{f_nx}",
                                                **config_remote_os)
    ensure_printed(f'''std_out_str={std_out_str} {'%%%FOO%%%' if LTA else ''}''')
    raise
    # cmd_to_remote_os(cmd=rf"ls", **config_remote_os)
    # cmd_to_remote_os(cmd=rf"ls ~/Downloads/{os.path.basename(D_PROJECT)}/{f_nx}", **config_remote_os)
    # cmd_to_remote_os(cmd=rf"ls ~/Downloads/{os.path.basename(D_PROJECT)}/{f_nx}", **config_remote_os)
    # raise
    # cmd_to_remote_os(cmd=rf"pwd", **config_remote_os)

    # docker run
    f_n = get_n(f)
    docker_container_n = rf'{f_n}'
    cmd_list = [
        f"sudo docker run --rm -d \\",
        f"--name {docker_container_n} {f_docker_img_n} \\",
        # f"-p <로컬_포트>: <컨테이너_포트>\\",
        # f"-v ~/Downloads/mariadb_data:/var/lib/mysql \\",  # 볼륨 마운트
        # f"mariadb \\",  # exec 할 이미지 (선택적)
    ]
    cmd = get_str_from_list(working_list=cmd_list)
    cmd_to_remote_os(cmd=cmd, **config_remote_os)

    # check docker container
    # cmd_to_os(cmd=rf"wsl docker ps -a")  # 중지된 컨테이너 포함

    # 이 설정을 완료하면
    # WSL Docker deamon tcp://0.0.0.0:2375에서 외부 요청 수신대기
    config_content = """{
        "hosts": ["unix:///var/run/docker.sock", "tcp://0.0.0.0:2375"]
    }"""
    cmd_to_remote_os_with_pubkey(cmd=rf"sudo sh -c 'echo \"{config_content}\" | tee /etc/docker/daemon.json'",
                                 **config_remote_os)
    cmd_to_remote_os_with_pubkey(cmd=rf"sudo service docker restart", **config_remote_os)

    # wsl docker_ip
    std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(
        cmd=f"docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {docker_container_n}")  # 이거되나?
    # std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=f"docker inspect -f '{{{{range .NetworkSettings.Networks}}}}{{{{.IPAddress}}}}{{{{end}}}}' {f_docker_container_name}")
    docker_ip = std_out_list[0]
    ensure_printed(f'''docker_ip="{docker_ip}"  {'%%%FOO%%%' if LTA else ''}''')

    # wsl 내부 docker deamon 제어(wsl 외부에서)
    # Docker SDK # TCP로 노출 또는 Unix 소켓
    client = docker.DockerClient(base_url=rf"tcp://{docker_ip}:2375")  # Docker deamon 에 연결 (WSL 외부에서)
    print(client.info())  # Docker 정보 확인

    ensure_pnx_removed(f)

    # send_f(f=f_dockerfile, ip=xc)
