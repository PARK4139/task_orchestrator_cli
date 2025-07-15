#! /bin/bash

#! /bin/bash
# install_prerequisite
sudo apt-get install -y python3-pip tmux stress
sudo pip3 install -U jetson-stats



echo "Please logout/in again or reboot NX to get jtop result."
reboot



## Set xavier to MAXN mode before a test
# sudo nvpmodel -m 0
# sudo nvpmodel -q

# Session creation
session="stress-test"
tmux new-session -d -s $session

# Window creation
# window 0 for jtop
window=0
tmux rename-window -t $session:$window 'jtop/gpu/cpu'
tmux send-keys -t $session:$window "jtop" C-m

# window 0 / adding vertical pane
tmux split-window -h -t $session:$window
tmux send-keys -t $session:$window './stress_logger 60' C-m

# window 0 / adding vertical pane
tmux split-window -v -t $session:$window
tmux send-keys -t $session:$window 'cd ./gpu-burn && ./gpu_burn 100000' C-m

# window 0 / adding horizontal pane
tmux split-window -v -t $session:$window
tmux send-keys -t $session:$window 'stress --cpu 12' C-m

tmux attach-session -t $session
