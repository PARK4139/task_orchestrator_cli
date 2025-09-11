
sudo apt update
sudo apt install -y pkg-config
sudo apt install -y default-libmysqlclient-dev
sudo apt install -y libmysqlclient-dev
sudo apt install -y build-essential
sudo apt install -y python3-dev


sudo apt install -y portaudio19-dev

cd $D_TASK_ORCHESTRATOR_CLI
./
uv sync
# uv pip install .
