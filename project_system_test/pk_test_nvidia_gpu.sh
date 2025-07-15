# gpu-burn은 GPU의 안정성과 발열, 성능을 테스트하기 위한 스트레스 테스트 도구입니다. 
# 주로 NVIDIA GPU를 대상으로 하고 CUDA를 이용해 GPU에 고부하를 걸어 테스트합니다.
# nvidia GPU 

# installation necessary packages
sudo apt update
sudo apt install git build-essential

# installation 
git clone https://github.com/wilicc/gpu-burn.git

# make
cd gpu-burn
make

# execution
# ./gpu_burn <SECONDS>
./gpu_burn 60
