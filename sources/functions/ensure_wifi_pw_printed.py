# -*- coding: utf-8 -*-
"""
Wi-Fi 프로필/비밀번호 출력 (권한 감지 + 안전한 자동복구 + 하이브리드 파싱)
- 관리자 권한 필수 작업은 관리자일 때만 수행 (비관리자면 즉시 명확히 종료)
- WLAN AutoConfig 서비스/무선 인터페이스 자동 복구(관리자 한정)
- profiles(복수) 사용, UTF-8 코드페이지 시도 + 단수 명령 폴백
- 레거시(라인 스캔) → 정규식 폴백 하이브리드 파싱
- 비밀번호 추출은 레거시 파이프(| find) → 정규식 순서로 시도
- 인터페이스 없음/서비스 거부 등 환경 문제를 명확히 리포트
"""
import re
from typing import List, Tuple, Optional

import logging

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.get_str_from_list import get_str_from_list
from sources.functions.ensure_sensitive_info_masked import ensure_sensitive_info_masked
from sources.objects.pk_map_colors import ANSI_COLOR_MAP
from sources.objects.pk_local_test_activate import LTA


# ---------------- 공통 실행 래퍼 ----------------

def _exec(cmd: str) -> str:
    out_list = ensure_command_executed(cmd)
    return (get_str_from_list(out_list) or "").strip()


def _first_nonempty_output(cmds: List[str]) -> str:
    for cmd in cmds:
        s = _exec(cmd)
        if s:
            return s
    return ""


# ---------------- 권한/환경 진단 ----------------

def _is_admin() -> bool:
    try:
        import ctypes
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        # fallback: 'net session'은 관리자만 0으로 끝남
        out = _exec("net session")
        return "There are no entries" in out or "명령을 잘 실행" in out  # 언어별 대충 매칭


NO_WLAN_PATTERNS = [
    r"There is no wireless interface on the system\.",
    r"시스템에\s*무선\s*인터페이스가\s*없습니다\.",
]


def _wlan_unavailable_message(std: str) -> Optional[str]:
    if not std:
        return None
    for pat in NO_WLAN_PATTERNS:
        if re.search(pat, std, re.IGNORECASE):
            return "이 시스템에서 무선(Wi-Fi) 인터페이스를 찾지 못했습니다."
    return None


# ---------------- 자동 복구 (관리자 한정) ----------------

def _start_wlan_service() -> None:
    cmds = [
        r'powershell -NoProfile -Command "Try { Set-Service -Name WlanSvc -StartupType Automatic; Start-Service WlanSvc -ErrorAction Stop } Catch {}"',
        r'sc config WlanSvc start= auto',
        r'net start WlanSvc',
    ]
    for c in cmds:
        _exec(c)


def _valid_netsh_iface_output(s: str) -> bool:
    """인터페이스 상세 출력이 '정상'인지 판별(에러 문구/빈 출력 배제)"""
    if not s:
        return False
    if re.search(r"(not registered with the router|지정한 인터페이스가 등록되어 있지 않습니다)", s, re.I):
        return False
    if _wlan_unavailable_message(s):
        return False
    # 정상 출력에 흔한 키들
    return bool(re.search(r"(Admin State|상태\s*:|State\s*:)", s, re.I))


def _list_wireless_interface_names() -> List[str]:
    names: List[str] = []

    # (1) PowerShell: 어댑터 이름
    ps = r'''powershell -NoProfile -Command "$ErrorActionPreference='SilentlyContinue'; Get-NetAdapter -IncludeHidden | Where-Object { $_.InterfaceDescription -match 'Wireless|802\.11|Wi-?Fi|WLAN' -or $_.Name -match 'Wireless|Wi-?Fi|무선|WLAN' } | Select-Object -ExpandProperty Name"'''
    out = _exec(ps)
    for ln in out.splitlines():
        n = ln.strip().strip('"')
        if n and n not in names:
            names.append(n)

    # (2) netsh wlan show interfaces → Name: 라인
    netsh = _first_nonempty_output([
        "netsh wlan show interfaces",
        "chcp 65001>NUL & netsh wlan show interfaces",
    ])
    if _valid_netsh_iface_output(netsh):
        for m in re.finditer(r"^\s*Name\s*:\s*(.+?)\s*$", netsh, re.MULTILINE | re.IGNORECASE):
            n = m.group(1).strip().strip('"')
            if n and n not in names:
                names.append(n)

    # (3) 과거 표준명 후보는 **실재 검증 통과 시에만** 추가
    for hint in ["Wi-Fi", "무선 네트워크 연결", "Wireless Network Connection", "WLAN"]:
        s = _exec(fr'netsh interface show interface name="{hint}"')
        if _valid_netsh_iface_output(s):
            if hint not in names:
                names.append(hint)

    return names


