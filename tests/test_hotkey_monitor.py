#!/usr/bin/env python3
"""
단축키 모니터링 시스템 테스트 스크립트
"""

import sys
import os

# 프로젝트 루트를 Python 경로에 추가
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from pkg_py.functions_split.ensure_hotkey_monitor_started import ensure_hotkey_monitor_started
from pkg_py.functions_split.ensure_printed import ensure_printed


def test_hotkey_monitor():
    """단축키 모니터링 테스트"""
    ensure_printed("🧪 단축키 모니터링 테스트 시작", print_color='blue')
    ensure_printed("💡 Ctrl+Alt+P를 눌러서 테스트하세요", print_color='cyan')
    ensure_printed("💡 종료하려면 Ctrl+C를 누르세요", print_color='yellow')
    
    # 모니터링 시작
    ensure_hotkey_monitor_started(hotkey="ctrl+alt+p", auto_start=True)


def test_instant_execution():
    """즉시 실행 테스트"""
    ensure_printed("⚡ 즉시 실행 테스트", print_color='blue')
    
    from pkg_py.functions_split.ensure_pk_system_started_instant import ensure_pk_system_started_instant
    ensure_pk_system_started_instant()


def test_minimal_execution():
    """최소 실행 테스트"""
    ensure_printed("🚀 최소 실행 테스트", print_color='blue')
    
    from pkg_py.functions_split.ensure_pk_system_started_instant import ensure_pk_system_started_minimal
    ensure_pk_system_started_minimal()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        test_mode = sys.argv[1]
        
        if test_mode == "monitor":
            test_hotkey_monitor()
        elif test_mode == "instant":
            test_instant_execution()
        elif test_mode == "minimal":
            test_minimal_execution()
        else:
            ensure_printed("❌ 잘못된 테스트 모드", print_color='red')
            ensure_printed("사용법: python test_hotkey_monitor.py [monitor|instant|minimal]", print_color='yellow')
    else:
        # 기본: 모니터링 테스트
        test_hotkey_monitor() 