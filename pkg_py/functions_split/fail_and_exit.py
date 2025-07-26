import sys
import time

from pkg_py.functions_split.run_command import run_command
from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP


def fail_and_exit(start_time):
    print(f"\n{PK_ANSI_COLOR_MAP['RED']}[!] Aborting further steps. Current git status:{PK_ANSI_COLOR_MAP['RESET']}")
    _, status_out = run_command("git status", capture_output=True)
    print(status_out.strip())
    duration = time.time() - start_time
    print(f"{PK_ANSI_COLOR_MAP['RED']}process failed at {time.strftime('%Y-%m-%d %H:%M:%S')} (elapsed {duration:.2f} sec){PK_ANSI_COLOR_MAP['RESET']}")
    sys.exit(1)