def _enable_wireless_interfaces() -> None:
    for name in _list_wireless_interface_names():
        _exec(fr'netsh interface set interface name="{name}" admin=enabled')


def _attempt_env_autofix(is_admin: bool) -> None:
    if not is_admin:
        # 비관리자면 건드리지 않고 리턴(에러 스팸 방지)
        return
    _start_wlan_service()
    _enable_wireless_interfaces()


def _assert_wlan_available(autofix: bool, is_admin: bool) -> None:
    def check_once() -> Tuple[bool, str]:
        s = _first_nonempty_output([
            "netsh wlan show interfaces",
            "chcp 65001>NUL & netsh wlan show interfaces",
        ])
        msg = _wlan_unavailable_message(s)
        return (msg is None, s)

    ok, s = check_once()
    if ok:
        return
    if autofix:
        _attempt_env_autofix(is_admin=is_admin)
        ok2, s2 = check_once()
        if ok2:
            return
        s = s2
    raise RuntimeError(
        "무선(Wi-Fi) 인터페이스를 찾지 못했습니다."
        + ("" if is_admin else " (관리자 권한이 아니어서 자동 복구를 수행하지 못했습니다.)")
        + "\n확인사항:\n"
          "  1) 관리자 권한으로 실행했는지\n"
          "  2) 장치 관리자에서 Wi-Fi 어댑터가 존재/활성화인지\n"
          "  3) 서비스 'WLAN AutoConfig(WlanSvc)'가 실행 중인지\n"
          "  4) VM/서버라면 무선 어댑터가 실제로 존재하는지"
        + f"\n(진단 스니펫: {s[:300].replace(chr(13), '\\r').replace(chr(10), '\\n')})"
    )


# ---------------- 프로필 파싱 ----------------

def _parse_profiles_hybrid(std: str) -> List[str]:
    """레거시 라인 스캔 우선 → 정규식 폴백. (레거시 우선순위 유지)"""
    logging.debug(f"프로필 파싱 입력 (첫 200자): {std[:200]}...")
    names = []
    # 한 번에 처리하는 정규식 대신, 각 줄을 순회하며 파싱하여 안정성 확보
    profile_line_pat = re.compile(r"(?:모든\s*사용자\s*프로필|All\s*User\s*Profile)\s*:\s*(.+)$")
    for line in std.splitlines():
        match = profile_line_pat.search(line.strip())
        if match:
            profile_name = match.group(1).strip()
            # 프로필명이 유효한지 확인 (쉼표나 특수문자 제거)
            if profile_name and profile_name != "<None>":
                # 쉼표로 분리된 경우 첫 번째 항목만 사용
                if ',' in profile_name:
                    profile_name = profile_name.split(',')[0].strip()
                # 유효한 프로필명인지 확인 (공백만 있는 경우 제외)
                if profile_name and not profile_name.isspace():
                    names.append(profile_name)
    
    logging.debug(f"라인별 파싱으로 발견된 프로필: {names}")
    return names


def _get_profiles_stdout() -> str:
    """
    표준 경로: 'show profiles' → 실패/빈출력 시 'show profile'(단수) 폴백.
    두 경우 모두 UTF-8 코드페이지 시도 포함.
    """
    std = _first_nonempty_output([
        "netsh wlan show profiles",
        "chcp 65001>NUL & netsh wlan show profiles",
    ])
    if not std.strip():
        std = _first_nonempty_output([
            "netsh wlan show profile",
            "chcp 65001>NUL & netsh wlan show profile",
        ])
    return std or ""


# ---------------- 명령 실행 유틸 ----------------
def _exec(cmd: str) -> str:
    out_list = ensure_command_executed(cmd)
    return (get_str_from_list(out_list) or "").strip()


def _first_nonempty_output(cmds: List[str]) -> str:
    for cmd in cmds:
        s = _exec(cmd)
        if s:
            return s
    return ""


# ---------------- 프로필/키 파서 공통 정규식 ----------------
_PAT_PROFILE_LINE = re.compile(
    r"^(?:모든\s*사용자\s*프로필|All\s*User\s*Profile)\s*:\s*(.+?)\s*$",
    re.MULTILINE
)
_PAT_KEY_LINE = re.compile(
    r"^(?:키\s*콘텐츠|Key\s*Content)\s*:\s*(.+?)\s*$",
    re.MULTILINE
)


