#!/bin/bash

set -e # 에러발생시 bash 종료하도록 설정

# get environment variables (해당쉘세션)
ENV_FILE="/etc/default/setup_env"
if [ -f "$ENV_FILE" ]; then
    set -o allexport
    source "$ENV_FILE"
    set +o allexport
fi


# Use environment variables or fallback defaults
WORKSPACE_PATH="${WORKSPACE_PATH:-/home/nvidia/Workspace/}"
AIFW_PATH="${AIFW_PATH:-/home/nvidia/Workspace/ai_framework/}"
SETUP_PATH="${SETUP_PATH:-/home/nvidia/Workspace/jetson-setup/}"

OS_NAME=$(grep '^NAME=' /etc/os-release | cut -d= -f2 | tr -d '"')
OS_VERSION=$(grep '^VERSION=' /etc/os-release | cut -d= -f2 | tr -d '"')
KERNEL_VERSION=$(uname -r)
PYTHON_VERSION=$(python3 --version 2>/dev/null | awk '{print $2}')
GCC_VERSION=$(gcc --version 2>/dev/null | head -n1 | awk '{print $3}')
GIT_VERSION=$(git --version | awk '{print $3}')
AI_FRAMEWORK_GIT_TAG_VERSION=$(git -C "$AIFW_PATH" describe --tags --always 2>/dev/null || echo "unknown") # local git repo versions
JETSON_SETUP_GIT_VERSION=$(git -C "$SETUP_PATH" describe --tags --always 2>/dev/null || echo "unknown") # local git repo versions
MODULE_TYPE=$(command -v module-type >/dev/null 2>&1 && module-type || echo "unknown")
VPC_ID=$(python3 -c '
import os
target_file = "/etc/nv_boot_control.conf"
result = "Error"
if os.path.exists(target_file):
    with open(target_file) as f:
        for line in f:
            parts = line.strip().split(" ")
            if len(parts) >= 2 and parts[0] == "TNSPEC":
                if "xavier" in parts[1]:
                    result = "NX"
                elif "acuno" in parts[1]:
                    result = "NO"
print(result)
')
versions=($(find "$WORKSPACE_PATH" -maxdepth 1 -type f -iname 'ai_framework_[0-9]*.[0-9]*.[0-9]*.[0-9]*_*.zip' \
    ! -iname '*_unpacked.zip' | \
    sed -n 's/.*ai_framework_\([0-9.]*\)_.*\.zip/\1/p' | sort | uniq))

if [ ${#versions[@]} -eq 1 ]; then
    AIFW_RELEASE_ZIP_FILE_VERSION="${versions[0]}"
else
    AIFW_RELEASE_ZIP_FILE_VERSION="unknown"
fi



# Print vpc info as JSON
cat <<EOF
{
  "vpc_id": "$VPC_ID",
  "module_type": "$MODULE_TYPE",
  "os": {
    "name": "$OS_NAME",
    "version": "$OS_VERSION"
  },
  "kernel": "$KERNEL_VERSION",
  "python": "$PYTHON_VERSION",
  "gcc": "$GCC_VERSION",
  "git": "$GIT_VERSION",
  "system_softwares": {
    "ai_framework_git_tag_version": "$AI_FRAMEWORK_GIT_TAG_VERSION",
    "ai_framework_release_zip_file_version": "$AIFW_RELEASE_ZIP_FILE_VERSION",
    "jetson-setup": "$JETSON_SETUP_GIT_VERSION"
  }
}
EOF