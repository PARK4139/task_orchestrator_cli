mkdir -p $D_PKG_BASHRC
f_backup=$D_PKG_BASHRC/.bashrc.bak.$(date +%Y%m%d_%H%M%S)
cp ~/.bashrc $f_backup
f_backup=$D_PKG_BASHRC/.bashrc.bak
cp ~/.bashrc $f_backup
echo $f_backup