# ---------------- 폴백 #1: 사용자가 처음에 하신 "레거시 방식" ----------------
def _legacy_original_profiles() -> List[str]:
    """
    - netsh wlan show profile (단수)도 시도
    - 라인 스캔으로 '모든 사용자 프로필 :' / 'All User Profile' 추출
    """
    std = _first_nonempty_output([
        "netsh wlan show profile",
        "chcp 65001>NUL & netsh wlan show profile",
        "netsh wlan show profiles",
        "chcp 65001>NUL & netsh wlan show profiles",
    ])
    names: List[str] = []
    for ln in [ln.strip() for ln in std.splitlines() if ln.strip()]:
        if "모든 사용자 프로필" in ln and ":" in ln:
            names.append(ln.split(":", 1)[1].strip().strip('"'));
            continue
        if "All User Profile" in ln and ":" in ln:
            names.append(ln.split(":", 1)[1].strip().strip('"'))
    names = list(dict.fromkeys([n for n in names if n]))
    return names


def _legacy_original_pw(profile: str) -> Optional[str]:
    """
    - key=clear 뒤에 | find "키 콘텐츠"/"Key Content" 파이프 사용
    - 코드페이지 이슈 대비 2회 시도
    """
    candidates = [
        f'netsh wlan show profile name="{profile}" key=clear | find "키 콘텐츠"',
        f'netsh wlan show profile name="{profile}" key=clear | find "Key Content"',
        f'chcp 65001>NUL & netsh wlan show profile name="{profile}" key=clear | find "키 콘텐츠"',
        f'chcp 65001>NUL & netsh wlan show profile name="{profile}" key=clear | find "Key Content"',
    ]
    for cmd in candidates:
        s = _exec(cmd)
        if not s:
            continue
        # 예: "    키 콘텐츠              : password123"
        for ln in [ln.strip() for ln in s.splitlines() if ln.strip()]:
            if ":" in ln:
                return ln.split(":", 1)[1].strip()
    return None


# ---------------- 기존 코드의 일반 경로/보조 폴백들 ----------------
def _list_profiles_via_netsh() -> List[str]:
    std = _first_nonempty_output([
        "netsh wlan show profiles",
        "chcp 65001>NUL & netsh wlan show profiles",
    ])
    names: List[str] = []
    for ln in [ln.strip() for ln in std.splitlines() if ln.strip()]:
        if "모든 사용자 프로필" in ln and ":" in ln:
            names.append(ln.split(":", 1)[1].strip().strip('"'));
            continue
        if "All User Profile" in ln and ":" in ln:
            names.append(ln.split(":", 1)[1].strip().strip('"'))
    if not names:
        names = [m.strip('" ').strip() for m in _PAT_PROFILE_LINE.findall(std)]
    names = list(dict.fromkeys([n for n in names if n]))
    return names


def _get_pw_via_netsh(profile: str) -> Optional[str]:
    std = _first_nonempty_output([
        f'netsh wlan show profile name="{profile}" key=clear',
        f'chcp 65001>NUL & netsh wlan show profile name="{profile}" key=clear',
    ])
    for ln in [ln.strip() for ln in std.splitlines() if ln.strip()]:
        if ("키 콘텐츠" in ln or "Key Content" in ln) and ":" in ln:
            return ln.split(":", 1)[1].strip()
    m = _PAT_KEY_LINE.search(std)
    return m.group(1).strip() if m else None


def _list_profiles_from_registry() -> List[str]:
    names: List[str] = []
    roots = [
        r'HKLM\SOFTWARE\Microsoft\WlanSvc\Interfaces',
        r'HKLM\SOFTWARE\Microsoft\WlanSvc\Profiles',
    ]
    for root in roots:
        sub_out = _exec(f'reg query "{root}"')
        if not sub_out:
            continue
        subkeys = [ln.strip() for ln in sub_out.splitlines() if ln.strip().startswith(root + "\\")]
        for sk in list(subkeys):
            if sk.lower().endswith("\\profiles"):
                more = _exec(f'reg query "{sk}"')
                if more:
                    subkeys += [ln.strip() for ln in more.splitlines() if ln.strip().startswith(sk + "\\")]
                continue
        for sk in subkeys:
            q = _exec(f'reg query "{sk}" /v ProfileName')
            for ln in q.splitlines():
                if "ProfileName" in ln:
                    parts = [p for p in ln.split("  ") if p.strip()]
                    if len(parts) >= 3:
                        name = parts[-1].strip().strip('"')
                        if name and name not in names:
                            names.append(name)
    return names


