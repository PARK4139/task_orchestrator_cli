mkdir -p "$D_PKG_ZSHRC"
f_backup=$D_PKG_ZSHRC/.zshrc.bak.$(date +%Y%m%d_%H%M%S)
cp ~/.zshrc $f_backup
f_backup=$D_PKG_ZSHRC/.zshrc.bak
cp ~/.zshrc $f_backup
echo $f_backup