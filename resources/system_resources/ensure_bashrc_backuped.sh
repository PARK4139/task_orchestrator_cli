mkdir -p $D_TASK_ORCHESTRATOR_CLI_DATA
filename=.bashrc
f_backup=$D_TASK_ORCHESTRATOR_CLI_DATA/$filename.bak.$(date +%Y%m%d_%H%M%S)
cp ~/$filename $f_backup
echo $f_backup
f_backup=$D_TASK_ORCHESTRATOR_CLI_DATA/$filename.bak
cp ~/$filename $f_backup
echo $f_backup
