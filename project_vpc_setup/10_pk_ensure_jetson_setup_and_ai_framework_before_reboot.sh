# ping -c 2 8.8.8.8 

cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_set_as_124.sh
# 2 5/26
sudo rm -rf ./jetson-setup*
sudo rm -rf ./ai_framework*



sudo rm -rf ~/Workspace
mkdir ~/Workspace


# 3 5/26
cd ~/Workspace
git clone http://mkrmkrmkrmkr:8003/ai_dept/jetson-setup.git 
cd ~/Workspace/jetson-setup
git checkout 2.2.1
cd ~/Workspace
tar -jcvf ./jetson-setup_x_x_x.tar.bz2 ./jetson-setup
wget http://mkrmkrmkrmkr:mkr/ai_framework_2_3_0_0_NO_KR.zip

# cp ./jetson-setup_x_x_x.tar.bz2 ~/Workspace
# cp ./ai_framework_2_3_0_0_NO_KR.zip ~/Workspace


cd ~/Workspace
tar -jxvf ~/Workspace/jetson-setup_x_x_x.tar.bz2
unzip ~/Workspace/ai_framework_2_3_0_0_NO_KR.zip 



# sudo rm -rf "$(dirname "$(realpath "$0")")/jetson-setup"
cd "$(dirname "$(realpath "$0")")"
sudo rm -rf ./jetson-setup




cd ~/Workspace/jetson-setup
sudo ./install.py