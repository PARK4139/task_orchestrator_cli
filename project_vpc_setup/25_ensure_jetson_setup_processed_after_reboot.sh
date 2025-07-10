cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_set_as_124.sh


cd ~/Workspace/jetson-setup
sudo ./install.py


cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_set_as_124.sh
sleep 1s

cd ~/Workspace/jetson-setup
sudo pip install -e .
