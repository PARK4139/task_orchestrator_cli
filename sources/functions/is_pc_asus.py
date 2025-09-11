import traceback

from functions.check_hostname_match import check_hostname_match
from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def is_pc_asus():
    try:
        def is_pc_asus():
            """Checks if the current PC is the Anyang house desktop."""
            return check_hostname_match(target_hostname_value="pk", match_type="contains", pc_name_for_log="Anyang house PC")

        return True
    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        pass
