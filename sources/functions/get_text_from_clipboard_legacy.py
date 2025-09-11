import traceback
from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

@ensure_seconds_measured
def get_text_from_clipboard_legacy():
    import logging

    from functions.get_str_from_tuple import get_str_from_tuple
    from sources.functions.is_os_windows import is_os_windows

    from sources.functions.ensure_command_executed import ensure_command_executed

    if is_os_windows():
        results = ensure_command_executed('powershell.exe Get-Clipboard')
        logging.debug(f'type(results)={type(results)}')
        if isinstance(results, str):
            return results
        elif isinstance(results, list):
            for result in results:
                logging.debug("way1: powershell.exe Get-Clipboard list")
                logging.debug(rf"result={result}")
            return results.__str__()
        elif isinstance(results, tuple):
            for result in results:
                logging.debug("way1: powershell.exe Get-Clipboard list")
                logging.debug(rf"result={result}")
            return get_str_from_tuple(results, separator='\n')
        else:
            return ""
    else:
        try:
            import clipboard
            logging.debug("way3 : clipboard.paste()")
            return clipboard.paste()
        except ImportError:
            # clipboard 모듈이 없는 경우 빈 문자열 반환
            return ""
