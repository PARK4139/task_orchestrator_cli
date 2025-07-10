# ping -c 2 8.8.8.8 



cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_set_as_124.sh

sudo rm -rf ~/Workspace/jetson*


# 3 lines unannotated at 5/26
git clone http://mkrmkrmkrmkr:8003/ai_dept/jetson-setup.git ~/Workspace

cd ~/Workspace/jetson-setup
sudo ./install.py
