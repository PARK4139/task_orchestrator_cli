

from pkg_py.functions_split.ensure_printed import ensure_printed


def run_cmd(cmd):
    import subprocess

    """Run a shell cmd and return 1 if successful."""
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception as e:
        ensure_printed(f"cmd failed: {cmd}, Error: {e}", print_color='red')
        return 0
