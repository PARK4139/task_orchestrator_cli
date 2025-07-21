def get_remote_tree(d_path, **config_remote_os):
    ip = config_remote_os['ip']
    user_n = config_remote_os['user_n']
    pw = config_remote_os['pw']

    from paramiko import SSHClient, AutoAddPolicy
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=ip, username=user_n, password=pw)

    cmd = f"find {d_path}"
    stdin, stdout, stderr = ssh.exec_command(cmd)
    tree_output = stdout.read().decode()
    ssh.close()
    return tree_output
