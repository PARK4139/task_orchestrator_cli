def ensure_wsl_distro_session(wsl_distro_name):
    import logging
    import time # Added import

    from functions.is_wsl_distro_started import is_wsl_distro_started
    from sources.functions.is_os_windows import is_os_windows
    from sources.functions.is_os_wsl_linux import is_os_wsl_linux
    from sources.objects.pk_local_test_activate import LTA
    import subprocess

    logging.debug(f"Attempting to ensure WSL distro session for: {wsl_distro_name}")

    if is_os_windows():
        if not is_os_wsl_linux():
            if not is_wsl_distro_started(wsl_distro_name):
                logging.debug(f"WSL distro {wsl_distro_name} is not started. Attempting to start it.")
                subprocess.Popen(f"wsl -d {wsl_distro_name}", creationflags=subprocess.CREATE_NO_WINDOW)

                # Add retry mechanism to wait for WSL to start
                max_retries = 10
                retry_delay = 1  # seconds
                started = False
                for i in range(max_retries):
                    logging.debug(f"Checking if WSL distro {wsl_distro_name} started (attempt {i+1}/{max_retries})...")
                    if is_wsl_distro_started(wsl_distro_name):
                        started = True
                        logging.debug(f"WSL distro {wsl_distro_name} successfully started.")
                        break
                    time.sleep(retry_delay)
                
                if not started:
                    logging.error(f"Failed to start WSL distro {wsl_distro_name} after {max_retries} attempts.")
                    raise RuntimeError(f"Failed to start WSL distro: {wsl_distro_name}")
            
            if is_wsl_distro_started(wsl_distro_name): # This check is redundant after the loop, but keeping for consistency with original logic
                logging.debug(        f'''{wsl_distro_name} is started already in wsl with keeping session {'%%%FOO%%%' if LTA else ''}''')
            else: # This else branch should ideally not be reached if the above logic is correct
                logging.debug(f'''{wsl_distro_name} is not started in wsl with keeping session {'%%%FOO%%%' if LTA else ''}''')
                raise RuntimeError(f"Failed to start WSL distro: {wsl_distro_name}")

    return True