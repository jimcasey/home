#!/bin/bash -e
# Synchronizes Visual Studio Code settings between this repo and your local VSCode settings directory.
# This is very overengineered.

function show_usage_and_exit() {
  script_name=`basename "$0"`

  echo -e "${bright}Synchronizes Visual Studio Code settings.${normal}"
  echo "Usage: $script_name [options]"
  echo
  echo "Options:"
  echo "  up               Copies files to the repository (default)"
  echo "  down             Copies files to your VSCode settings directory"
  echo "  -d, --diff       Show the diff between files"
  echo "  -h, --help       Show this help and exit"
  echo
  echo "Examples:"
  echo "  $script_name"
  echo "  $script_name down"
  exit 1
}

echo_action() {
  echo -e "${bright}${1}${normal}"
}

echo_cmd() {
  echo -e "${gray}${1}${normal}"
}

echo_error() {
  echo -e "${error}${1}${normal}"
}

echo_warning() {
  if [[ $2 != n ]]; then echo; fi
  echo -e "${warning}${1}${normal}"
}

ask_continue() {
  ask_question input_response "$1" "$2"

  if [[ $input_response != y ]]; then
    exit 1
  fi
}

ask_question() {
  question_text=${2:-'Continue?'}
  default_response=${3:-n}

  message_text="$question_text ($default_response):"
  read -n 1 -p "$message_text " input_response

  if [[ -z $input_response ]]; then
    echo -en "\033[A" # move up
    echo -en "$message_text $default_response"
    input_response=$default_response
  fi

  eval $1="$input_response"
  echo
}

show_diff=n
sync_direction=up

for arg; do
  if [[ $arg == '-h' || $arg == '--help' ]]; then
    show_usage_and_exit
  elif [[ $arg == '-d' || $arg == '--diff' ]]; then
    show_diff=y
  elif [[ $arg == 'up' ]]; then
    sync_direction=up
  elif [[ $arg == 'down' ]]; then
    sync_direction=down
  else
    echo_error 'Invalid command.'
    show_usage_and_exit
  fi
done

# globals
bright="\033[1;36m"
gray="\033[90m"
warning="\033[1;33m"
error="\033[1;31m"
normal="\033[0m"

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
settings_dir=$HOME/Library/Application\ Support/Code/User
files=(keybindings.json settings.json)

if [[ $show_diff == y ]]; then
  for file in ${files[*]}; do
    echo_action "Changes in $file:"
    git diff "$settings_dir/$file" "$repo_dir/$file"
    echo
  done
  exit 1
fi

if [[ $sync_direction == up ]]; then
  echo_action 'Synchronizing files to repository directory...'
  source_dir=$settings_dir
  dest_dir=$repo_dir
elif [[ $sync_direction == down ]]; then
  echo_action 'Synchronizing files to settings directory...'
  echo_warning 'This will overwrite your local settings files.'
  ask_continue
  echo

  source_dir=$repo_dir
  dest_dir=$settings_dir
fi

echo_cmd "Source:      $source_dir"
echo_cmd "Destination: $dest_dir"
echo

for file in ${files[*]}; do
  echo_cmd "Copying $file..."
  cp "$source_dir/$file" "$dest_dir/"
done

echo
echo_action 'Done!'
