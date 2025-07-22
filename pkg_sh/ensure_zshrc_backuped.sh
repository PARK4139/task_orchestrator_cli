mkdir -p $D_PKG_IDE_BACKUP
filename=.zshrc
f_backup=$D_PKG_IDE_BACKUP/$filename.bak.$(date +%Y%m%d_%H%M%S)
cp ~/$filename $f_backup
echo $f_backup
f_backup=$D_PKG_IDE_BACKUP/$filename.bak
cp ~/$filename $f_backup
echo $f_backup