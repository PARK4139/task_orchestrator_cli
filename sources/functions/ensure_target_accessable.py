def ensure_target_accessable(target_device_data, **remote_device_target_config):
    from functions.ensure_target_ip import ensure_target_ip
    ensure_target_ip(target_device_data, **remote_device_target_config)
