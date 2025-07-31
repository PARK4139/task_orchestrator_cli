#!/usr/bin/env python3
"""
PK System Enable Script (Python Version)
Linux/WSL 환경에서 PK 시스템을 활성화하는 스크립트
"""

import os
import sys
import subprocess
import shutil
import platform
import json
import tarfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Linux/WSL Constants
UV_URL_LINUX = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz"
FZF_API_URL = "https://api.github.com/repos/junegunn/fzf/releases/latest"
USER_HOME = Path.home()
D_PK_SYSTEM = USER_HOME / "Downloads" / "pk_system"
D_BUSINESS_DEMO = USER_HOME / "Downloads" / "business_demo"
D_PKG_LINUX = D_PK_SYSTEM / "pkg_linux"
D_VENV_BIN = D_PK_SYSTEM / ".venv" / "bin"
F_UV_BINARY = D_PKG_LINUX / "uv"
F_FZF_BINARY = D_PKG_LINUX / "fzf"
F_VENV_PYTHON = D_VENV_BIN / "python"
F_UV_TAR = USER_HOME / "Downloads" / "uv.tar.gz"
F_FZF_TAR = USER_HOME / "Downloads" / "fzf.tar.gz"


class PKSystemEnabler:
    def __init__(self):
        self.script_dir = Path(__file__).resolve().parent
        self.project_root = self.script_dir
        self.user_home = Path.home()
        self.pkg_sh_dir = self.script_dir / "pkg_sh"
        
        print("🐍 PK System Enabler (Python)")
        print("=" * 50)
        print(f"📁 Script directory: {self.script_dir}")
        print(f"📁 Project root: {self.project_root}")
        print(f"🏠 User home: {self.user_home}")
        print(f"🖥️ OS: {platform.system()} {platform.release()}")
    
    def run_command(self, command: List[str], cwd: Optional[Path] = None, 
                   capture_output: bool = True, check: bool = True) -> subprocess.CompletedProcess:
        """명령어를 실행하는 헬퍼 함수"""
        try:
            result = subprocess.run(
                command,
                cwd=cwd,
                capture_output=capture_output,
                text=True,
                check=check
            )
            return result
        except subprocess.CalledProcessError as e:
            print(f"❌ 명령어 실행 실패: {' '.join(command)}")
            print(f"   오류: {e.stderr}")
            if check:
                raise
            return e
    
    def detect_os(self) -> str:
        """OS 감지"""
        system = platform.system().lower()
        if "linux" in system:
            return "linux"
        elif "windows" in system:
            return "windows"
        elif "darwin" in system:
            return "macos"
        else:
            return "unknown"
    
    def step_00_ensure_os_variables(self):
        """Step 00: OS 변수 설정"""
        print("\n🔧 Step 00: OS 변수 설정")
        
        # UTF-8 환경 변수 설정
        os.environ['LANG'] = 'en_US.UTF-8'
        print("✅ UTF-8 환경 변수 설정 완료")
        
        # 시스템 업데이트는 건너뛰기 (사용자 상호작용 문제 방지)
        print("ℹ️ 시스템 업데이트는 건너뜁니다 (필요시 수동으로 실행)")
    
    def step_10_install_uv(self):
        """Step 10: uv 설치"""
        print("\n📦 Step 10: uv 설치")
        
        # uv가 이미 설치되어 있는지 확인
        try:
            result = self.run_command(["uv", "--version"], check=False)
            if result.returncode == 0:
                print(f"✅ uv가 이미 설치되어 있습니다: {result.stdout.strip()}")
                return
        except FileNotFoundError:
            pass
        
        # Linux/WSL 환경에서만 uv 설치
        if self.detect_os() == "linux":
            print("🔧 uv 설치 중...")
            
            # uv가 이미 설치되어 있으면 건너뛰기
            try:
                result = self.run_command(["uv", "--version"], check=False)
                if result.returncode == 0:
                    print(f"✅ uv가 이미 설치되어 있습니다: {result.stdout.strip()}")
                    return
            except FileNotFoundError:
                pass
            
            print("⚠️ uv 설치를 건너뜁니다 (필요시 수동으로 설치)")
            print("💡 수동 설치: curl -LsSf https://astral.sh/uv/install.sh | sh")
        else:
            print("ℹ️ Windows/macOS 환경이므로 uv 설치를 건너뜁니다")
            print("💡 Windows에서는 다음 명령어로 uv를 설치하세요:")
            print("   pip install uv")
    
    def step_20_sync_uv_packages(self):
        """Step 20: uv 패키지 동기화"""
        print("\n🔄 Step 20: uv 패키지 동기화")
        
        # uv가 설치되어 있는지 확인
        try:
            result = self.run_command(["uv", "--version"], check=False)
            if result.returncode != 0:
                print("❌ uv가 설치되지 않았습니다")
                return
        except FileNotFoundError:
            print("❌ uv가 설치되지 않았습니다")
            return
        
        # 프로젝트 루트로 이동
        os.chdir(self.project_root)
        
        # uv sync 실행 (오류가 있어도 계속 진행)
        print("📦 uv sync 실행 중...")
        try:
            self.run_command(["uv", "sync"], check=False)
            print("✅ uv sync 완료")
        except Exception as e:
            print(f"⚠️ uv sync 중 일부 패키지 빌드 실패: {e}")
            print("💡 일부 패키지는 나중에 수동으로 설치할 수 있습니다")
            print("   계속 진행합니다...")
    
    def step_30_install_dependencies(self):
        """Step 30: 종속성 설치"""
        print("\n📚 Step 30: 종속성 설치")
        
        # Linux/WSL 환경에서만 종속성 설치
        if self.detect_os() == "linux":
            dependencies = [
                "pkg-config",           # pk database 종속성
                "default-libmysqlclient-dev",  # pk database 종속성
                "build-essential",      # pk database 종속성
                "portaudio19-dev",      # pk 종속성
                "python3-dev",         # Python 개발 헤더 (pyaudio 빌드용)
            ]
            
            for dep in dependencies:
                print(f"📦 {dep} 설치 중...")
                self.run_command(["sudo", "apt", "install", "-y", dep], check=False)
                print(f"✅ {dep} 설치 완료")
        else:
            print("ℹ️ Windows/macOS 환경이므로 시스템 종속성 설치를 건너뜁니다")
    
    def step_40_setup_python_venv(self):
        """Step 40: Python 가상환경 설정"""
        print("\n🐍 Step 40: Python 가상환경 설정")
        
        venv_path = self.project_root / ".venv"
        
        if venv_path.exists():
            print(f"✅ 가상환경 발견: {venv_path}")
            
            # Python 경로 설정
            venv_python = venv_path / "bin" / "python"
            venv_pip = venv_path / "bin" / "pip"
            
            if venv_python.exists():
                print("🔗 Python 가상환경 심볼릭 링크 생성 중...")
                
                # Linux 환경에서만 심볼릭 링크 생성
                if self.detect_os() == "linux":
                    # 기존 심볼릭 링크 제거
                    python_venv_link = Path("/usr/local/bin/python-venv")
                    pip_venv_link = Path("/usr/local/bin/pip-venv")
                    
                    if python_venv_link.exists():
                        self.run_command(["sudo", "rm", "-f", str(python_venv_link)])
                    
                    if pip_venv_link.exists():
                        self.run_command(["sudo", "rm", "-f", str(pip_venv_link)])
                    
                    # 새로운 심볼릭 링크 생성
                    self.run_command(["sudo", "ln", "-sf", str(venv_python), str(python_venv_link)])
                    self.run_command(["sudo", "ln", "-sf", str(venv_pip), str(pip_venv_link)])
                    
                    print("✅ Python 가상환경 심볼릭 링크 생성 완료:")
                    print(f"  - python-venv -> {venv_python}")
                    print(f"  - pip-venv -> {venv_pip}")
                
                # 환경 변수 설정을 .bashrc에 추가 (Linux만)
                if self.detect_os() == "linux":
                    bashrc_path = self.user_home / ".bashrc"
                    python_setup_marker = "# Python virtual environment setup"
                    
                    if not bashrc_path.exists() or python_setup_marker not in bashrc_path.read_text():
                        with open(bashrc_path, "a") as f:
                            f.write(f"\n{python_setup_marker}\n")
                            f.write(f'export VENV_PYTHON="{venv_python}"\n')
                            f.write(f'export VENV_PIP="{venv_pip}"\n')
                            f.write(f'alias python-venv="{venv_python}"\n')
                            f.write(f'alias pip-venv="{venv_pip}"\n')
                
                # 현재 세션에서도 환경 변수 설정
                os.environ['VENV_PYTHON'] = str(venv_python)
                os.environ['VENV_PIP'] = str(venv_pip)
                
                print("✅ Python 가상환경 별칭 설정 완료")
                print("  - 'python-venv' 명령어로 가상환경 Python 실행")
                print("  - 'pip-venv' 명령어로 가상환경 pip 실행")
                
                # Python 버전 확인
                version_result = self.run_command([str(venv_python), "--version"])
                print(f"📋 가상환경 Python 버전: {version_result.stdout.strip()}")
                
            else:
                print(f"❌ 가상환경에서 Python 실행 파일을 찾을 수 없습니다: {venv_python}")
        else:
            print(f"❌ 가상환경을 찾을 수 없습니다: {venv_path}")
            print("💡 가상환경을 생성하려면 다음 명령어를 실행하세요:")
            print(f"   cd {self.project_root} && python -m venv .venv")
    
    def step_50_clear_profile_settings(self):
        """Step 50: 기존 프로필 설정 정리"""
        print("\n🧹 Step 50: 기존 프로필 설정 정리")
        
        # Linux 환경에서만 .bashrc 정리
        if self.detect_os() == "linux":
            bashrc_path = self.user_home / ".bashrc"
            if bashrc_path.exists():
                # .bash_aliases 소스 라인 제거
                content = bashrc_path.read_text()
                lines = content.split('\n')
                filtered_lines = [line for line in lines if 'source ~/.bash_aliases' not in line]
                
                if len(filtered_lines) != len(lines):
                    bashrc_path.write_text('\n'.join(filtered_lines))
                    print("✅ 기존 .bash_aliases 소스 라인 제거 완료")
                else:
                    print("ℹ️ 제거할 .bash_aliases 소스 라인이 없습니다")
        else:
            print("ℹ️ Windows/macOS 환경이므로 프로필 설정 정리를 건너뜁니다")
    
    def step_60_register_pk_alias(self):
        """Step 60: pk_alias를 Bash/Zsh 프로필에 등록"""
        print("\n📝 Step 60: pk_alias를 Bash/Zsh 프로필에 등록")

        if self.detect_os() == "linux":
            pk_alias_script = self.pkg_sh_dir / "pk_alias.sh"

            env_vars = {
                "D_PK_PROJECT": str(self.project_root),
                "D_PK_WORKING": str(self.project_root.parent / "pk_working"),
                "D_PKG_SH": str(self.pkg_sh_dir),
                "D_PKG_BASHRC": str(self.project_root / "pkg_bashrc"),
                "D_PKG_ZSHRC": str(self.project_root / "pkg_zshrc"),
                "D_PKG_EXE": str(self.project_root / "pkg_exe"),
                "F_UV_ZIP": str(self.user_home / "Downloads/uv.zip"),
                "F_UV_EXE": str(self.project_root / "pkg_exe/uv.exe"),
            }

            aliases = {
                "cls": "clear",
                "x": "exit",
                "0": "cd $D_PKG_SH",
                "1": "cd $D_PK_PROJECT",
                "2": "cd $D_PK_WORKING",
                "3": "cd $D_BUSINESS_DEMO",
                "4": "cd ~/Downloads",
                "5": "cd ~/Documents",
                "6": "cd ~/Desktop",
                "~": "cd ~",
                ".": "explorer.exe .",
                "pk": "echo '🐍 PK System Information' && echo '================' && echo '📁 Root: $D_PK_PROJECT' && echo '🐍 Python: $(which python3)' && echo '📦 uv: $(which uv 2>/dev/null || echo \"Not installed\")' && echo '================'",
                "pk-info": "echo '🐍 PK System Information' && echo '================' && echo '📁 Root: $D_PK_PROJECT' && echo '🐍 Python: $(which python3)' && echo '📦 uv: $(which uv 2>/dev/null || echo \"Not installed\")' && echo '================'",
                "pk-enable": "echo '🔧 PK System 활성화 중...' && cd \"$D_PK_PROJECT\" && ./pkg_sh/ensure_pk_system_enabled.sh",
                "pk-sync": "echo '🔄 PK System 동기화 중...' && cd \"$D_PK_PROJECT\" && uv sync",
                "pk-test": "echo '🧪 PK System 테스트 중...' && cd \"$D_PK_PROJECT\" && if [ -f 'tests/run_tests.py' ]; then python-venv tests/run_tests.py; else echo '❌ 테스트 파일을 찾을 수 없습니다.'; fi",
            }

            config_files = [
                (self.user_home / ".bashrc", "bash"),
                (self.user_home / ".zshrc", "zsh")
            ]

            for config_file, shell_type in config_files:
                if config_file.exists():
                    content = config_file.read_text()
                    env_section = f"\n# PK System Environment Variables ({shell_type})\n"
                    for var_name, var_value in env_vars.items():
                        env_section += f'export {var_name}="{var_value}"\n'
                    alias_section = f"\n# PK System Aliases ({shell_type})\n"
                    for alias_name, alias_command in aliases.items():
                        alias_section += f'alias {alias_name}="{alias_command}"\n'
                    pk_alias_source = f"\n# PK System Alias Script ({shell_type})\nsource {pk_alias_script}\n"

                    lines = content.split('\n')
                    filtered_lines = []
                    for line in lines:
                        if any(marker in line for marker in [
                            "# PK System Environment Variables", "# PK System Aliases", "# PK System Alias Script",
                            "export D_PK_", "export D_PKG_", "export F_UV_",
                            "alias cls=", "alias x=", "alias 0=", "alias 1=", "alias 2=", "alias 3=", "alias 4=", "alias 5=", "alias 6=", "alias ~=", "alias .=", "alias pk", "alias pk-",
                            f"source {pk_alias_script}"
                        ]):
                            continue
                        filtered_lines.append(line)

                    new_content = '\n'.join(filtered_lines) + env_section + alias_section + pk_alias_source
                    config_file.write_text(new_content)
                    print(f"✅ {shell_type} 설정 완료: {config_file}")
                else:
                    print(f"⚠️ {shell_type} 설정 파일을 찾을 수 없습니다: {config_file}")

            print("✅ PK System 환경 변수 및 alias 설정 완료:")
            print(f"  - 환경 변수: {len(env_vars)}개")
            print(f"  - alias: {len(aliases)}개")
            print(f"  - pk_alias.sh: {pk_alias_script}")

            for var_name, var_value in env_vars.items():
                os.environ[var_name] = var_value
        else:
            print("ℹ️ Windows/macOS 환경이므로 pk_alias 등록을 건너뜁니다")
    
    def install_uv_linux(self, max_retry: int = 2) -> None:
        """UV 다운로드 및 설치 (Linux/WSL)"""
        print("\n📦 Step 11: UV 설치 (Linux/WSL)")
        
        # UV가 이미 설치되어 있는지 확인
        try:
            result = self.run_command(["uv", "--version"], check=False)
            if result.returncode == 0:
                print(f"✅ uv가 이미 설치되어 있습니다: {result.stdout.strip()}")
                return
        except FileNotFoundError:
            pass
        
        # Linux/WSL 환경에서만 UV 설치
        if self.detect_os() == "linux":
            print("🔧 uv 설치 중...")
            
            # requests 모듈 설치 확인
            try:
                import requests
            except ImportError:
                print("📦 requests 모듈 설치 중...")
                self.run_command([sys.executable, "-m", "pip", "install", "requests"])
                import requests
            
            os.makedirs(D_PKG_LINUX, exist_ok=True)
            
            # 이미 UV가 설치되어 있는지 확인
            if F_UV_BINARY.exists():
                print(f"✅ uv가 이미 설치되어 있습니다: {F_UV_BINARY}")
                return
            
            for attempt in range(1, max_retry + 1):
                try:
                    print(f"[Attempt {attempt}] Downloading uv from {UV_URL_LINUX}")
                    response = requests.get(UV_URL_LINUX, stream=True)
                    response.raise_for_status()
                    
                    with open(F_UV_TAR, "wb") as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)

                    # Extract tar.gz
                    print("Extracting uv.tar.gz...")
                    with tarfile.open(F_UV_TAR, 'r:gz') as tar_ref:
                        tar_ref.extractall(D_PKG_LINUX)

                    # Find uv binary
                    found_uv = None
                    for root, _, files in os.walk(D_PKG_LINUX):
                        for name in files:
                            if name == "uv":
                                found_uv = Path(root) / name
                                break
                        if found_uv:
                            break

                    if not found_uv:
                        raise FileNotFoundError("uv binary not found in extracted tar.gz.")

                    # 대상 파일이 이미 존재하면 삭제
                    if F_UV_BINARY.exists():
                        F_UV_BINARY.unlink()

                    # 파일 복사 (더 안전한 방법 사용)
                    try:
                        shutil.copy2(found_uv, F_UV_BINARY)
                        os.chmod(F_UV_BINARY, 0o755)  # 실행 권한 부여
                        print(f"✅ uv 바이너리 복사 완료: {F_UV_BINARY}")
                    except Exception as copy_error:
                        print(f"파일 복사 중 오류: {copy_error}")
                        # 대안: 직접 복사
                        with open(found_uv, 'rb') as src, open(F_UV_BINARY, 'wb') as dst:
                            dst.write(src.read())
                        os.chmod(F_UV_BINARY, 0o755)
                        print(f"✅ uv 바이너리 직접 복사 완료: {F_UV_BINARY}")

                    # Validate execution
                    print("Validating uv binary execution...")
                    result = self.run_command([str(F_UV_BINARY), "--version"])
                    print(f"✅ uv 설치 완료: {result.stdout.strip()}")

                    break

                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt >= max_retry:
                        print("❌ uv 설치 실패")
                        raise RuntimeError("uv installation failed after multiple attempts.") from e
                    else:
                        print("Retrying...")

                finally:
                    try:
                        if F_UV_TAR.exists():
                            F_UV_TAR.unlink()
                    except Exception as e:
                        print(f"Failed to remove uv.tar.gz: {e}")
        else:
            print("ℹ️ Windows/macOS 환경이므로 Linux UV 설치를 건너뜁니다")
    
    def get_latest_fzf_url_linux(self) -> str:
        """GitHub API를 사용하여 최신 FZF 다운로드 URL 가져오기 (Linux)"""
        try:
            import requests
        except ImportError:
            print("📦 requests 모듈 설치 중...")
            self.run_command([sys.executable, "-m", "pip", "install", "requests"])
            import requests
        
        try:
            print("FZF 최신 버전 확인 중...")
            response = requests.get(FZF_API_URL)
            response.raise_for_status()
            data = response.json()
            version = data["tag_name"]
            print(f"FZF 최신 버전: {version}")
            
            # Remove 'v' prefix from version for filename
            version_clean = version.lstrip('v')
            
            # Linux AMD64 다운로드 URL 생성
            download_url = f"https://github.com/junegunn/fzf/releases/download/{version}/fzf-{version_clean}-linux_amd64.tar.gz"
            print(f"FZF 다운로드 URL: {download_url}")
            
            return download_url
            
        except Exception as e:
            # Fallback URL
            fallback_url = "https://github.com/junegunn/fzf/releases/download/v0.65.0/fzf-0.65.0-linux_amd64.tar.gz"
            print(f"Fallback URL 사용: {fallback_url}")
            
            try:
                # Fallback URL 테스트
                response = requests.head(fallback_url)
                if response.status_code == 200:
                    return fallback_url
            except:
                pass
            
            print(f"FZF 최신 버전 확인 실패: {e}")
            print(f"최종 Fallback URL 사용: {fallback_url}")
            return fallback_url

    def install_fzf_linux(self, max_retry: int = 2) -> None:
        """FZF 다운로드 및 설치 (Linux/WSL)"""
        print("\n🔍 Step 12: FZF 설치 (Linux/WSL)")
        
        # FZF가 이미 설치되어 있는지 확인
        try:
            result = self.run_command(["fzf", "--version"], check=False)
            if result.returncode == 0:
                print(f"✅ fzf가 이미 설치되어 있습니다: {result.stdout.strip()}")
                return
        except FileNotFoundError:
            pass
        
        # Linux/WSL 환경에서만 FZF 설치
        if self.detect_os() == "linux":
            print("🔧 fzf 설치 중...")
            
            # 이미 FZF가 설치되어 있는지 확인
            if F_FZF_BINARY.exists():
                print(f"✅ fzf가 이미 설치되어 있습니다: {F_FZF_BINARY}")
                return
            
            os.makedirs(D_PKG_LINUX, exist_ok=True)
            
            for attempt in range(1, max_retry + 1):
                try:
                    print(f"[Attempt {attempt}] Installing fzf using WSL bash...")
                    
                    # WSL bash를 사용하여 직접 설치
                    install_cmd = [
                        "wsl", "bash", "-c",
                        f"cd /tmp && curl -LsSf https://github.com/junegunn/fzf/releases/download/v0.65.0/fzf-0.65.0-linux_amd64.tar.gz | tar -xz && sudo cp fzf {D_PKG_LINUX}/ && sudo chmod +x {D_PKG_LINUX}/fzf"
                    ]
                    
                    result = subprocess.run(install_cmd, capture_output=True, text=True, check=True)
                    print("✅ fzf 설치 완료")

                    # Validate execution
                    print("Validating fzf binary execution...")
                    result = self.run_command([str(F_FZF_BINARY), "--version"])
                    print(f"✅ fzf 설치 완료: {result.stdout.strip()}")

                    break

                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt >= max_retry:
                        print("❌ fzf 설치 실패")
                        raise RuntimeError("fzf installation failed after multiple attempts.") from e
                    else:
                        print("Retrying...")
        else:
            print("ℹ️ Windows/macOS 환경이므로 Linux FZF 설치를 건너뜁니다")
    
    def setup_linux_path(self) -> None:
        """UV, FZF, 가상환경 Python 경로를 .bashrc/.zshrc에 추가"""
        print("\n🛤️ Step 13: Linux PATH 설정")
        
        print(f"UV 경로: {D_PKG_LINUX}")
        print(f"가상환경 bin 경로: {D_VENV_BIN}")
        print(f"Business Demo 경로: {D_BUSINESS_DEMO}")
        
        # Business Demo 디렉토리 생성
        if not D_BUSINESS_DEMO.exists():
            try:
                D_BUSINESS_DEMO.mkdir(parents=True, exist_ok=True)
                print(f"Business Demo 디렉토리 생성: {D_BUSINESS_DEMO}")
            except Exception as e:
                print(f"Business Demo 디렉토리 생성 실패: {e}")
        
        # .bashrc와 .zshrc 모두 설정
        config_files = [
            (USER_HOME / ".bashrc", "bash"),
            (USER_HOME / ".zshrc", "zsh")
        ]
        
        for config_file, shell_type in config_files:
            if config_file.exists():
                content = config_file.read_text()
                
                # 기존 PK System PATH 설정 제거
                lines = content.split('\n')
                filtered_lines = []
                for line in lines:
                    if not any(marker in line for marker in [
                        "# PK System PATH",
                        "export PATH=",
                        "export D_BUSINESS_DEMO="
                    ]):
                        filtered_lines.append(line)
                
                # 새로운 PATH 설정 추가
                path_section = f"\n# PK System PATH ({shell_type})\n"
                path_section += f'export PATH="$PATH:{D_PKG_LINUX}:{D_VENV_BIN}"\n'
                path_section += f'export D_BUSINESS_DEMO="{D_BUSINESS_DEMO}"\n'
                
                new_content = '\n'.join(filtered_lines) + path_section
                
                config_file.write_text(new_content)
                
                print(f"✅ {shell_type} PATH 설정 완료: {config_file}")
            else:
                print(f"⚠️ {shell_type} 설정 파일을 찾을 수 없습니다: {config_file}")
        
        print("✅ Linux PATH 설정 완료")
    
    def run_all_steps(self):
        """모든 단계 실행"""
        try:
            self.step_00_ensure_os_variables()
            self.step_10_install_uv()
            
            # Linux/WSL 환경에서 추가 UV/FZF 설치 (Linux용)
            if self.detect_os() == "linux":
                self.install_uv_linux()
                self.install_fzf_linux()
                self.setup_linux_path()
            
            self.step_20_sync_uv_packages()
            self.step_30_install_dependencies()
            self.step_40_setup_python_venv()
            self.step_50_clear_profile_settings()
            self.step_60_register_pk_alias()
            
            print("\n" + "=" * 50)
            print("✅ 모든 단계가 성공적으로 완료되었습니다!")
            
            if self.detect_os() == "linux":
                print("\n🔄 변경사항을 적용하려면 새 터미널을 열거나 다음 명령어를 실행하세요:")
                print("   source ~/.bashrc")
            
        except Exception as e:
            print(f"\n❌ 오류 발생: {e}")
            sys.exit(1)


def main():
    """메인 함수"""
    enabler = PKSystemEnabler()
    enabler.run_all_steps()


if __name__ == "__main__":
    main() 