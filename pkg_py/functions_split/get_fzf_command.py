def get_fzf_command():
    import subprocess

    for name in ["fzf", "fzf.exe"]:
        try:
            subprocess.run([name, "--version"], capture_output=True, check=True)
            return name
        except Exception:
            continue
    return None
