

from pkg_py.simple_module.part_014_pk_print import pk_print


def run_cmd(cmd):
    import subprocess

    """Run a shell cmd and return 1 if successful."""
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        pk_print(f"cmd failed: {cmd}, Error: {e}", print_color='red')
        return 0
