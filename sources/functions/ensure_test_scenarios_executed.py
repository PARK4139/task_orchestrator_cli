import logging
import pytest
from pathlib import Path
import io
import sys
import os

def ensure_test_scenarios_executed():
    """Discovers and runs all automated tests in the task_orchestrator_cli_tests directory using pytest."""
    # lazy import
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_TESTS
    from sources.objects.task_orchestrator_cli_files import F_TASK_ORCHESTRATOR_CLI_LOG

    logging.debug("test_scenarios.py executed")
    logging.debug("Starting automated test execution with pytest...")

    # Set FORCE_COLOR environment variable to force colored output
    os.environ['FORCE_COLOR'] = '1'

    pytest_args = [str(D_TASK_ORCHESTRATOR_CLI_TESTS), "-v", "-s", "--ignore=task_orchestrator_cli_tests/TBD", "--color=yes"]

    # --- First run: For console output with colors ---
    logging.debug("Running pytest for console output...")
    try:
        result_code_console = pytest.main(pytest_args)
    finally:
        # Unset FORCE_COLOR environment variable
        del os.environ['FORCE_COLOR']

    # --- Second run: For capturing output to log file ---
    logging.debug("Running pytest for log file capture...")
    # Re-set FORCE_COLOR for the second run if needed, though it might not affect captured output
    os.environ['FORCE_COLOR'] = '1' # Ensure it's set for the second run too

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_output = io.StringIO()
    sys.stdout = redirected_output
    sys.stderr = redirected_output

    try:
        result_code_log = pytest.main(pytest_args)
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        del os.environ['FORCE_COLOR'] # Unset after second run

    pytest_output = redirected_output.getvalue()

    with open(F_TASK_ORCHESTRATOR_CLI_LOG, "w", encoding="utf-8") as f:
        f.write(pytest_output)

    logging.debug(f"Automated test execution finished. Pytest results saved to {F_TASK_ORCHESTRATOR_CLI_LOG}.")
    # Return the result code from the console run, as that's what the user sees
    return result_code_console
