

def get_key_public(**config_remote_os):
    import os.path
    local_ssh_public_key = config_remote_os['local_ssh_public_key']

    if not os.path.exists(local_ssh_public_key):
        raise FileNotFoundError(f"PUBLIC KEY NOT FOUND AT {local_ssh_public_key}")
    with open(local_ssh_public_key, "r") as f_obj:
        key_public = f_obj.read().strip()
