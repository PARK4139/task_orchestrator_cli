
_, status_out = run_command("git status", capture_output=True)
def fail_and_exit(start_time):
duration = time.time() - start_time
print(f"\n{PK_ANSI_COLOR_MAP['RED']}[!] Aborting further steps. Current git status:{PK_ANSI_COLOR_MAP['RESET']}")
print(f"{PK_ANSI_COLOR_MAP['RED']}process failed at {time.strftime('%Y-%m-%d %H:%M:%S')} (elapsed {duration:.2f} sec){PK_ANSI_COLOR_MAP['RESET']}")
print(status_out.strip())
sys.exit(1)
