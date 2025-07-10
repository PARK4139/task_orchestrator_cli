cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_reset.sh

cd ~/Workspace/jetson-setup
sudo ./install.py -n 
