

def ensure_remote_os_connection(**config_remote_os):
    ip = config_remote_os['ip']
    while 1:
        if not ensure_pinged(ip=ip):
            todo('%%%FOO%%%')
            continue
        if ensure_pinged(ip=ip):
            break
