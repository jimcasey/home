#!/bin/bash -e

echo_bright() {
  echo -e "${bright}${1}${normal}"
}

echo_version() {
  printf -v name "%11s" "$1"
  echo -e "${cyan}${name}${normal} : ${gray}${2}${normal}"
}

get_version() {
  local output
  output=$(n which $1 2>&1)
  if [[ $? -ne 0 ]]; then
    echo ""
  else
    if [[ $output =~ ([0-9]+\.[0-9]+\.[0-9]+) ]]; then
      echo "${BASH_REMATCH[1]}"
    else
      echo ""
    fi
  fi
}

bright="\033[1;36m"
cyan="\033[36m"
gray="\033[37m"
normal="\033[0m"

current_version=$(node --version)
current_version=${current_version:1}
auto_version=$(get_version auto)
lts_version=$(get_version lts)

echo_bright 'Node versions:'
echo_version 'current' $current_version
echo_version 'auto' ${auto_version:-n/a}
echo_version 'lts' $lts_version

if [[ "$auto_version" == "$current_version" || "$lts_version" == "$current_version" ]]; then
  exit 0
fi

echo
if [ -n "$auto_version" ]; then
  echo_bright 'Switching to configured Node version...'
  n auto
else
  echo_bright 'Switching to the LTS Node version...'
  n lts
fi
