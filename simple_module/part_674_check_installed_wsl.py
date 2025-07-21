from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def check_installed_wsl():
    import subprocess
    import re

    def clean_line(line: str) -> str:
        return ''.join(line.strip().split())

    def get_wsl_distro_n_list() -> list[str]:

        try:
            result = subprocess.run(['wsl', '--list', '--quiet'], capture_output=True)
            output = result.stdout.decode('utf-16')
            return [line.replace(" ", "") for line in output.splitlines() if line.strip()]
        except Exception as e:
            pk_print(f"Failed to get WSL names: {e}", print_color='red')
            return []

    state_wsl_installed = None
    wsl_cmd_map_dict = {}
    wsl_distro_n_list = get_wsl_distro_n_list()
    if not wsl_distro_n_list:
        pk_print("No WSL distros found.", print_color='yellow')
        state_wsl_installed = 0
        return state_wsl_installed, wsl_cmd_map_dict

    wsl_cmd_map_dict["wsl state"] = ["wsl", "-l", "-v"]
    std_list = get_wsl_distro_info_std_list()
    for idx, name in enumerate(wsl_distro_n_list):
        matched_line = next((line for line in std_list if name.replace(" ", "") in clean_line(line)), "")
        state = "Unknown"
        version = "?"
        if matched_line:
            tokens = clean_line(matched_line)
            if "Running" in tokens:
                state = "Running"
            elif "Stopped" in tokens:
                state = "Stopped"
            match = re.search(r'(?:Running|Stopped)(\d)', tokens)
            if match:
                version = match.group(1)

        cmd_key = f"wsl {idx}"
        cmd_value = ["wsl", "-d", name]
        wsl_cmd_map_dict[cmd_key] = cmd_value
        if LTA:
            pk_print(f"Added: {cmd_key} = {cmd_value} ({state}, v{version})")
        state_wsl_installed = 1

    # shutdown 명령 수동 등록
    wsl_cmd_map_dict["wsl shutdown"] = ["wsl", "--shutdown"]

    return state_wsl_installed, wsl_cmd_map_dict
