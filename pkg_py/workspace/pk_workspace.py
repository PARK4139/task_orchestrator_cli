import inspect
import traceback

from pkg_py.ensure_python_program_reloaded_as_hot_reloader import get_value_via_fzf_or_history
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.get_f_historical import get_f_historical
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_values_from_historical_file import get_values_from_historical_file
from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.set_values_to_historical_file import set_values_to_historical_file
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
import glob
import inspect
import os
import subprocess

import psutil
import win32gui
import win32process

from pkg_py.ensure_python_program_reloaded_as_hot_reloader import get_value_via_fzf_or_history
from pkg_py.functions_split.chcp_65001 import chcp_65001
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_os_n import get_os_n
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_window_title import get_window_title
from pkg_py.functions_split.kill_process_via_taskkill import kill_process_via_taskkill
from pkg_py.functions_split.pk_colorama_init_once import pk_colorama_init_once
from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.pk_sleep import pk_sleep
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.write_like_person import write_like_person
from pkg_py.pk_interface_graphic_user import get_windows_opened
from pkg_py.pk_system_object.directories import D_PKG_WINDOWS
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.etc import PK_UNDERLINE


def get_last_history_file(__file__, func_n):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    history_file = os.path.join(__file__, f".{func_n}_history")
    return history_file


def get_last_history(history_file):
    if os.path.exists(history_file):
        with open(history_file, encoding="utf-8") as f:
            return f.read().strip()
    return None


def save_to_history(contents_to_save: str, history_file):
    with open(history_file, "w", encoding="utf-8") as f:
        f.write(contents_to_save.strip())


def get_fzf_command():
    for name in ["fzf", "fzf.exe"]:
        try:
            subprocess.run([name, "--version"], capture_output=True, check=True)
            return name
        except Exception:
            continue
    return None


def fallback_choice(pk_file_list: list[str], last_selected: str | None):
    print("※ fzf 미설치 → fallback 선택 모드 사용")
    for idx, fpath in enumerate(pk_file_list):
        fname = os.path.basename(fpath)
        mark = " <- 최근 실행" if fpath == last_selected else ""
        print(f"[{idx}] {fname}{mark}")
    try:
        choice = input("실행할 번호를 입력하세요 (Enter로 취소): ").strip()
        if not choice:
            return None
        return pk_file_list[int(choice)]
    except (ValueError, IndexError):
        return None


def pk_run_py_system_process_by_pnx(file_to_excute, file_title):
    # OS별 실행
    import subprocess

    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

    if is_os_windows():
        # title 명령어로 창 제목 지정 (pk_ 접두사 제거된 제목)
        cmd = f'start "" cmd.exe /k "title {file_title}&& python {file_to_excute}"'
        print(f"[실행 중 - Windows] {cmd}")
        cmd_to_os(cmd=cmd, mode='a', mode_with_window=1)
    elif is_os_wsl_linux():
        # WSL 환경
        cmd = f'python3 {file_to_excute}'
        print(f"[실행 중 - WSL] {cmd}")
        cmd_to_os(cmd=cmd)
    else:
        # 기타 리눅스/유닉스
        cmd = f'python3 {file_to_excute}'
        print(f"[실행 중 - Linux/Unix] {cmd}")
        subprocess.run(cmd, shell=True)


def get_refactor_py_file_list():
    refactor_dir = os.path.join(os.path.dirname(__file__), "../refactor")
    pattern = os.path.join(refactor_dir, "*.py")
    return sorted(glob.glob(pattern))


# from pkg_py.pk_system_object.Local_test_activate import LTA
#
# from pkg_py.pk_system_object.print_util import pk_print
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_pids import get_pids
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.pk_system_object.Local_test_activate import LTA


