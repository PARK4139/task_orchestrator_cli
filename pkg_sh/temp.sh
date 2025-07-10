# power 
curl -sL https://raw.githubusercontent.com/aiktb/dotzsh/master/zsh.sh | bash && zsh
41211n1y


# oh-my-zsh
git clone https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc


# oh-my-zsh의 custom plugins 경로
ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"
git clone https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting"
git clone https://github.com/zsh-users/zsh-history-substring-search "$ZSH_CUSTOM/plugins/zsh-history-substring-search"
git clone https://github.com/MichaelAquilina/zsh-you-should-use.git "$ZSH_CUSTOM/plugins/you-should-use"


# 테마 설치
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "$ZSH_CUSTOM/themes/powerlevel10k"



# 테마 플러그인 적용
sudo vi ~/.zshrc
# --------------------------------------------------
# Oh-My-Zsh 기본 설정
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"     

plugins=(
  autojump # j -s   # j touch 
  zsh-autosuggestions  # ctrl + right arrow
  zsh-syntax-highlighting
  zsh-history-substring-search
  git
  z
  extract
  thefuck
  jsontools
  colored-man-pages
  you-should-use
  nvm
  debian
  tmux
)

source $ZSH/oh-my-zsh.sh

# syntax-highlighting 플러그인은 반드시 마지막에!
source ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

# --------------------------------------------------


source ~/.zshrc 




# 필요시 기본쉘 변경 물어보기
if [ "$SHELL" != "/usr/bin/zsh" ]; then
    read -p "zsh를 기본쉘로 변경할까요? [y/N]: " yn
    if [[ "$yn" =~ ^[Yy]$ ]]; then
        chsh -s $(which zsh)
        echo -e "${GREEN}기본쉘이 zsh로 변경되었습니다.${NC}"
    else
        echo -e "${YELLOW}기본쉘 변경은 건너뜁니다.${NC}"
    fi
fi











# ZSH_CUSTOM
다른 사용자 정의 디렉토리 사용
$ZSH_CUSTOM.zshrc

~/.zshrc
ZSH_CUSTOM=$HOME/Downloads/pk_zsh_customizations

$HOME
└── pk_zsh_customizations
    ├── my_lib_patches.zsh
    ├── plugins
    │   └── my_plugin
    │       └── my_plugin.plugin.zsh
    └── themes
        └── my_awesome_theme.zsh-theme