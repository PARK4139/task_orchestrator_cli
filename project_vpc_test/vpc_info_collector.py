# -*- coding: utf-8 -*-  # set encoding as UTF-8

# this python code for xc
# Reference: Compatible with Python 3.6.9 and above

import os
import platform
import subprocess
import traceback
from pathlib import Path

from pkg_py.pk_core import get_pnx_unix_style

# todo : chore : mode, -v or --verbose 를 인자로
mode = 'front'

stamp_fail = "[ FAIL ]"
stamp_success = "[ SUCCESS ]"
stamp_error = "[ ERROR ]"
stamp_tried = "[ ATTEMPTED ]"
stamp_output = "[ OUTPUT ]"
stamp_expected = "[ EXPECTED ]"
RESET = "\033[0m" # print test result normal/abnormal decision as color
MENT_TEST_COMPLETE = rf"{os.path.basename(__file__)} executed successfully"


# vision module ip
if mode == 'front':
    ip_xc = "192.168.10.11"
elif mode == 'rear':
    ip_xc = "192.168.10.12"


def write_content_to_f(f_pnx: str, content: str, linefeed: str = "\n"):
    with open(f_pnx, "a",encoding='utf-8') as f:
        f.write(f"{content}{linefeed}")

def execute_command(command):
    """Execute a shell command and return the result."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            # text=True,  # Ensures stdout and stderr are returned as strings, compatible with Python 3.7 and above
            universal_newlines=True,  # Ensures stdout and stderr are returned as strings, compatible with Python 3.7 and below
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            return f"{result.stdout.strip()}", 0
        else:
            return f"{result.stderr.strip()}", 1
    except Exception as e:
        return f"Error: {str(e)}"


def excute_test_case(description: str, command_list:[str], test_results_f:str, ment_negative: str = None, ment_expected: str = None):
    """Process a list of commands and log their results."""
    write_content_to_f("____________________________________________________ ", test_results_f)
    std_out_stream = None
    state = None
    for command in command_list:

        # try stamp
        write_content_to_f(f_pnx=test_results_f,content=f"{stamp_tried:18s}{command}")

        std_out_stream_str, state = execute_command(command)
        std_out_stream_list = std_out_stream_str.split("\n")

        # output stamp
        for std_out_stream in std_out_stream_list:
            write_content_to_f(f_pnx=test_results_f, content=f"{stamp_output:18s}{std_out_stream}")

        # fail stamp
        if state != 0:  # 0 : command succes
            write_content_to_f(f_pnx=test_results_f, content=f"{stamp_fail:18s}The command did not execute successfully.")

            return std_out_stream, state

        # stamp_expected stamp
        if ment_expected is not None:
            write_content_to_f(f_pnx=test_results_f, content=f"{stamp_expected:18s}{ment_expected}")


        # fail stamp
        if ment_expected is not None:
            for std_out_stream in std_out_stream_list:
                if ment_expected not in std_out_stream:
                    write_content_to_f(f_pnx=test_results_f, content=f"{stamp_fail:18s}'standard output stream' did not contains '{ment_expected}'")
                    return std_out_stream, state

        # success stamp
        if ment_expected is not None:
            for std_out_stream in std_out_stream_list:
                if ment_expected in std_out_stream:
                    write_content_to_f(f_pnx=test_results_f, content=f"{stamp_success:18s}'standard output stream' contains '{ment_expected}'")
                    # write_to_file(f"{stamp_success:18s}'{std_out_stream[:30].strip()}' contains '{ment_expected}'",f_txt)

    return std_out_stream, state


def print_as_red(string):
    RED = "\033[31m"
    print(f"{RED}{string}{RESET}")


def print_with_flush(string, flush: bool):
    print(string, flush)


def print_as_green(string):
    GREEN = "\033[32m"
    print(f"{GREEN}{string}{RESET}")


def print_as_blue(string):
    BLUE = "\033[34m"
    print(f"{BLUE}{string}{RESET}")


def print_as_yellow(string):
    YELLOW = "\033[33m"
    print(f"{YELLOW}{string}{RESET}")

def initialize_file(f_pnx):
    """Create and initialize a file."""
    if "\0" in f_pnx:
        raise ValueError(f"Invalid file path with null byte: {f_pnx!r}")
    directory = os.path.dirname(f_pnx)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    try:
        with open(f_pnx, "w", encoding='utf-8') as f:
            f.write("")  # Initialize with empty content
    except Exception as e:
        raise IOError(f"Failed to initialize file {f_pnx!r}: {e}")

def excute_test_cases(test_results_f_pnx):
    # init f_pnx
    initialize_file(test_results_f_pnx)

    # test environment logging
    write_content_to_f(f_pnx=test_results_f_pnx, content="____________________________________________________ ")
    if platform.system() == 'Windows':
        write_content_to_f(f_pnx=test_results_f_pnx, content=f'{"TEST ENVIRONMENT OS":30s} : Windows ')
    elif platform.system() == 'Linux':
        write_content_to_f(f_pnx=test_results_f_pnx, content=f'{"TEST ENVIRONMENT OS":30s} : Linux ')
    else:
        write_content_to_f(f_pnx=test_results_f_pnx, content=f'{"TEST ENVIRONMENT OS":30s} : Undefined ')

    # python3 vesion logging
    python_version, state = execute_command(command="python3 --version")
    write_content_to_f(f_pnx=test_results_f_pnx, content=f'{"TEST ENVIRONMENT PYTHON":30s} : {python_version} ')

    # module name logging
    write_content_to_f(f_pnx=test_results_f_pnx, content=f'{"TEST TARGET":30s} : vision module (xc {mode})')

    # module name logging
    nvidia_serial_number, state = execute_command(command="cat /sys/firmware/devicetree/base/serial-number && echo ''")
    if state == 1:
        nvidia_serial_number = 'Not Found'
    write_content_to_f(f_pnx=test_results_f_pnx, content=f'{"TEST TARGET DEVICE ID ":30s} : {nvidia_serial_number}\n')

    excute_test_case(
        description="NVIDIA Serial Number (13 digits, only numbers)",
        command_list=["cat /sys/firmware/devicetree/base/serial-number && echo ''"],
        test_results_f = test_results_f_pnx
    )

    excute_test_case(
        description="User Information(whoami)",
        command_list=["whoami"],
        ment_expected='nvidia',
        test_results_f = test_results_f_pnx
    )
    excute_test_case(
        description="User Information(hostname)",
        command_list=["hostname"],
        ment_expected='nvidia',
        test_results_f = test_results_f_pnx
    )
    excute_test_case(
        description="User Information(users)",
        command_list=["users"],
        ment_expected='nvidia',
        test_results_f = test_results_f_pnx
    )
    excute_test_case(
        description=f"IP Information ({mode})",
        command_list=["ifconfig eth0"],
        ment_expected=ip_xc,
        test_results_f = test_results_f_pnx
    )

    # write end line
    write_content_to_f(content="____________________________________________________ ",f_pnx=test_results_f_pnx)

    # The 0 indicates that this file executed successfully.
    # write_content_to_f(content=MENT_TEST_COMPLETE, f_pnx=test_results_f_pnx)
    # write_content_to_f(content="0", linefeed='', f_pnx=test_results_f_pnx)


def print_test_cases(test_results_f_pnx):
    with open(test_results_f_pnx, "r",encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if 'Not Found' in line:
                print_as_red(line.strip())
            elif stamp_fail in line:
                print_as_red(line.strip())
            elif stamp_success in line:
                print_as_green(line.strip())
            elif stamp_error in line:
                print_as_yellow(line.strip())
            elif stamp_tried in line:
                print(line.strip())
            else:
                print(line.strip())
            if MENT_TEST_COMPLETE in line:
                print_with_flush(line.strip(), flush=True)


def get_pnx_windows_style(pnx):
    pnx = pnx.replace(rf"//", f"/")
    pnx = pnx.replace(rf"/", f"\\")
    pnx = pnx.replace(rf"/mnt/c/", f"C:/")
    pnx = pnx.replace(rf"/mnt/d/", f"D:/")
    pnx = pnx.replace(rf"/mnt/e/", f"E:/")
    pnx = pnx.replace(rf"/mnt/f/", f"F:/")
    return pnx


if __name__ == '__main__':
    try:
        # todo test_vpc() 로 pytest 기반으로 동작하도록 마이그레이션하고, pytest -v 옵션 줘서 출력하고,
        #     log 파일은 test_vpc_xc_#.log 에 작성하도록
        # init path of f_txt
        f_txt = None
        if platform.system() == 'Windows':
            f_txt = f"{os.path.splitext(os.path.basename(__file__))[0]}.txt"
            f_txt = get_pnx_windows_style(f_txt)
        if platform.system() == 'Linux':
            f_txt = f"{os.path.splitext(os.path.basename(__file__))[0]}.txt"
            f_txt = get_pnx_unix_style(f_txt)
        # print_as_green(string = rf'''f_txt="{f_txt}" %%%FOO%%%''')

        # excute to test cases
        excute_test_cases(test_results_f_pnx=f_txt)

        # print test result recorded
        # print_test_cases(test_results_f_pnx=f_txt)
    except Exception as e:
        print_as_red(traceback.format_exc())

        # debugger
        # import pdb
        # pdb.set_trace()
