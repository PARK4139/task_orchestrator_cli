

def ensure_remote_os_connection(**config_remote_os):
    ip = config_remote_os['ip']
    while 1:
        if not ping(ip=ip):
            todo('%%%FOO%%%')
            continue
        if ping(ip=ip):
            break
