# "Jetson-stress 온도테스트기능 활성화 스크립트"
# 해당 스크립트는 jetson-setup의 sudo ./install.py 선수행에 의존함
# cd ~/Workspace/jetson-setup
# git submodule init 
# git submodule update

# cd ~/Workspace/jetson-setup/extern/jetson_stress/gpu-burn
# make
# cd ~/Workspace/jetson-setup/extern
# cp -r jetson_stress ~/



# 2,2,1 이상의 버전 적용.
cd ~/Workspace/jetson-setup
git submodule init 
git submodule update
./install.py
cd ~/Workspace/jetson-setup/extern/jetson_stress/gpu-burn
make
cd ~/Workspace/jetson-setup/extern




# migration to python (TBD)
# python3 50_ensure_jetson_stress_activate.py
