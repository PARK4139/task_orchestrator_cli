import os
import subprocess
import sys
from datetime import datetime

# ANSI colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def log_step(step_msg):
    print(f"\n{YELLOW}pk_🟡 [Step Start] {step_msg} - {datetime.now().strftime('%H:%M:%S')}{RESET}")
    input(f"{YELLOW}  ⏎ Enter to continue...{RESET}")

def log_failure(step_msg, error_msg=None):
    print(f"{RED}pk_❌ [Failed] {step_msg}{RESET}")
    if error_msg:
        print(f"{RED}    pk_❌ Error message: {error_msg}{RESET}")
    sys.exit(1)

def log_success(msg):
    print(f"\n{GREEN}pk_✅ {msg}{RESET}")

def run(cmd, cwd=None, step_name=None):
    try:
        print(f"{YELLOW}pk_🔄 Running command: {cmd}{RESET}")
        subprocess.run(cmd, shell=True, check=True, cwd=cwd)
    except subprocess.CalledProcessError as e:
        log_failure(step_name or cmd, str(e))

def main():
    base_path = os.path.abspath("jetson-setup")
    stress_path = os.path.join(base_path, "jetson-stress")
    gpu_burn_path = os.path.join(stress_path, "gpu-burn")
    home_dir = os.path.expanduser("~")
    target_path = os.path.join(home_dir, "jetson-stress")

    step = "Check 'jetson-setup' directory"
    log_step(step)
    if not os.path.isdir(base_path):
        log_failure(step, f"'{base_path}' directory does not exist. Make sure you have cloned the repository.")

    step = "Initialize git submodule"
    log_step(step)
    run("git submodule init", cwd=base_path, step_name=step)

    step = "Update git submodule"
    log_step(step)
    run("git submodule update", cwd=base_path, step_name=step)

    step = "Check 'gpu-burn' directory"
    log_step(step)
    if not os.path.isdir(gpu_burn_path):
        log_failure(step, f"'{gpu_burn_path}' directory does not exist. Check if submodules were cloned properly.")

    step = "Build gpu-burn with make"
    log_step(step)
    run("make", cwd=gpu_burn_path, step_name=step)

    step = f"Copy 'jetson-stress' to home directory → {target_path}"
    log_step(step)
    run(f"cp -r {stress_path} {home_dir}", step_name=step)

    log_success("All tasks completed successfully!")

if __name__ == "__main__":
    main()
