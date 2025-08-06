#!/usr/bin/env python3
"""
Linux/WSL 전용 PK System 관리자
Path 객체 적극 활용
"""
import os
import platform
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path
import time

from pkg_py.system_object.urls import UV_URL_LINUX
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP

from pkg_py.functions_split.ensure_pk_system_enabled_refactored import PlatformManager, CommonUtils

class LinuxManager(PlatformManager):
    """Linux/WSL 플랫폼 관리자"""
    
    def __init__(self):
        super().__init__()
        self.user_home = Path.home()
        
        # Linux 전용 Path 객체들
        self.d_venv_bin = self.pk_system_path / ".venv_linux" / "bin"
        self.f_uv_binary_linux = self.pkg_linux_path / "uv"
        self.f_fzf_binary_linux = self.pkg_linux_path / "fzf"
        self.f_venv_python_linux = self.d_venv_bin / "python"
        self.f_uv_tar_linux = self.downloads_path / "uv.tar.gz"
        self.f_fzf_tar_linux = self.downloads_path / "fzf.tar.gz"
        
        # 셸 설정 파일들
        self.bashrc_path = self.user_home / ".bashrc"
        self.zshrc_path = self.user_home / ".zshrc"
    
    def install_uv(self, max_retry: int = 2) -> bool:
        """UV 설치 (Linux/WSL)"""
        try:
            # Lazy import to avoid circular dependency
            try:
                from pkg_py.functions_split.ensure_printed import ensure_printed
                from pkg_py.system_object.map_massages import PkMessages2025
            except ImportError:
                def fallback_print(msg, **kwargs):
                    print(msg)
                ensure_printed = fallback_print
                PkMessages2025 = type('PkMessages2025', (), {
                    'LINUX_UV_INSTALLATION': 'UV 설치 (Linux/WSL)',
                    'LINUX_UV_ALREADY_INSTALLED': 'uv가 이미 설치되어 있습니다',
                    'LINUX_UV_BINARY_ALREADY_INSTALLED': 'uv가 이미 설치되어 있습니다',
                    'LINUX_UV_INSTALLATION_COMPLETE': 'uv 설치 완료'
                })()

            print(f"\n[{PkMessages2025.LINUX_UV_INSTALLATION}]")
            
            # 이미 설치되어 있는지 확인
            result = subprocess.run([self.f_uv_binary_linux, "--version"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"[{PkMessages2025.LINUX_UV_ALREADY_INSTALLED}] {PK_ANSI_COLOR_MAP['GREEN']}버전={result.stdout.strip()} {PK_ANSI_COLOR_MAP['RESET']}")
                return True
            
            # UV 다운로드 및 설치
            for attempt in range(max_retry):
                try:
                    # UV 설치 스크립트 다운로드 및 실행
                    install_script = """
                    curl -LsSf https://astral.sh/uv/install.sh | sh
                    """
                    
                    result = subprocess.run(install_script, shell=True, 
                                          capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        # 설치 확인
                        result = subprocess.run([self.f_uv_binary_linux, "--version"], 
                                              capture_output=True, text=True)
                        if result.returncode == 0:
                            print(f"[{PkMessages2025.LINUX_UV_INSTALLATION_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}버전={result.stdout.strip()} {PK_ANSI_COLOR_MAP['RESET']}")
                            return True
                        else:
                            print(f"[{PkMessages2025.LINUX_UV_BINARY_ALREADY_INSTALLED}] {PK_ANSI_COLOR_MAP['GREEN']}경로={self.f_uv_binary_linux} {PK_ANSI_COLOR_MAP['RESET']}")
                            return True
                    else:
                        print(f"UV 설치 실패 (시도 {attempt + 1}/{max_retry}): {result.stderr}")
                        if attempt < max_retry - 1:
                            time.sleep(2)
                            continue
                        else:
                            return False
                            
                except Exception as e:
                    print(f"UV 설치 중 오류 (시도 {attempt + 1}/{max_retry}): {e}")
                    if attempt < max_retry - 1:
                        time.sleep(2)
                        continue
                    else:
                        return False
            
            return False
            
        except Exception as e:
            print(f"UV 설치 중 예상치 못한 오류: {e}")
            return False


    def install_fzf(self, max_retry: int = 2) -> bool:
        """FZF 설치 (Linux/WSL)"""
        try:
            # Lazy import to avoid circular dependency
            try:
                from pkg_py.functions_split.ensure_printed import ensure_printed
                from pkg_py.system_object.map_massages import PkMessages2025
            except ImportError:
                def fallback_print(msg, **kwargs):
                    print(msg)
                ensure_printed = fallback_print
                PkMessages2025 = type('PkMessages2025', (), {
                    'LINUX_FZF_INSTALLATION': 'FZF 설치 (Linux/WSL)',
                    'LINUX_FZF_ALREADY_INSTALLED': 'fzf가 이미 설치되어 있습니다',
                    'LINUX_FZF_BINARY_ALREADY_INSTALLED': 'fzf가 이미 설치되어 있습니다',
                    'LINUX_FZF_INSTALLATION_COMPLETE': 'fzf 설치 완료'
                })()

            print(f"\n[{PkMessages2025.LINUX_FZF_INSTALLATION}]")
            
            # 이미 설치되어 있는지 확인
            result = subprocess.run([self.f_fzf_binary_linux, "--version"], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                print(f"[{PkMessages2025.LINUX_FZF_ALREADY_INSTALLED}] {PK_ANSI_COLOR_MAP['GREEN']}버전={result.stdout.strip()} {PK_ANSI_COLOR_MAP['RESET']}")
                return True
            
            # FZF 설치
            for attempt in range(max_retry):
                try:
                    # FZF 설치 스크립트 다운로드 및 실행
                    install_script = """
                    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
                    ~/.fzf/install --all
                    """
                    
                    result = subprocess.run(install_script, shell=True, 
                                          capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        # 설치 확인
                        result = subprocess.run([self.f_fzf_binary_linux, "--version"], 
                                              capture_output=True, text=True)
                        if result.returncode == 0:
                            print(f"[{PkMessages2025.LINUX_FZF_INSTALLATION_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}버전={result.stdout.strip()} {PK_ANSI_COLOR_MAP['RESET']}")
                            return True
                        else:
                            print(f"[{PkMessages2025.LINUX_FZF_BINARY_ALREADY_INSTALLED}] {PK_ANSI_COLOR_MAP['GREEN']}경로={self.f_fzf_binary_linux} {PK_ANSI_COLOR_MAP['RESET']}")
                            return True
                    else:
                        print(f"FZF 설치 실패 (시도 {attempt + 1}/{max_retry}): {result.stderr}")
                        if attempt < max_retry - 1:
                            time.sleep(2)
                            continue
                        else:
                            return False
                            
                except Exception as e:
                    print(f"FZF 설치 중 오류 (시도 {attempt + 1}/{max_retry}): {e}")
                    if attempt < max_retry - 1:
                        time.sleep(2)
                        continue
                    else:
                        return False
            
            return False
            
        except Exception as e:
            print(f"FZF 설치 중 예상치 못한 오류: {e}")
            return False


    def setup_path(self) -> bool:
        """Linux PATH 설정"""
        try:
            # Lazy import to avoid circular dependency
            try:
                from pkg_py.functions_split.ensure_printed import ensure_printed
                from pkg_py.system_object.map_massages import PkMessages2025
            except ImportError:
                def fallback_print(msg, **kwargs):
                    print(msg)
                ensure_printed = fallback_print
                PkMessages2025 = type('PkMessages2025', (), {
                    'LINUX_PATH_SETUP': 'Linux PATH 설정',
                    'LINUX_SHELL_PATH_SETUP_COMPLETE': 'shell PATH 설정 완료',
                    'LINUX_SHELL_CONFIG_NOT_FOUND': 'shell 설정 파일을 찾을 수 없습니다',
                    'LINUX_PATH_SETUP_COMPLETE': 'Linux PATH 설정 완료'
                })()

            print(f"\n[{PkMessages2025.LINUX_PATH_SETUP}]")
            
            # 사용자의 기본 shell 확인
            shell = os.environ.get('SHELL', '/bin/bash')
            shell_type = os.path.basename(shell)
            
            # 설정 파일 경로
            config_files = {
                'bash': os.path.expanduser('~/.bashrc'),
                'zsh': os.path.expanduser('~/.zshrc'),
                'fish': os.path.expanduser('~/.config/fish/config.fish')
            }
            
            config_file = config_files.get(shell_type, config_files['bash'])
            
            # PATH 설정 추가
            path_config = f"""
            # PK System PATH 설정
            export PATH="$HOME/.local/bin:$PATH"
            export PATH="$HOME/.cargo/bin:$PATH"
            """
            
            try:
                # 기존 설정 확인
                with open(config_file, 'r') as f:
                    content = f.read()
                
                if 'PK System PATH 설정' not in content:
                    # 설정 추가
                    with open(config_file, 'a') as f:
                        f.write(path_config)
                    print(f"[{PkMessages2025.LINUX_SHELL_PATH_SETUP_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}파일={config_file} {PK_ANSI_COLOR_MAP['RESET']}")
                else:
                    print(f"[{PkMessages2025.LINUX_SHELL_PATH_SETUP_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}파일={config_file} {PK_ANSI_COLOR_MAP['RESET']}")
                    
            except FileNotFoundError:
                print(f"[{PkMessages2025.LINUX_SHELL_CONFIG_NOT_FOUND}] {PK_ANSI_COLOR_MAP['YELLOW']}파일={config_file} {PK_ANSI_COLOR_MAP['RESET']}")
                # 파일 생성
                with open(config_file, 'w') as f:
                    f.write(path_config)
                print(f"[{PkMessages2025.LINUX_SHELL_PATH_SETUP_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}파일생성={config_file} {PK_ANSI_COLOR_MAP['RESET']}")
            
            print(f"[{PkMessages2025.LINUX_PATH_SETUP_COMPLETE}]")
            return True
            
        except Exception as e:
            print(f"Linux PATH 설정 중 오류: {e}")
            return False


    def setup_aliases(self) -> bool:
        """Linux 별칭 설정"""
        try:
            # Lazy import to avoid circular dependency
            try:
                from pkg_py.functions_split.ensure_printed import ensure_printed
                from pkg_py.system_object.map_massages import PkMessages2025
            except ImportError:
                def fallback_print(msg, **kwargs):
                    print(msg)
                ensure_printed = fallback_print
                PkMessages2025 = type('PkMessages2025', (), {
                    'LINUX_ALIAS_SETUP': 'Linux 별칭 설정',
                    'LINUX_ALIAS_SETUP_COMPLETE': 'Linux 별칭 설정 완료',
                    'LINUX_ALIAS_SETUP_FAILED': 'Linux 별칭 설정 실패'
                })()

            print(f"\n[{PkMessages2025.LINUX_ALIAS_SETUP}]")
            
            # 별칭 설정 (PATH 설정에 포함됨)
            alias_config = f"""
            # PK System 별칭 설정
            alias pk='python -m pkg_py.functions_split.ensure_pk_system_enabled'
            alias uv='{self.f_uv_binary_linux}'
            alias fzf='{self.f_fzf_binary_linux}'
            """
            
            # 사용자의 기본 shell 확인
            shell = os.environ.get('SHELL', '/bin/bash')
            shell_type = os.path.basename(shell)
            
            # 설정 파일 경로
            config_files = {
                'bash': os.path.expanduser('~/.bashrc'),
                'zsh': os.path.expanduser('~/.zshrc'),
                'fish': os.path.expanduser('~/.config/fish/config.fish')
            }
            
            config_file = config_files.get(shell_type, config_files['bash'])
            
            try:
                # 기존 설정 확인
                with open(config_file, 'r') as f:
                    content = f.read()
                
                if 'PK System 별칭 설정' not in content:
                    # 설정 추가
                    with open(config_file, 'a') as f:
                        f.write(alias_config)
                
                print(f"[{PkMessages2025.LINUX_ALIAS_SETUP_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}상태=완료 {PK_ANSI_COLOR_MAP['RESET']}")
                return True
                
            except Exception as e:
                print(f"[{PkMessages2025.LINUX_ALIAS_SETUP_FAILED}] {PK_ANSI_COLOR_MAP['RED']}오류={e} {PK_ANSI_COLOR_MAP['RESET']}")
                return False
                
        except Exception as e:
            print(f"Linux 별칭 설정 중 오류: {e}")
            return False


    def sync_uv_packages(self) -> bool:
        """uv 패키지 동기화 (Linux)"""
        try:
            # Lazy import to avoid circular dependency
            try:
                from pkg_py.functions_split.ensure_printed import ensure_printed
                from pkg_py.system_object.map_massages import PkMessages2025
            except ImportError:
                def fallback_print(msg, **kwargs):
                    print(msg)
                ensure_printed = fallback_print
                PkMessages2025 = type('PkMessages2025', (), {
                    'LINUX_PACKAGE_SYNC': 'uv 패키지 동기화 (Linux)',
                    'LINUX_PYPROJECT_TOML_FOUND': 'pyproject.toml 찾음',
                    'LINUX_PYPROJECT_TOML_OR_ROOT_FOUND': 'pyproject.toml 또는 프로젝트 루트에서 찾음',
                    'LINUX_UV_SYNC_COMPLETE': 'Linux 전용 uv sync 완료'
                })()

            print(f"\n[{PkMessages2025.LINUX_PACKAGE_SYNC}]")
            
            # 프로젝트 루트 찾기
            work_root = Path.cwd()
            
            # pyproject.toml 파일 찾기
            pyproject_file = work_root / "pyproject.toml"
            if pyproject_file.exists():
                print(f"[{PkMessages2025.LINUX_PYPROJECT_TOML_FOUND}] {PK_ANSI_COLOR_MAP['GREEN']}경로={work_root} {PK_ANSI_COLOR_MAP['RESET']}")
            else:
                # 상위 디렉토리에서 찾기
                for parent in work_root.parents:
                    pyproject_file = parent / "pyproject.toml"
                    if pyproject_file.exists():
                        work_root = parent
                        print(f"[{PkMessages2025.LINUX_PYPROJECT_TOML_OR_ROOT_FOUND}] {PK_ANSI_COLOR_MAP['GREEN']}경로={work_root} {PK_ANSI_COLOR_MAP['RESET']}")
                        break
                else:
                    print("pyproject.toml 파일을 찾을 수 없습니다.")
                    return False
            
            # uv sync 실행
            try:
                result = subprocess.run([
                    str(self.f_uv_binary_linux), "sync", "--python", str(self.f_venv_python_linux)
                ], cwd=work_root, capture_output=True, text=True)
                
                if result.returncode == 0:
                    print(f"[{PkMessages2025.LINUX_UV_SYNC_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}상태=완료 {PK_ANSI_COLOR_MAP['RESET']}")
                    return True
                else:
                    print(f"uv sync 실패: {result.stderr}")
                    return False
                    
            except Exception as e:
                print(f"uv sync 중 오류: {e}")
                return False
                
        except Exception as e:
            print(f"uv 패키지 동기화 중 오류: {e}")
            return False


    def install_packages_with_venv_python(self) -> bool:
        """가상환경 Python으로 패키지 설치 (Linux)"""
        try:
            # Lazy import to avoid circular dependency
            try:
                from pkg_py.functions_split.ensure_printed import ensure_printed
                from pkg_py.system_object.map_massages import PkMessages2025
            except ImportError:
                def fallback_print(msg, **kwargs):
                    print(msg)
                ensure_printed = fallback_print
                PkMessages2025 = type('PkMessages2025', (), {
                    'LINUX_VENV_SETUP': '가상환경 Python으로 패키지 설치 (Linux)',
                    'LINUX_VENV_PYTHON_NOT_FOUND': '가상환경 Python을 찾을 수 없습니다',
                    'LINUX_VENV_PYTHON_FOUND': '가상환경 Python 사용',
                    'LINUX_PACKAGE_INSTALLING': '패키지 설치 중',
                    'LINUX_PACKAGE_INSTALL_COMPLETE': '패키지 설치 완료',
                    'LINUX_PACKAGE_INSTALL_FAILED': '패키지 설치 실패'
                })()

            print(f"\n[{PkMessages2025.LINUX_VENV_SETUP}]")
            
            # 가상환경 Python 확인
            if not self.f_venv_python_linux.exists():
                print(f"[{PkMessages2025.LINUX_VENV_PYTHON_NOT_FOUND}] {PK_ANSI_COLOR_MAP['RED']}경로={self.f_venv_python_linux} {PK_ANSI_COLOR_MAP['RESET']}")
                return False
            
            print(f"[{PkMessages2025.LINUX_VENV_PYTHON_FOUND}] {PK_ANSI_COLOR_MAP['GREEN']}경로={self.f_venv_python_linux} {PK_ANSI_COLOR_MAP['RESET']}")
            
            # 필수 패키지 설치
            packages = ["requests", "pathlib", "subprocess", "json", "time", "datetime"]
            
            for package in packages:
                try:
                    print(f"[{PkMessages2025.LINUX_PACKAGE_INSTALLING}] {PK_ANSI_COLOR_MAP['YELLOW']}패키지={package} {PK_ANSI_COLOR_MAP['RESET']}")
                    
                    result = subprocess.run([
                        str(self.f_venv_python_linux), "-m", "pip", "install", package
                    ], capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        print(f"[{PkMessages2025.LINUX_PACKAGE_INSTALL_COMPLETE}] {PK_ANSI_COLOR_MAP['GREEN']}패키지={package} {PK_ANSI_COLOR_MAP['RESET']}")
                    else:
                        print(f"[{PkMessages2025.LINUX_PACKAGE_INSTALL_FAILED}] {PK_ANSI_COLOR_MAP['RED']}패키지={package} 오류={result.stderr} {PK_ANSI_COLOR_MAP['RESET']}")
                        
                except Exception as e:
                    print(f"[{PkMessages2025.LINUX_PACKAGE_INSTALL_FAILED}] {PK_ANSI_COLOR_MAP['RED']}패키지={package} 오류={e} {PK_ANSI_COLOR_MAP['RESET']}")
            
            return True
            
        except Exception as e:
            print(f"가상환경 Python 패키지 설치 중 오류: {e}")
            return False
    
    def test_venv_python(self) -> bool:
        """가상환경 Python 테스트 (Linux)"""
        print("\n Step 22: 가상환경 Python 테스트 (Linux)")
        
        if not self.f_venv_python_linux.exists():
            print(f" 가상환경 Python을 찾을 수 없습니다: {self.f_venv_python_linux}")
            return False
        
        try:
            # Python 버전 확인
            result = subprocess.run([str(self.f_venv_python_linux), "--version"], 
                                  capture_output=True, text=True, check=True)
            print(f" 가상환경 Python 버전: {result.stdout.strip()}")
            
            # toml 모듈 테스트
            result = subprocess.run([str(self.f_venv_python_linux), "-c", "import toml; print('toml 모듈 사용 가능')"], 
                                  capture_output=True, text=True, check=True)
            print(f" {result.stdout.strip()}")
            
            return True
        except subprocess.CalledProcessError as e:
            print(f" 가상환경 Python 테스트 실패: {e}")
            return False
        except Exception as e:
            print(f" 테스트 중 오류: {e}")
            return False 