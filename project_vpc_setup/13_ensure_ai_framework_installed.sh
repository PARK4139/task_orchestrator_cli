# 1 
cd "$(dirname "$(realpath "$0")")"
sudo ./pk_ensure_wired_connection_1_set_as_124.sh

# 2 
sudo rm -rf ./ai_framework*

# 3
cd ~/Workspace
sudo rm -rf ./ai_framework
wget http://mkrmkrmkrmkr:mkr/ai_framework_x.x.x.x_NO_KR.zip

# cp ./ai_framework_x.x.x.x_NO_KR.zip ~/Workspace


# 4
cd ~/Workspace
unzip ~/Workspace/ai_framework_x.x.x.x_NO_KR.zip 

