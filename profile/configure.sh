#!/bin/bash

echo_action() {
  echo
  echo -e "${bright}${1}${normal}"
}

bright="\033[1;36m"
normal="\033[0m"

script_dir="$(cd "$(dirname ${BASH_SOURCE[0]-$0})" && pwd)"

zshrc_local=~/.zshrc
zshrc_command="source ${script_dir}/.zshrc"

if ! grep -qs "$zshrc_command" $zshrc_local; then
  echo_action "Configuring ${zshrc_local}..."
  touch $zshrc_local
  echo $zshrc_command >> $zshrc_local
fi

zshrc_backup=~/.zshrc.pre-oh-my-zsh
if [[ -f $zshrc_backup ]]; then
  echo_action "Restoring ${zshrc_local}..."
  rm $zshrc_local
  mv $zshrc_backup $zshrc_local
fi

echo "Done."
