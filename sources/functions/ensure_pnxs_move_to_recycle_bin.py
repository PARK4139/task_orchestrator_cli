from pathlib import Path
from typing import List, Optional, Union

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pnxs_move_to_recycle_bin(pnxs: Optional[List[Union[str, Path]]]):
    import logging
    from pathlib import Path

    from sources.functions.ensure_pnx_moved import ensure_pnx_moved
    from sources.objects.task_orchestrator_cli_directories import D_PK_RECYCLE_BIN
    from sources.objects.pk_local_test_activate import LTA
    try:
        for pnx in pnxs:
            pnx = Path(pnx)
            if pnx.exists():
                logging.debug(f'''이동할 {pnx} is exist. {'%%%FOO%%%' if LTA else ''}''')
                D_PK_RECYCLE_BIN.mkdir(parents=True, exist_ok=True)
                ensure_pnx_moved(pnx=pnx, d_dst=D_PK_RECYCLE_BIN)
            else:
                logging.debug(f'''이동할 {pnx} is not existing. {'%%%FOO%%%' if LTA else ''}''')
    except:
        logging.debug("❌ An unexpected error occurred")