def kill_cmd_exe():
    try:
        pids = get_pids("cmd.exe")
        for pid in pids:
            kill_process(pid=pid)
    except:
        pk_print(working_str=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')


def kill_powershell_exe(debug_mode=True):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    try:
        pids = get_pids("powershell.exe")
        for pid in pids:
            kill_process_via_wmic(pid=pid)
    except:
        pk_print(working_str=rf'''{'%%%FOO%%%' if LTA else ''}''', print_color='red')


def kill_process_via_wmic(process_img_n=None, debug_mode=True):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    if process_img_n is not None:
        pk_print(rf"{func_n}() 동작 조건 충족")
    else:
        pk_print(rf"{func_n}() 동작 조건 불충족")
        return

    if process_img_n is not None:
        process_img_n = process_img_n.replace("\'", "")
        process_img_n = process_img_n.replace("\"", "")
        cmd_to_os(f'wmic process where name="{process_img_n}" delete ')


def pk_kill_process_v1(cmd_exe_title):
    import psutil
    pk_print(f'''cmd_exe_title={cmd_exe_title}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    """
    주어진 cmd_exe_title과 일치하는 프로세스를 찾아 동기적으로 종료하는 함수
    """
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # cmd_exe_title이 프로세스 cmdline에 포함되어 있는지 확인
            if process.info['cmdline'] and any(cmd_exe_title in cmd for cmd in process.info['cmdline']):
                pid = process.info['pid']
                # pk_print(f"[PROCESS TERMINATED] PID={pid}, Name={process.info['name']}")
                proc = psutil.Process(pid)
                proc.terminate()  # 프로세스 종료 요청
                proc.wait(timeout=5)  # 종료 완료를 대기, 최대 5초 대기
                pk_print(f"[PROCESS TERMINATED] PID={pid}, Name={process.info['name']}", print_color="green")
        except psutil.TimeoutExpired:
            pk_print(f"[PROCESS TERMINATED] 시간 초과 ", print_color='red')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


def pk_kill_process_v2(cmd_exe_title: str):
    import subprocess

    import csv
    from io import StringIO
    try:
        window_title = get_window_title(window_title_seg=cmd_exe_title)
        if not window_title:
            return
        if LTA:
            pk_print(f'''window_title={window_title} {'%%%FOO%%%' if LTA else ''}''')
        # if not is_window_opened_exactly(window_title=window_title):
        #     return
        cmd = f'tasklist /FI "WINDOWTITLE eq {window_title}" /FO CSV'
        pk_print(f'''cmd={cmd} {'%%%FOO%%%' if LTA else ''}''')
        output = subprocess.check_output(cmd, shell=True, encoding='cp949', errors='ignore')

        matched_pids = set()
        reader = csv.DictReader(StringIO(output))
        for row in reader:
            pid = row.get("PID")
            if pid:
                matched_pids.add(pid)

        for pid in matched_pids:
            subprocess.run(['taskkill', '/PID', pid, '/T', '/F'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pk_print(f"[PK KILL] PID={pid} cmd_exe_title={cmd_exe_title}", print_color="green")

        if not matched_pids:
            pk_print(f"[NO MATCH] '{cmd_exe_title}'와 일치하는 프로세스를 찾지 못했습니다.", print_color="red")

    except subprocess.CalledProcessError:
        pk_print(f"[NO MATCH] '{cmd_exe_title}' 프로세스를 찾지 못했습니다.", print_color="red")
    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v3(cmd_exe_title: str):
    import wmi
    import subprocess

    try:
        window_title = get_window_title(window_title_seg=cmd_exe_title)
        if not window_title:
            # pk_print(f"[SKIP] 창 제목 세그먼트 '{cmd_exe_title}'로 찾은 창이 없습니다.", print_color="blue")
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        c = wmi.WMI()
        matched_pids = set()

        for proc in c.Win32_Process():
            try:
                title_match = window_title.lower() in (proc.CommandLine or "").lower()
                caption_match = "cmd.exe" in (proc.Caption or "").lower()

                if title_match and caption_match:
                    matched_pids.add(proc.ProcessId)
            except Exception:
                continue

        for pid in matched_pids:
            subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pk_print(f"[PK KILL] PID={pid} window_title={window_title}", print_color="green")

        if not matched_pids:
            pk_print(f"[NO MATCH] '{window_title}'와 일치하는 프로세스를 찾지 못했습니다.", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v5(cmd_exe_title: str):
    import psutil
    import subprocess

    try:
        window_title = get_window_title(window_title_seg=cmd_exe_title)
        if not window_title:
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        matched_pids = set()

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if 'cmd.exe' in (proc.info['name'] or '').lower() and window_title.lower() in ' '.join(proc.info['cmdline'] or []).lower():
                    matched_pids.add(proc.info['pid'])
            except Exception:
                continue

        for pid in matched_pids:
            try:
                subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
                pk_print(f"[PK KILL] PID={pid} window_title={window_title}", print_color="green")
            except subprocess.TimeoutExpired:
                pk_print(f"[TIMEOUT] PID={pid} taskkill took too long", print_color="yellow")

        if not matched_pids:
            pk_print(f"[NO MATCH] '{window_title}'와 일치하는 프로세스를 찾지 못했습니다.", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v6(cmd_exe_title: str):
    import psutil
    import subprocess

    try:
        window_title = get_window_title(window_title_seg=cmd_exe_title)
        if not window_title:
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        matched_pids = set()

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
                if 'cmd.exe' in (proc.info['name'] or '').lower() and cmd_exe_title.lower() in cmdline.lower():
                    matched_pids.add(proc.info['pid'])
            except (psutil.AccessDenied, psutil.ZombieProcess, psutil.NoSuchProcess):
                continue
            except Exception as e:
                pk_print(f"[WARN] psutil error: {e}", print_color="yellow")
                continue

        for pid in matched_pids:
            try:
                subprocess.run(
                    ['taskkill', '/PID', str(pid), '/T', '/F'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=1
                )
                pk_print(f"[PK KILL] PID={pid} window_title={window_title}", print_color="green")
            except subprocess.TimeoutExpired:
                pk_print(f"[TIMEOUT] taskkill for PID={pid} timed out", print_color="yellow")
            except Exception as e:
                pk_print(f"[TASKKILL ERROR] PID={pid}, {e}", print_color="red")

        if not matched_pids:
            pk_print(f"[NO MATCH] '{window_title}'와 일치하는 프로세스를 찾지 못했습니다.", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v17(window_title_seg: str):
    import wmi
    import subprocess

    try:
        window_title = get_window_title(window_title_seg=window_title_seg)
        if not window_title:
            return
        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
        c = wmi.WMI()
        matched_pids = set()
        for proc in c.query("SELECT ProcessId, CommandLine, Caption FROM Win32_Process"):
            try:
                if "cmd.exe" in (proc.Caption or "").lower() and get_nx(window_title).lower() in (proc.CommandLine or "").lower():
                    matched_pids.add(proc.ProcessId)
            except Exception:
                continue
        for pid in matched_pids:
            subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pk_print(f"PK KILL PID={pid} window_title={window_title}", print_color="green")
        if not matched_pids:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v17_fast(window_title_seg: str):
    import subprocess

    window_title = get_window_title(window_title_seg=window_title_seg)
    if not window_title:
        return

    if LTA:
        pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

    target = get_nx(window_title).lower()
    matched_pids = set()

    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'].lower() == "cmd.exe":
                cmdline = " ".join(proc.info['cmdline']).lower()
                if target in cmdline:
                    matched_pids.add(proc.info['pid'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    for pid in matched_pids:
        subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pk_print(f"PK KILL PID={pid} window_title={window_title}", print_color="green")

    if not matched_pids:
        pk_print(f"PK KILL '{window_title}' not found", print_color="red")


def pk_kill_process_v8(window_title_seg: str):
    import psutil
    import subprocess

    try:
        window_title = get_window_title(window_title_seg=window_title_seg)
        if not window_title:
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        target = get_nx(window_title).lower()
        matched_pids = set()

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'].lower() == "cmd.exe":
                    cmdline = " ".join(proc.info['cmdline']).lower()
                    if target in cmdline:
                        matched_pids.add(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        for pid in matched_pids:
            subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pk_print(f"PK KILL PID={pid} window_title={window_title}", print_color="green")

        if not matched_pids:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v9(window_title_seg: str):
    import psutil
    import subprocess
    from concurrent.futures import ThreadPoolExecutor

    try:
        window_title = get_window_title(window_title_seg=window_title_seg)
        if not window_title:
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        target = get_nx(window_title).lower()
        matched_pids = set()

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'].lower() == "cmd.exe":
                    cmdline = " ".join(proc.info['cmdline']).lower()
                    if target in cmdline:
                        matched_pids.add(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        def kill_pid(pid):
            subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            pk_print(f"PK KILL PID={pid} window_title={window_title}", print_color="green")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
                executor.map(kill_pid, matched_pids)
        else:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v10(window_title_seg: str):
    import psutil
    from concurrent.futures import ThreadPoolExecutor

    try:
        window_title = get_window_title(window_title_seg=window_title_seg)
        if not window_title:
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        target = get_nx(window_title).lower()
        matched_pids = set()

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'].lower() == "cmd.exe":
                    cmdline = " ".join(proc.info['cmdline']).lower()
                    if target in cmdline:
                        matched_pids.add(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        def kill_pid_psutil(pid):
            import psutil
            import time

            try:
                proc = psutil.Process(pid)
                proc.terminate()

                start = time.time()
                try:
                    proc.wait(timeout=1)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=1)
                    except psutil.TimeoutExpired:
                        pass  # 최종 타임아웃 2초 경과 후 포기

                elapsed = time.time() - start
                if elapsed > 2.0:
                    pk_print(f"PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="yellow")
                else:
                    pk_print(f"PK KILL PID={pid} window_title=...", print_color="green")

            except Exception as e:
                pk_print(f"PK KILL ERROR PID={pid} : {e}", print_color="red")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
                executor.map(kill_pid_psutil, matched_pids)
        else:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v11(window_title_seg: str):
    import psutil
    # import win32gui
    import time
    from concurrent.futures import ThreadPoolExecutor

    try:
        @pk_measure_seconds
        def get_window_title(window_title_seg: str) -> str | None:
            matches = []

            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if window_title_seg.lower() in title.lower():
                        matches.append((hwnd, title))

            win32gui.EnumWindows(enum_handler, None)
            if matches:
                return matches[0][1]
            return None

        window_title = get_window_title(window_title_seg=window_title_seg)
        if not window_title:
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        target = get_nx(window_title).lower()
        matched_pids = set()

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'].lower() == "cmd.exe":
                    cmdline = " ".join(proc.info['cmdline']).lower()
                    if target in cmdline:
                        matched_pids.add(proc.info['pid'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        @pk_measure_seconds
        def kill_pid_psutil(pid):
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                start = time.time()
                try:
                    proc.wait(timeout=1)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=1)
                    except psutil.TimeoutExpired:
                        pass

                elapsed = time.time() - start
                if elapsed > 2.0:
                    pk_print(f"PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="yellow")
                else:
                    pk_print(f"PK KILL PID={pid} window_title={window_title}", print_color="green")

            except Exception as e:
                pk_print(f"PK KILL ERROR PID={pid} : {e}", print_color="red")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
                executor.map(kill_pid_psutil, matched_pids)
        else:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v12(window_title_seg: str):
    import psutil
    # import win32gui
    import time
    from concurrent.futures import ThreadPoolExecutor

    try:
        @pk_measure_seconds
        def get_window_title(window_title_seg: str) -> str | None:
            matches = []

            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if window_title_seg.lower() in title.lower():
                        matches.append((hwnd, title))

            win32gui.EnumWindows(enum_handler, None)
            return matches[0][1] if matches else None

        @pk_measure_seconds
        def get_nx(path: str) -> str:
            import os
            return os.path.splitext(os.path.basename(path))[0]

        @pk_measure_seconds
        def monitor_process_state(proc, max_sec=2.5, interval=0.5):
            steps = int(max_sec / interval)
            for _ in range(steps):
                if not proc.is_running():
                    break
                try:
                    cpu = proc.cpu_percent()
                    mem = proc.memory_info().rss / (1024 * 1024)
                    th = proc.num_threads()
                    pk_print(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="yellow")
                except Exception:
                    pass
                time.sleep(interval)

        window_title = get_window_title(window_title_seg)
        if not window_title:
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        target = get_nx(window_title).lower()
        matched_pids = {
            proc.info['pid']
            for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
            if proc.info['name'].lower() == 'cmd.exe'
               and target in " ".join(proc.info.get('cmdline', [])).lower()
        }

        @pk_measure_seconds
        def kill_pid_psutil(pid):
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                start = time.time()

                monitor_process_state(proc)  # 실시간 모니터링 시작

                try:
                    proc.wait(timeout=1)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=1)
                    except psutil.TimeoutExpired:
                        pass

                elapsed = time.time() - start
                if elapsed > 2.5:
                    pk_print(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
                else:
                    pk_print(f"✅ PK KILL PID={pid} window_title={window_title}", print_color="green")
            except Exception as e:
                pk_print(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
                executor.map(kill_pid_psutil, matched_pids)
        else:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v13(window_title_seg: str):
    import psutil
    # import win32gui
    import time
    from concurrent.futures import ThreadPoolExecutor

    try:
        @pk_measure_seconds
        def get_window_title(window_title_seg: str) -> str | None:
            matches = []

            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if window_title_seg.lower() in title.lower():
                        matches.append((hwnd, title))

            win32gui.EnumWindows(enum_handler, None)
            return matches[0][1] if matches else None

        @pk_measure_seconds
        def get_nx(path: str) -> str:
            import os
            return os.path.splitext(os.path.basename(path))[0]

        @pk_measure_seconds
        def monitor_process_state(proc, max_sec=2.5, interval=0.5):
            pk_print(f"👁️ Start monitoring PID={proc.pid}", print_color="blue")
            steps = int(max_sec / interval)
            for _ in range(steps):
                if not proc.is_running():
                    break
                try:
                    cpu = proc.cpu_percent()
                    mem = proc.memory_info().rss / (1024 * 1024)
                    th = proc.num_threads()
                    pk_print(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
                except Exception:
                    pass
                time.sleep(interval)
            pk_print(f"👁️ End monitoring PID={proc.pid}", print_color="blue")

        window_title = get_window_title(window_title_seg)
        if not window_title:
            pk_print(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        target = get_nx(window_title).lower()
        matched_pids = {
            proc.info['pid']
            for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
            if proc.info['name'].lower() == 'cmd.exe'
               and target in " ".join(proc.info.get('cmdline', [])).lower()
        }

        failed_pids = []

        @pk_measure_seconds
        def kill_pid_psutil(pid):
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                start = time.time()

                monitor_process_state(proc)

                try:
                    proc.wait(timeout=1)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=1)
                    except psutil.TimeoutExpired:
                        pass

                elapsed = time.time() - start
                if elapsed > 5.0:
                    pk_print(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
                    failed_pids.append(pid)
                elif elapsed > 2.5:
                    pk_print(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
                else:
                    pk_print(f"✅ PK KILL PID={pid} window_title={window_title}", print_color="green")

            except Exception as e:
                failed_pids.append(pid)
                pk_print(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
                executor.map(kill_pid_psutil, matched_pids)
        else:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

        if failed_pids:
            pk_print(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def is_process_killed(window_title_seg: str, timeout: float = 1.0) -> bool:
    """
    주어진 window_title_seg에 해당하는 CMD 프로세스가 종료되었는지 확인하고 종료 시도.
    :param window_title_seg: 윈도우 제목 일부 문자열
    :param timeout: 종료 대기 시간 (초)
    :return: True (모두 종료됨), False (하나라도 종료 실패)
    """
    import psutil
    import os

    def get_pids_by_title_seg(windows_title_seg: str) -> list[int]:
        matches = get_window_title(windows_title_seg)
        if not matches:
            return []

        # 첫 번째 매칭된 타이틀을 기준으로 process 검색
        target = os.path.splitext(os.path.basename(matches[0]))[0].lower()
        return [
            proc.info['pid']
            for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
            if proc.info['name'].lower() == 'cmd.exe'
               and target in " ".join(proc.info.get('cmdline', [])).lower()
        ]

    try:
        pids = get_pids_by_title_seg(window_title_seg)

        if not pids:
            pk_print(f"[SKIP] No matching process found for '{window_title_seg}'", print_color="yellow")
            return True  # 이미 종료된 것으로 간주

        all_killed = True

        for pid in pids:
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                try:
                    proc.wait(timeout=timeout)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=timeout)
                    except psutil.TimeoutExpired:
                        pk_print(f"🛑 PID={pid} 종료 실패 (TIMEOUT)", print_color="red")
                        all_killed = False
                        continue

                if proc.is_running():
                    pk_print(f"⚠️ PID={pid} 여전히 실행 중", print_color="yellow")
                    all_killed = False
                else:
                    pk_print(f"✅ PID={pid} 종료 확인됨", print_color="green")

            except psutil.NoSuchProcess:
                continue
            except Exception as e:
                pk_print(f"❌ 예외 발생 PID={pid}, error={e}", print_color="red")
                all_killed = False

        return all_killed

    except Exception as e:
        pk_print(f"[ERROR] 전체 종료 확인 실패: {e}", print_color="red")
        return False


def pk_kill_process_v14(window_title_seg: str):
    import psutil
    # import win32gui
    import time
    from concurrent.futures import ThreadPoolExecutor

    try:
        @pk_measure_seconds
        def get_window_title(window_title_seg: str) -> str | None:
            matches = []

            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if window_title_seg.lower() in title.lower():
                        matches.append((hwnd, title))

            win32gui.EnumWindows(enum_handler, None)
            return matches[0][1] if matches else None

        @pk_measure_seconds
        def get_nx(path: str) -> str:
            import os
            return os.path.splitext(os.path.basename(path))[0]

        @pk_measure_seconds
        def monitor_process_state(proc, duration=1.0):
            try:
                pk_print(f"👁️ Monitor PID={proc.pid}", print_color="blue")
                cpu = proc.cpu_percent(interval=duration)
                mem = proc.memory_info().rss / (1024 * 1024)
                th = proc.num_threads()
                pk_print(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
            except Exception:
                pass

        window_title = get_window_title(window_title_seg)
        if not window_title:
            pk_print(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
            return

        if LTA:
            pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        target = get_nx(window_title).lower()
        matched_pids = {
            proc.info['pid']
            for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
            if proc.info['name'].lower() == 'cmd.exe'
               and target in " ".join(proc.info.get('cmdline', [])).lower()
        }

        failed_pids = []

        @pk_measure_seconds
        def kill_pid_psutil(pid):
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                start = time.time()

                monitor_process_state(proc, duration=0.5)

                try:
                    proc.wait(timeout=1)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=1)
                    except psutil.TimeoutExpired:
                        pass

                elapsed = time.time() - start
                if elapsed > 5.0:
                    pk_print(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
                    failed_pids.append(pid)
                    return  # 💥 병목 방지용 조기 종료

                if elapsed > 2.5:
                    pk_print(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
                else:
                    pk_print(f"✅ PK KILL PID={pid} window_title={window_title}", print_color="green")

            except Exception as e:
                failed_pids.append(pid)
                pk_print(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=4) as executor:
                executor.map(kill_pid_psutil, matched_pids)
        else:
            pk_print(f"PK KILL '{window_title}' not found", print_color="red")

        if failed_pids:
            pk_print(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def pk_kill_process_v15(window_title_seg: str):
    import psutil
    # import win32gui
    import time
    from concurrent.futures import ThreadPoolExecutor

    try:
        @pk_measure_seconds
        def get_window_matches(window_title_seg: str):
            matches = []

            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if title:
                        similarity = window_title_seg.lower() in title.lower()
                        matches.append((hwnd, title, similarity))

            win32gui.EnumWindows(enum_handler, None)

            # 출력용 정렬: 유사한 것 먼저
            matches.sort(key=lambda x: x[2], reverse=True)
            return matches

        @pk_measure_seconds
        def get_nx(path: str) -> str:
            import os
            return os.path.splitext(os.path.basename(path))[0]

        @pk_measure_seconds
        def monitor_process_state(proc, max_sec=2.5, interval=0.5):
            pk_print(f"👁️ Start monitoring PID={proc.pid}", print_color="blue")
            steps = int(max_sec / interval)
            for _ in range(steps):
                if not proc.is_running():
                    break
                try:
                    cpu = proc.cpu_percent()
                    mem = proc.memory_info().rss / (1024 * 1024)
                    th = proc.num_threads()
                    pk_print(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
                except Exception:
                    pass
                time.sleep(interval)
            pk_print(f"👁️ End monitoring PID={proc.pid}", print_color="blue")

        matches = get_window_matches(window_title_seg)

        if not matches:
            pk_print(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
            return

        pk_print(f"[INFO] Found {len(matches)} window(s). Similarity check:", print_color="cyan")
        for hwnd, title, is_similar in matches:
            sim_mark = "✅" if is_similar else "  "
            pk_print(f"{sim_mark} [{hwnd}] {title}", print_color="cyan")

        best_match_title = matches[0][1]
        if LTA:
            pk_print(f"🪟 Using best match title: {best_match_title} {'%%%FOO%%%' if LTA else ''}", print_color="cyan")

        target = get_nx(best_match_title).lower()
        matched_pids = {
            proc.info['pid']
            for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
            if proc.info['name'].lower() == 'cmd.exe'
               and target in " ".join(proc.info.get('cmdline', [])).lower()
        }

        failed_pids = []

        @pk_measure_seconds
        def kill_pid_psutil(pid):
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                start = time.time()

                monitor_process_state(proc)

                try:
                    proc.wait(timeout=1)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=1)
                    except psutil.TimeoutExpired:
                        pass

                elapsed = time.time() - start
                if elapsed > 5.0:
                    pk_print(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
                    failed_pids.append(pid)
                elif elapsed > 2.5:
                    pk_print(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
                else:
                    pk_print(f"✅ PK KILL PID={pid} window_title={best_match_title}", print_color="green")

            except Exception as e:
                failed_pids.append(pid)
                pk_print(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
                executor.map(kill_pid_psutil, matched_pids)
        else:
            pk_print(f"PK KILL '{best_match_title}' not found", print_color="red")

        if failed_pids:
            pk_print(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")

@pk_measure_seconds
def pk_ensure_process_killed(window_title: str):
    # pk_kill_process_v1(window_title)
    pk_kill_process_v17(window_title)
    # pk_kill_process_v16(window_title, exact=True)


def pk_kill_process_v16(window_title: str, exact: bool = True):
    import psutil
    import logging
    from concurrent.futures import ThreadPoolExecutor

    window_title = window_title.strip()

    try:
        import win32gui
        import win32process
    except ImportError as e:
        logging.error(f"[IMPORT ERROR] {e}. Please install pywin32.")
        return

    def enum_handler(hwnd, matched_hwnds):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).strip()
            if not title:
                return
            logging.debug(f"[ENUM] hwnd={hwnd}, title='{title}', target='{window_title}'")
            if exact:
                if title.lower() == window_title.lower():
                    matched_hwnds.append((hwnd, title))
                    logging.info(f"[MATCHED:EXACT] '{title}'")
            else:
                if window_title.lower() in title.lower():
                    matched_hwnds.append((hwnd, title))
                    logging.info(f"[MATCHED:PARTIAL] '{title}'")

    matched_hwnds = []
    try:
        win32gui.EnumWindows(lambda h, _: enum_handler(h, matched_hwnds), None)
    except Exception as e:
        logging.error(f"[EnumWindows ERROR] {e}")
        return

    if not matched_hwnds:
        logging.warning(f"[SKIP] No window matched for: '{window_title}' (exact={exact})")
        return

    logging.info(f"[INFO] Found {len(matched_hwnds)} matched window(s) for '{window_title}'")

    matched_pids = set()
    for hwnd, title in matched_hwnds:
        try:
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            logging.info(f"[HWND->PID] title='{title}' → pid={pid}")
            matched_pids.add(pid)
        except Exception as e:
            logging.warning(f"[WARN] Failed to get PID from hwnd={hwnd}: {e}")

    if not matched_pids:
        logging.error(f"[ERROR] No valid PID found for window title: '{window_title}'")
        return

    failed_pids = []

    def try_kill_pid(pid):
        try:
            proc = psutil.Process(pid)
            exe = proc.name().lower()
            if exe == "cmd.exe":
                logging.warning(f"[SKIP] Not killing cmd.exe (PID={pid})")
                return

            # ✅ 종료 전에 실행
            # ensure_pk_system_exit_silent()

            proc.terminate()
            try:
                proc.wait(timeout=1)
            except psutil.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=1)
            logging.info(f"[KILLED] PID={pid} ('{window_title}') exe='{exe}'")
        except Exception as e:
            failed_pids.append(pid)
            logging.error(f"[FAILED] PID={pid} error: {e}")

    with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
        executor.map(try_kill_pid, matched_pids)

    if failed_pids:
        logging.error(f"[FAILED PIDs] {sorted(failed_pids)}")
    # ipdb.set_trace()  # 🔍 디버깅 시작 지점


def pk_kill_process_by_window_title_seg(window_title_seg: str):
    import psutil
    # import win32gui
    # import win32process
    import time
    from concurrent.futures import ThreadPoolExecutor

    try:
        @pk_measure_seconds
        def get_window_matches(window_title_seg: str):
            matches = []

            def enum_handler(hwnd, _):
                if win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if title:
                        similarity = window_title_seg.lower() in title.lower()
                        matches.append((hwnd, title, similarity))

            win32gui.EnumWindows(enum_handler, None)
            matches.sort(key=lambda x: x[2], reverse=True)
            return matches

        @pk_measure_seconds
        def monitor_process_state(proc, max_sec=2.5, interval=0.5):
            pk_print(f"👁️ Start monitoring PID={proc.pid}", print_color="blue")
            steps = int(max_sec / interval)
            for _ in range(steps):
                if not proc.is_running():
                    break
                try:
                    cpu = proc.cpu_percent()
                    mem = proc.memory_info().rss / (1024 * 1024)
                    th = proc.num_threads()
                    pk_print(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
                except Exception:
                    pass
                time.sleep(interval)
            pk_print(f"👁️ End monitoring PID={proc.pid}", print_color="blue")

        matches = get_window_matches(window_title_seg)

        if not matches:
            pk_print(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
            return

        pk_print(f"[INFO] Found {len(matches)} window(s). Similarity check:", print_color="cyan")
        for hwnd, title, is_similar in matches:
            sim_mark = "✅" if is_similar else "  "
            pk_print(f"{sim_mark} [{hwnd}] {title}", print_color="cyan")

        # 유사도 높은 첫 번째 타이틀로 선택
        best_match_hwnd, best_match_title, _ = matches[0]
        if LTA:
            pk_print(f"🪟 Using best match title: {best_match_title} {'%%%FOO%%%' if LTA else ''}", print_color="cyan")

        # 해당 타이틀을 가진 윈도우들의 PID 직접 수집
        matched_pids = set()
        for hwnd, title, is_similar in matches:
            if is_similar:
                try:
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    matched_pids.add(pid)
                except Exception:
                    continue

        failed_pids = []

        @pk_measure_seconds
        def kill_pid_psutil(pid):
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                start = time.time()

                monitor_process_state(proc)

                try:
                    proc.wait(timeout=1)
                except psutil.TimeoutExpired:
                    proc.kill()
                    try:
                        proc.wait(timeout=1)
                    except psutil.TimeoutExpired:
                        pass

                elapsed = time.time() - start
                if elapsed > 5.0:
                    pk_print(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
                    failed_pids.append(pid)
                elif elapsed > 2.5:
                    pk_print(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
                else:
                    pk_print(f"✅ PK KILL PID={pid} title_match={best_match_title}", print_color="green")

            except Exception as e:
                failed_pids.append(pid)
                pk_print(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")

        if matched_pids:
            with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
                executor.map(kill_pid_psutil, matched_pids)
        else:
            pk_print(f"PK KILL '{best_match_title}' not found (No PIDs)", print_color="red")

        if failed_pids:
            pk_print(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def kill_wsl_exe():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    process_name = "wsl.exe"
    cmd = "wsl --shutdown"
    cmd_to_os(cmd=cmd, mode="a")
    pids = get_pids("wsl.exe")
    if pids is not None:
        for pid in pids:
            if pid is not None:
                kill_process_via_taskkill(pid=pid)
    write_like_person("exit")
    pk_press("enter")


def kill_thread(thread_name):
    import threading
    # 종료할 스레드 이름

    # 현재 exec  중인 모든 스레드 가져오기
    current_threads = threading.enumerate()

    # 종료할 스레드 찾기
    target_thread = None
    for thread in current_threads:
        if thread.name == thread_name:
            target_thread = thread
            break

    # 스레드 종료
    if target_thread:
        target_thread.join()
        print(f"{thread_name} 스레드가 종료되었습니다.")
    else:
        print(f"{thread_name} 스레드를 찾을 수 없습니다.")


def kill_us_keyboard():
    """
    프로세스 간 공유 메모리를 내부에서 초기화하고 사용하도록 변경
    """
    import threading
    from multiprocessing import shared_memory, Lock

    pk_colorama_init_once()

    if get_os_n() == 'windows':
        chcp_65001()

    shm_name = "flag_to_detect_enter"
    lock = Lock()

    try:
        # 기존 공유 메모리 존재 여부 확인
        shm = shared_memory.SharedMemory(name=shm_name, create=False)
        pk_print(rf"기존 공유 메모리 발견, 초기화 생략 shm_name={shm_name}", print_color="green")
    except FileNotFoundError:
        pk_print(rf"새로운 공유 메모리 생성 shm_name={shm_name}", print_color="green")
        shm = shared_memory.SharedMemory(create=True, size=1, name=shm_name)
        shm.buf[0] = 0  # 초기값 False (0)

    def listen_enter():
        """사용자가 Enter 키를 입력하면 flag를 True로 설정"""
        try:
            existing_shm = shared_memory.SharedMemory(name=shm_name)
            flag = existing_shm.buf
        except FileNotFoundError:
            pk_print("listen_enter: 공유 메모리가 존재하지 않음. 종료.", print_color='red')
            return

        while 1:
            input()  # Enter 입력 대기
            with lock:
                flag[0] = 1  # flag를 True로 변경
                pk_print("Enter detected! flag 업데이트됨.", print_color="blue")

        existing_shm.close()

    def main_loop():
        """flag 값이 True가 되면 특정 작업 수행 후 다시 False로 초기화"""
        try:
            existing_shm = shared_memory.SharedMemory(name=shm_name)
            flag = existing_shm.buf
        except FileNotFoundError:
            pk_print("main_loop: 공유 메모리가 존재하지 않음. 종료.", print_color='red')
            return

        while 1:
            # exec 할 명령
            f_cmd = rf"{D_PKG_WINDOWS}/pk_kill_us_keyboard.cmd"
            f_cmd = get_pnx_os_style(pnx=f_cmd)
            cmd_to_os(cmd=rf'"{f_cmd}"', encoding=Encoding.CP949)

            # sleep
            sleep_seconds = 3
            for _ in range(sleep_seconds):
                with lock:
                    if flag[0]:  # flag가 True면 리셋 후 루프 재시작
                        pk_print("Enter detected! Restarting loop...", print_color="white")

                        # pk_system_kill_us_keyboard.cmd (run)
                        f_cmd = rf"{D_PKG_WINDOWS}/pk_kill_us_keyboard.cmd"
                        f_cmd = get_pnx_os_style(pnx=f_cmd)
                        cmd_to_os(cmd=rf'"{f_cmd}"', encoding='utf-8')

                        flag[0] = 0  # flag를 다시 False로 초기화
                        pk_print(f"wait for enter  {'%%%FOO%%%' if LTA else ''}", print_color='white')
                        break
                pk_sleep(seconds=1)

        existing_shm.close()

    # thread run (in background)
    thread = threading.Thread(target=listen_enter, daemon=True)
    thread.start()

    # main loop run
    main_loop()

    # 공유 메모리 해제 (필요하면 exec )
    shm.close()
    # shm.unlink()  # 주석 해제하면 공유 메모리 삭제됨 (프로세스 간 공유 유지하려면 유지)


async def pk_kill_process_as_async(f):
    """
    주어진 cmd_exe_title과 일치하는 프로세스를 찾아 비동기적으로 종료하는 함수
    """
    import psutil
    import asyncio
    tasks = []

    f = get_pnx_os_style(f)
    f_nx = get_nx(f)
    # f_nx = f_nx

    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = process.info.get('cmdline', [])
            if cmdline and any(f_nx in cmd for cmd in cmdline):
                pid = process.info['pid']
                name = process.info['name']
                tasks.append(terminate_process_async(pid, name, f_nx))
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # 권한 오류나 존재하지 않는 프로세스는 무시

    if tasks:
        await asyncio.gather(*tasks)  # 모든 프로세스를 비동기적으로 종료


def kill_process(img_name=None, pid=None):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    pk_print(working_str=rf'''{PK_UNDERLINE}{func_n}()  {'%%%FOO%%%' if LTA else ''}''')
    # function_arg_names= [param.name for param in inspect.signature(process_kill).parameters.values()] # fail
    Nones = [img_name, pid]
    None_count = Nones.count(None)
    if None_count == 2:
        pk_print(working_str=rf''' 이 {func_n}()의 인자는 최대 1개 까지 받을 수 있습니다.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    if None_count == 1:
        if img_name is not None:
            img_name = img_name.replace("\'", "")
            img_name = img_name.replace("\"", "")
            cmd_to_os(f'taskkill /f /im "{img_name}"')
            cmd_to_os(f'wmic process where name="{img_name}" delete ')
        if pid is not None:
            # cmd_to_os(f'taskkill /f /pid {pid}', debug_mode=debug_mode)
            cmd_to_os(f'taskkill /f /pid {pid}')
    if None_count == 0:
        pk_print(working_str=rf''' 이 {func_n}()의 인자는 최소 1개의 인자가 요구됩니다.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')


def get_process_name_list(unique: bool = True, sort: bool = True) -> list:
    """
    현재 실행 중인 모든 프로세스의 이름 목록을 반환합니다.

    :param unique: True일 경우 중복 remove
    :param sort: True일 경우 알파벳 순 정렬
    :return: 프로세스 이름 리스트
    """
    import psutil
    names = []

    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name']:
                names.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if unique:
        names = list(set(names))
    if sort:
        names.sort()

    return names


def pk_kill_process_v16_1(window_title: str, exact: bool = True):
    """
    창 제목이 정확히 일치(또는 부분 일치)하는 모든 창에 WM_CLOSE 메시지를 보내 창만 닫는다.
    """
    import win32gui
    import win32con
    import logging

    window_title = window_title.strip()
    closed_hwnds = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd).strip()
            if not title:
                return
            if exact:
                if title.lower() == window_title.lower():
                    logging.info(f"[CLOSE:EXACT] '{title}' (hwnd={hwnd})")
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                    closed_hwnds.append((hwnd, title))
            else:
                if window_title.lower() in title.lower():
                    logging.info(f"[CLOSE:PARTIAL] '{title}' (hwnd={hwnd})")
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                    closed_hwnds.append((hwnd, title))

    try:
        win32gui.EnumWindows(enum_handler, None)
    except Exception as e:
        logging.error(f"[EnumWindows ERROR] {e}")

    if not closed_hwnds:
        logging.warning(f"[SKIP] No window matched for: '{window_title}' (exact={exact})")
    else:
        logging.info(f"[INFO] Closed {len(closed_hwnds)} window(s) for '{window_title}'")


def get_values_sanitize_for_cp949(text):
    # 유사 문자 수동 치환
    replacements = {
        '–': '-',  # EN DASH
        '—': '-',  # EM DASH
        '“': '"', '”': '"',
        '‘': "'", '’': "'",
        '…': '...', '•': '*',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
    # return text.encode('cp949', errors='replace').decode('cp949')
    # return text.encode('cp949', errors='replace').decode('cp949')


def pk_ensure_process_deduplicated(window_title_seg: str, exact=True):
    import win32gui
    import win32con

    try:
        window_title = get_window_title(window_title_seg=window_title_seg)
        if not window_title:
            return

        if LTA:
            pk_print(f"[DEBUG] window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        hwnds = []

        def enum_handler(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if (exact and title == window_title) or (not exact and window_title in title):
                    hwnds.append(hwnd)

        win32gui.EnumWindows(enum_handler, None)

        if not hwnds:
            pk_print(f"[SKIP] No matching windows for '{window_title}'", print_color="red")
            return

        survivor_hwnd = hwnds[0]
        to_close = hwnds[1:]

        for hwnd in to_close:
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            pk_print(f"[CLOSE] HWND={hwnd} closed for window_title='{win32gui.GetWindowText(hwnd)}'", print_color="green")

        pk_print(f"[SURVIVED] HWND={survivor_hwnd} kept alive → '{win32gui.GetWindowText(survivor_hwnd)}'", print_color="yellow")

    except Exception as e:
        pk_print(f"[ERROR] {e}", print_color="red")


def ensure_cmd_exe_deduplicated():
    key_name = 'window_opened'
    func_n = inspect.currentframe().f_code.co_name
    values = get_windows_opened()
    values = [get_values_sanitize_for_cp949(v) for v in values]
    print_iterable_as_vertical(item_iterable=values, item_iterable_n="values")
    window_opened = get_value_via_fzf_or_history(key_name=key_name, options=values, file_id=get_file_id(key_name, func_n))
    while True:
        window_opened = get_pnx_os_style(window_opened)
        pk_print(f'''window_opened={window_opened} {'%%%FOO%%%' if LTA else ''}''')
        pk_ensure_process_deduplicated(window_title_seg=window_opened)
        # pk_sleep(milliseconds=1000)
        pk_sleep(milliseconds=200)


def ensure_cmd_exe_deduplicated_all():
    from collections import defaultdict
    # ① 열린 창 목록 확보 및 CP949 대응 처리
    values = get_windows_opened()
    values = [get_values_sanitize_for_cp949(v) for v in values]

    # ② 제목별로 그룹핑 (윈도우 제목 기준)
    grouped = defaultdict(list)
    for title in values:
        grouped[title].append(title)

    print_iterable_as_vertical(item_iterable=sorted(grouped), item_iterable_n="중복 확인 대상 창 제목들")

    # ③ 각 제목에 대해 1개만 남기고 닫기 시도
    for window_title in grouped:
        pk_print(f"[처리 중] 창 제목='{window_title}' 중복 제거", print_color="cyan")
        pk_ensure_process_deduplicated(window_title_seg=window_title, exact=True)
        # pk_sleep(seconds=1000)
        # pk_sleep(seconds=500)
        pk_sleep(milliseconds=200)  # 너무 빠르게 반복되지 않도록 약간 대기

def ensure_cmd_exe_deduplicated_all_in_loop():
    while True:
        ensure_cmd_exe_deduplicated_all()


def ensure_cmd_exe_all_closed_in_loop():
    while True:
        key_name = 'window_opened'
        values = get_windows_opened()
        func_n = inspect.currentframe().f_code.co_name
        # sys.stdout.reconfigure(encoding='utf-8') # fail
        # values = values.replace('–', '-')  # 유니코드 EN DASH → 하이픈
        values = [get_values_sanitize_for_cp949(v) for v in values]
        print_iterable_as_vertical(item_iterable=values, item_iterable_n="values")
        window_opened = get_value_via_fzf_or_history(key_name=key_name, options=values, file_id=get_file_id(key_name, func_n))
        window_opened = get_pnx_os_style(window_opened)
        pk_print(f'''window_opened={window_opened} {'%%%FOO%%%' if LTA else ''}''')

        pk_ensure_process_killed(window_title=window_opened)
        # pk_sleep(seconds=1000)
        # pk_sleep(seconds=500)
        pk_sleep(milliseconds=200)


def get_value_via_fzf_or_history_routine(key_name, file_id, options, editable):
    f_historical = get_f_historical(file_id=file_id)
    historical_values = get_values_from_historical_file(f_historical=f_historical)
    options = get_list_calculated(origin_list=options, plus_list=historical_values)
    options = get_list_calculated(origin_list=options, dedup=True)
    selected = get_value_via_fzf_or_history(key_name=key_name, file_id=file_id, options=options, editable=editable)
    options = get_list_calculated(origin_list=[selected], plus_list=options) # 선택값을 맨 앞으로 정렬
    options = get_list_calculated(origin_list=options, dedup=True)
    set_values_to_historical_file(f_historical=f_historical, values=options)
    return selected
