from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_installed_wsl_distros():
    import subprocess
    import re
    try:
        result = subprocess.run(['wsl', '-l', '-v'], capture_output=True)
        output = result.stdout.decode('utf-16')
        std_list = output.splitlines()
        for std_str in std_list:
            if LTA:
                pk_print(std_str)
        distros = []
        for line in std_list[1:]:
            line = line.strip()
            if not line:
                continue
            if line.startswith("*"):
                line = line[1:].strip()
            parts = re.split(r'\s{2,}', line)
            if LTA:
                pk_print(f'''parts={parts} {'%%%FOO%%%' if LTA else ''}''')
            if len(parts) >= 3:
                name, state, version = parts[0], parts[1], parts[2]
                distros.append({
                    'name': name.strip(),
                    'state': state.strip(),
                    'version': int(version.strip())
                })
        return distros
    except subprocess.CalledProcessError as e:
        pk_print(f"Failed to list WSL distros: {e}", print_color='red')
        return []
