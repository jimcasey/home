#!/bin/bash

echo_action() {
  echo
  echo -e "${bright}${1}${normal}"
}

append() {
  if ! grep -qs "\"$1\"" "$2"; then
    echo "$1" >> "$2"
  fi
}

bright="\033[1;36m"
normal="\033[0m"

script_dir="$(cd "$(dirname ${BASH_SOURCE[0]-$0})" && pwd)"

echo_action "Configuring Zsh..."
ohmyzsh_path=~/.oh-my-zsh
if [[ ! -d $ohmyzsh_path ]]; then
  echo_action "Installing Oh My Zsh..."
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
fi

zshrc_local=~/.zshrc
zshrc_command="source ${script_dir}/.zshrc"

if ! grep -qs "$zshrc_command" $zshrc_local; then
  echo_action "Configuring ${zshrc_local}..."
  touch $zshrc_local
  append $zshrc_local $zshrc_command
fi

zshrc_backup=~/.zshrc.pre-oh-my-zsh
if [[ -f $zshrc_backup ]]; then
  echo_action "Restoring ${zshrc_local}..."
  rm $zshrc_local
  mv $zshrc_backup $zshrc_local
fi

echo_action "Configuring git..."
git config --global core.editor "vi"
git config --global core.pager "cat"
git config --global pager.branch "false"
git config --global pager.diff "false"
git config --global log.diff "false"

echo_action "Configuring vim..."
if [[ ! -d ~/.vim/pack/themes/start/vim-code-dark ]]; then
  mkdir -p ~/.vim/pack/themes/start
  cd ~/.vim/pack/themes/start
  git clone https://github.com/tomasiser/vim-code-dark
fi

touch ~/.vimrc
append "syntax enable" ~/.vimrc
append "colorscheme codedark" ~/.vimrc

echo_action "Configuring bat..."
if [[ ! -d ~/.config/bat ]]; then
  mkdir -p ~/.config/bat
fi

touch ~/.config/bat/config
append '--theme="Visual Studio Dark+"' ~/.config/bat/config

echo "Done."
