#!/bin/bash -e

echo_command() {
  if [[ $2 != n ]]; then echo; fi
  echo -e "${bright}${1}${normal}"
}

echo_error() {
  if [[ $2 != n ]]; then echo; fi
  echo -e "${error}${1}${normal}"
}

echo_exception() {
  echo_error "$1" "$2"
  exit 1
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

# globals
bright="\033[1;36m"
error="\033[1;31m"
warning="\033[1;33m"
normal="\033[0m"
current_branch="$(git rev-parse --abbrev-ref HEAD)"

if [[ $current_branch == "master" ]]; then
  echo_exception 'Error: current branch is "master".'
fi

if [[ $(git diff master..$current_branch) == *"!!!"* ]]; then
  echo_warning 'Bangs exist in the diff.'
  ask_continue
fi

echo_warning 'Continuing will force push to the server.'
ask_continue

echo_command "Force pushing \"$current_branch\"..."
git push -u origin "$current_branch" --force
