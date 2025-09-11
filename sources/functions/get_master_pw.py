import logging

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_master_pw():
    from pathlib import Path

    from sources.functions import ensure_pnx_made
    from sources.functions.ensure_str_writen_to_f import ensure_str_writen_to_f
    from sources.functions.get_str_from_file import get_str_from_file
    from sources.objects.task_orchestrator_cli_directories import D_PK_RECYCLE_BIN
    from sources.objects.pk_local_test_activate import LTA

    if LTA:
        while True:
            pk_security_file = D_PK_RECYCLE_BIN / "5sym.txt"
            if not pk_security_file.exists():
                ensure_pnx_made(pk_security_file, mode='f')
                logging.debug("type your master_password")
                master_password = input("master_password(5th sym pw)=").strip()
                ensure_str_writen_to_f(msg=master_password, f=pk_security_file)
            else:
                master_password = get_str_from_file(pnx=pk_security_file).strip()
                logging.debug(f"master_password={master_password}")
                if not master_password:
                    continue
                else:
                    return master_password
    else:
        while True:
            logging.debug("type your master_password")
            master_password = input("master_password(5th sym pw)=").strip()
            logging.debug(f"master_password={master_password}")
            if not master_password:
                continue
            else:
                return master_password