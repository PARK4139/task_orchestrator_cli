#!/bin/bash
set -e  # 에러 발생 시 즉시 종료

# UTF-8 설정
export LANG=en_US.UTF-8

# 필요시 주석
sudo apt update

# 현재 스크립트 위치(절대경로)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
USER_HOME="$HOME"

echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
CURRENT_STEP="Step 00: ensure OS variable"
echo -e "\e[36m[1/6] $CURRENT_STEP\e[0m"
chmod +x "$SCRIPT_DIR/ensure_pk_os_constants_imported.sh"
sudo "$SCRIPT_DIR/ensure_pk_os_constants_imported.sh" "$USER_HOME"

# echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
# CURRENT_STEP="Step 10: Import pk_alias"
# echo -e "\e[36m[2/6] $CURRENT_STEP\e[0m"
# chmod +x "$SCRIPT_DIR/ensure_pk_alias_imported.sh"
# if ! "$SCRIPT_DIR/ensure_pk_alias_imported.sh"; then
#   echo "Failed at $CURRENT_STEP"
#   exit 1
# fi

# echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
# Step 20: Import ahk (AutoHotkey)
# CURRENT_STEP="Importing ahk"
# echo -e "\e[36m[3/6] $CURRENT_STEP (SKIP: Not applicable in Linux/WSL)\e[0m"

echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
# Step 30: Installing uv
CURRENT_STEP="Installing uv"
echo -e "\e[36m[4/6] $CURRENT_STEP\e[0m"
chmod +x "$SCRIPT_DIR/ensure_uv_installed.sh"
"$SCRIPT_DIR/ensure_uv_installed.sh" || exit 1

echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
# Step 40: Syncing uv
CURRENT_STEP="Syncing uv packages"
echo -e "\e[36m[5/6] $CURRENT_STEP\e[0m"
UV_PATH="$USER_HOME/Downloads/pk_system/pkg_windows"
export PATH="$PATH:$UV_PATH"
chmod +x "$SCRIPT_DIR/ensure_uv_synced.sh"
"$SCRIPT_DIR/ensure_uv_synced.sh" || exit 1

echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
# pk venv 종속성
sudo apt install -y pkg-config # pk database 종속성
sudo apt install -y default-libmysqlclient-dev # pk database 종속성
sudo apt install -y build-essential # pk database 종속성
sudo apt install -y portaudio19-dev # pk 종속성

echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
# Step 50: Clear existing shell profile settings (Bash equivalent of AutoRun)
CURRENT_STEP="Clearing existing profile settings"
echo -e "\e[33m[6/6] $CURRENT_STEP (Applicable in Linux/WSL)\e[0m"
sed -i '/source ~\/.bash_aliases/d' "$USER_HOME/.bashrc"

echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
# Step 60: Register pk_alias to Bash Profile (AutoRun alternative)
CURRENT_STEP="Registering pk_alias to Bash Profile"
echo -e "\e[36m[7/6] $CURRENT_STEP (Applicable in Linux/WSL)\e[0m"
if ! grep -Fxq "source $SCRIPT_DIR/pk_alias.sh" "$USER_HOME/.bashrc"; then
  echo "source $SCRIPT_DIR/pk_alias.sh" >> "$USER_HOME/.bashrc"
fi
# source "$USER_HOME/.bashrc" # 주의: 현재 쉘에서만 적용, 새 터미널 필요

echo -e "\e[36m──────────────────────────────────────────────────────────\e[0m"
CURRENT_STEP="All steps completed successfully"
echo -e "\e[32m✅ $CURRENT_STEP\e[0m"

exit 0
