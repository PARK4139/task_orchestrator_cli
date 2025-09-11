from typing import Optional


# @ensure_seconds_measured
def ensure_command_executed(cmd: str, mode: str = "sync", encoding: Optional[str] = None, mode_with_window: bool = True, errors: Optional[str] = None):
    from functions.get_caller_n import get_caller_n
    from functions.log_aligned import log_aligned
    from objects.pk_etc import PK_UNDERLINE

    import subprocess
    import logging
    import traceback

    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.encodings import Encoding
    from sources.functions.is_os_windows import is_os_windows

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    gap = len(func_n)  # 가장 긴 key 길이
    logging.debug(PK_UNDERLINE)
    # log_aligned(gap=gap, key="", PK_UNDERLINE)    value=
    # log_aligned(gap=gap, key=rf"{func_n}()", PK_UNDERLINE)    value=

    if mode == 'a':
        mode = 'async'

    if encoding is None:
        encoding = Encoding.UTF8.value
    if hasattr(encoding, 'value'):
        encoding = encoding.value

    if LTA:
        log_aligned(gap=gap, key="cmd", value=cmd)
        log_aligned(gap=gap, key="mode", value=mode)
        log_aligned(gap=gap, key="encoding", value=encoding)
        log_aligned(gap=gap, key="mode_with_window", value=str(mode_with_window))

    popen_kwargs = {"shell": True}
    if is_os_windows():
        if not mode_with_window:
            popen_kwargs["creationflags"] = subprocess.CREATE_NO_WINDOW
    elif mode == "async" and not mode_with_window:
        popen_kwargs["stdout"] = subprocess.DEVNULL
        popen_kwargs["stderr"] = subprocess.DEVNULL

    if mode == "async":
        subprocess.Popen(cmd, **popen_kwargs)
        return None

    try:
        process = subprocess.run(
            cmd,
            capture_output=True,
            text=True,  # Let subprocess handle decoding
            encoding=encoding,  # Pass the determined encoding
            errors=errors,  # Pass the errors argument
            **popen_kwargs
        )

        stdout = process.stdout
        stderr = process.stderr

        stdout_lines = process.stdout.splitlines() if process.stdout else []
        stderr_lines = process.stderr.splitlines() if process.stderr else []

        if stdout_lines:
            for idx, line in enumerate(stdout_lines):
                log_aligned(gap=gap, key=f"LINE {idx}", value=f"{line:<100}")
        else:
            # log_aligned(gap=gap, key="(empty stdout)")    value=
            pass

        if stderr_lines:
            for idx, line in enumerate(stderr_lines):
                log_aligned(gap=gap, key=f"LINE {idx}", value=f"{line:<100}")

        return stdout_lines, stderr_lines # Return two lists

    except FileNotFoundError:
        logging.error(f"Command not found: {cmd.split()[0]}")
        return [], [] # Return two empty lists on FileNotFoundError
    except Exception:
        logging.error(f"An error occurred while executing '{cmd}':")
        logging.error(traceback.format_exc())
        return [], [] # Return two empty lists on other exceptions
