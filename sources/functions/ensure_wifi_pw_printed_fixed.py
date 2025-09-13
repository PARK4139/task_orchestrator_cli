#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wi-Fi 비밀번호 출력 함수 - 수정된 버전

기존 ensure_wifi_pw_printed 함수의 프로필 파싱 문제를 해결한 버전
"""

import subprocess
from typing import Optional, Tuple

import logging


def ensure_wifi_pw_printed_fixed() -> Tuple[Optional[str], Optional[str]]:
    from sources.functions.ensure_sensitive_info_masked import ensure_sensitive_info_masked
    try:
        # n. Wi-Fi 프로필 목록 조회
        logging.info("Wi-Fi 프로필 목록을 조회합니다...")

        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'profiles'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode != 0:
            logging.error(f"Wi-Fi 프로필 조회 실패: {result.stderr}")
            return None, None

        # n. 프로필 이름 파싱
        wifi_profiles = []
        lines = result.stdout.split('\n')

        for line in lines:
            line = line.strip()
            # 한국어와 영어 모두 지원
            if ('모든 사용자 프로필' in line or 'All User Profile' in line) and ':' in line:
                profile_name = line.split(':', 1)[1].strip()
                if profile_name and profile_name != '<None>':
                    wifi_profiles.append(profile_name)
                    logging.info(f"발견된 Wi-Fi 프로필: {ensure_sensitive_info_masked(profile_name)}")

        if not wifi_profiles:
            logging.warning("저장된 Wi-Fi 프로필이 없습니다.")
            return None, None

        # n. 첫 번째 프로필의 비밀번호 조회
        wifi_name = wifi_profiles[0]
        logging.info(f"선택된 Wi-Fi 프로필: {ensure_sensitive_info_masked(wifi_name)}")

        # n. 비밀번호 조회
        wifi_password = get_wifi_password(wifi_name)

        if wifi_password:
            logging.info(f"Wi-Fi 비밀번호 조회 성공: {ensure_sensitive_info_masked(wifi_name)}")
        else:
            logging.warning(f"Wi-Fi 비밀번호 조회 실패: {ensure_sensitive_info_masked(wifi_name)}")

        return wifi_name, wifi_password

    except Exception as e:
        logging.error(f"Wi-Fi 정보 조회 중 오류: {e}")
        return None, None


def get_wifi_password(profile_name: str) -> Optional[str]:
    """
    특정 Wi-Fi 프로필의 비밀번호 조회

    Args:
        profile_name: Wi-Fi 프로필 이름

    Returns:
        Optional[str]: Wi-Fi 비밀번호 (없으면 None)
    """
    from sources.functions.ensure_sensitive_info_masked import ensure_sensitive_info_masked


    try:
        # 비밀번호 조회 명령어 실행
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'profile', f'name={ensure_sensitive_info_masked(profile_name)}', 'key=clear'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode != 0:
            logging.error(f"프로필 '{profile_name}' 정보 조회 실패: {result.stderr}")
            return None

        # 키 콘텐츠 찾기
        lines = result.stdout.split('\n')
        for line in lines:
            line = line.strip()
            # 한국어와 영어 모두 지원
            if ('키 콘텐츠' in line or 'Key Content' in line) and ':' in line:
                password = line.split(':', 1)[1].strip()
                if password:
                    logging.debug(f"비밀번호 발견: {ensure_sensitive_info_masked(password)}")
                    return password

        logging.info(f"프로필 '{profile_name}'에 비밀번호가 설정되지 않았거나 접근할 수 없습니다.")
        return None

    except Exception as e:
        logging.error(f"비밀번호 조회 중 오류: {e}")
        return None


def connect_to_wifi(profile_name: str) -> bool:
    """
    저장된 Wi-Fi 프로필로 연결
    
    Args:
        profile_name: 연결할 Wi-Fi 프로필 이름
        
    Returns:
        bool: 연결 성공 여부
    """

    try:
        logging.info(f"Wi-Fi '{profile_name}'에 연결 시도...")

        result = subprocess.run(
            ['netsh', 'wlan', 'connect', f'name={profile_name}'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode == 0:
            logging.info(f"Wi-Fi '{profile_name}' 연결 명령 성공")

            # 연결 상태 확인 (몇 초 대기 후)
            import time
            time.sleep(3)

            if check_wifi_connection():
                logging.info(f"Wi-Fi '{profile_name}' 연결 완료!")
                return True
            else:
                logging.warning(f"Wi-Fi '{profile_name}' 연결 명령은 성공했지만 연결 확인 실패")
                return False
        else:
            logging.error(f"Wi-Fi '{profile_name}' 연결 실패: {result.stderr}")
            return False

    except Exception as e:
        logging.error(f"Wi-Fi 연결 중 오류: {e}")
        return False


def check_wifi_connection() -> bool:
    """
    현재 Wi-Fi 연결 상태 확인
    
    Returns:
        bool: Wi-Fi 연결 여부
    """

    try:
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'interfaces'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode == 0:
            output = result.stdout.lower()

            # 연결 상태 확인
            if 'state' in output and 'connected' in output:
                # 연결된 네트워크 정보 추출
                lines = result.stdout.split('\n')
                ssid = None
                ip = None

                for line in lines:
                    line = line.strip()
                    if 'ssid' in line.lower() and 'bssid' not in line.lower() and ':' in line:
                        ssid = line.split(':', 1)[1].strip()
                    elif 'state' in line.lower() and ':' in line:
                        state = line.split(':', 1)[1].strip()
                        if state.lower() == 'connected':
                            logging.info(f"Wi-Fi 연결됨: {ssid if ssid else '알 수 없음'}")
                            return True

        logging.info("Wi-Fi 연결되지 않음")
        return False

    except Exception as e:
        logging.error(f"Wi-Fi 상태 확인 중 오류: {e}")
        return False


def get_current_ip() -> Optional[str]:
    """
    현재 IP 주소 조회
    
    Returns:
        Optional[str]: 현재 IP 주소
    """

    try:
        result = subprocess.run(
            ['ipconfig'],
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        if result.returncode == 0:
            lines = result.stdout.split('\n')

            # Wi-Fi 어댑터의 IPv4 주소 찾기
            in_wifi_section = False

            for line in lines:
                line = line.strip()

                if 'wireless lan adapter wi-fi' in line.lower():
                    in_wifi_section = True
                    continue
                elif 'adapter' in line.lower() and in_wifi_section:
                    in_wifi_section = False
                    continue

                if in_wifi_section and 'ipv4' in line.lower() and ':' in line:
                    ip = line.split(':', 1)[1].strip()
                    logging.info(f"현재 Wi-Fi IP: {ip}")
                    return ip

        return None

    except Exception as e:
        logging.error(f"IP 주소 조회 중 오류: {e}")
        return None


# 메인 실행 함수
# def ensure_wifi_pw_printed_fixed_v2():
#     """Wi-Fi 정보 조회 및 연결 테스트"""
#     from sources.functions.ensure_matter_device_controlled import ensure_sensitive_info_masked
#
#     logging.debug("Wi-Fi 정보 조회 및 연결 테스트 ===")
#
#     # n. Wi-Fi 프로필 및 비밀번호 조회
#     wifi_name, wifi_password = ensure_wifi_pw_printed_fixed()
#
#     if wifi_name:
#         logging.debug(f"✅ Wi-Fi 이름: {ensure_sensitive_info_masked((wifi_name))}")
#         if wifi_password:
#             logging.debug(f"🔑 Wi-Fi 비밀번호: {ensure_sensitive_info_masked((wifi_password))}")
#         else:
#             logging.debug("🔑 Wi-Fi 비밀번호: (없음 또는 접근 불가)")
#
#         # n. 현재 연결 상태 확인
#         if check_wifi_connection():
#             logging.debug("📶 현재 Wi-Fi 연결됨")
#             current_ip = get_current_ip()
#             if current_ip:
#                 logging.debug(f"🌐 현재 IP: {current_ip}")
#         else:
#             logging.debug("📶 현재 Wi-Fi 연결되지 않음")
#
#             # n. 연결 시도
#             logging.debug(f"\n🔗 '{wifi_name}'에 연결 시도...")
#             if connect_to_wifi(wifi_name):
#                 logging.debug("✅ Wi-Fi 연결 성공!")
#                 current_ip = get_current_ip()
#                 if current_ip:
#                     logging.debug(f"🌐 연결된 IP: {current_ip}")
#             else:
#                 logging.debug("❌ Wi-Fi 연결 실패")
#     else:
#         logging.debug("❌ Wi-Fi 프로필을 찾을 수 없습니다.")
#
#     logging.debug("=== 테스트 완료 ===")