def ensure_wifi_pw_printed_core(auto_fix: bool = True, skip_admin_check: bool = False):
    """
    Wi-Fi 프로필/비밀번호를 출력 및 반환.
    - auto_fix=True: 관리자 권한일 때만 서비스/인터페이스 자동 복구 시도
    - skip_admin_check=True: 관리자 권한 체크 건너뛰기 (테스트용)
    - 반환: (wifi_name, wifi_pw or None)
    """
    is_admin = _is_admin()
    if not is_admin and not skip_admin_check:
        # 권한 부족이면 먼저 명확히 리턴 (당신 로그의 Access denied 방지)
        raise RuntimeError(
            "관리자 권한이 필요합니다. 현재 권한으로는 WLAN 서비스/인터페이스 제어가 거부됩니다.\n"
            "관리자 PowerShell에서 다음 중 하나로 실행하세요:\n"
            "  1) python C:\\Users\\pk_system_security_literal\\Downloads\\task_orchestrator_cli\\resources\\wrappers\\pk_ensure_wifi_pw_printed.py\n"
            "  2) 또는 스크립트를 마우스 오른쪽 → '관리자 권한으로 실행'\n"
        )

    # 0) 환경 점검(+자동 복구)
    _assert_wlan_available(autofix=auto_fix, is_admin=is_admin)

    # 1) 프로필 목록
    std = _get_profiles_stdout()

    msg = _wlan_unavailable_message(std)
    if msg:
        if auto_fix and is_admin:
            _attempt_env_autofix(is_admin=True)
            std = _get_profiles_stdout()
            msg = _wlan_unavailable_message(std)
        if msg:
            raise RuntimeError(
                msg + " (profiles 조회 중)\n무선 어댑터/서비스 상태를 먼저 복구하세요."
                + f"\n(스니펫: {std[:300].replace(chr(13), '\\r').replace(chr(10), '\\n')})"
            )

    # 2) 파싱
    wifi_names = _parse_profiles_hybrid(std)
    if not wifi_names:
        snippet = (std or "")[:300].replace("\r", "\\r").replace("\n", "\\n")
        raise RuntimeError(
            "Wi-Fi 프로필을 찾지 못했습니다. 'netsh wlan show profiles' 실제 출력 형식을 확인하세요. "
            f"(첫 300자 스니펫: {snippet})"
        )

    # 3) 첫 번째 프로필 사용
    wifi_name = wifi_names[0]
    logging.debug(f'''wifi_name={wifi_name} {'%%%FOO%%%' if LTA else ''}''')

    # 4) 비밀번호 추출 — 레거시 파이프(| find) 우선 → 정규식 폴백
    # [LEGACY FIRST] 파이프 방식
    pipe_cmds = [
        f'netsh wlan show profile name="{wifi_name}" key=clear | find "키 콘텐츠"',
        f'netsh wlan show profile name="{wifi_name}" key=clear | find "Key Content"',
        f'chcp 65001>NUL & netsh wlan show profile name="{wifi_name}" key=clear | find "키 콘텐츠"',
        f'chcp 65001>NUL & netsh wlan show profile name="{wifi_name}" key=clear | find "Key Content"',
    ]
    wifi_pw: Optional[str] = None
    for cmd in pipe_cmds:
        s = _exec(cmd)
        if not s:
            continue
        for ln in [ln.strip() for ln in s.splitlines() if ln.strip()]:
            if ":" in ln:
                wifi_pw = ln.split(":", 1)[1].strip()
                break
        if wifi_pw:
            break

    # 정규식 폴백(전체 출력에서 키 라인 찾기)
    if not wifi_pw:
        prof_std = _first_nonempty_output([
            f'netsh wlan show profile name="{wifi_name}" key=clear',
            f'chcp 65001>NUL & netsh wlan show profile name="{wifi_name}" key=clear',
        ])
        m = re.search(r"^(?:키\s*콘텐츠|Key\s*Content)\s*:\s*(.+?)\s*$", prof_std, re.MULTILINE)
        if m:
            wifi_pw = m.group(1).strip()

    # 5) 로그/출력
    if wifi_pw:
        if LTA:
            logging.debug(rf'''{ANSI_COLOR_MAP['YELLOW']}{wifi_name}: {wifi_pw}{ANSI_COLOR_MAP['RESET']}" {'%%%FOO%%%' if LTA else ''}''')
        else:
            logging.debug(rf'''{ANSI_COLOR_MAP['YELLOW']}{wifi_name}: {ensure_sensitive_info_masked(wifi_pw)}{ANSI_COLOR_MAP['RESET']}" {'%%%FOO%%%' if LTA else ''}''')

    else:
        logging.warning(
            f'비밀번호(키 콘텐츠)를 찾지 못했습니다. 프로필="{wifi_name}". '
            f"관리자 권한인지 / 개방형 네트워크인지 / 로밍 프로필인지 확인하세요."
        )
        logging.debug(f"{wifi_name}: (비밀번호 없음 또는 확인 불가)")

    return wifi_name, wifi_pw
