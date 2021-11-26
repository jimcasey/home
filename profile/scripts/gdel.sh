#!/bin/bash -e

function show_usage_and_exit() {
  script_name=`basename "$0"`

  echo -e "${bright}Deletes Git branches.${normal}"
  echo "Usage: $script_name [options]"
  echo
  echo "Options:"
  echo "  -h, --help       Show this help and exit"
  echo "  -a, --all        Ask to delete all branches"
  echo "  -s, --skip       Skip branches that are in the list"
  echo
  echo "Examples:"
  echo "  $script_name"
  echo "  $script_name delete-this-branch"
  echo "  $script_name -s skip-this-branch skip-that-branch starts-with-*"
  exit 1
}

echo_action() {
  echo -e "${bright}${1}${normal}"
}

echo_gray() {
  echo -e "${gray}${1}${normal}"
}

echo_error() {
  echo -e "${error}${1}${normal}"
}

echo_exception() {
  echo_error "$1"
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
gray="\033[90m"
warning="\033[1;33m"
error="\033[1;31m"
normal="\033[0m"

current_branch="$(git rev-parse --abbrev-ref HEAD)"
delete_all=n
should_skip=n
main_branch=$(git show-ref --verify --quiet refs/heads/main && echo main || echo master)
skip_branches="$main_branch"

for arg; do
  if [[ ${arg:0:1} == '-' ]]; then
    if [[ $arg == '-h' || $arg == '--help' ]]; then
      show_usage_and_exit
    elif [[ $arg == '-a' || $arg == '--all' ]]; then
      delete_all=y
    elif [[ $arg == '-s' || $arg == '--skip' ]]; then
      delete_all=y
      should_skip=y
    else
      echo_error 'Invalid command.'
      show_usage_and_exit
    fi
  elif [[ $should_skip == y ]]; then
    skip_branches="${skip_branches} $arg"
  else
    delete_branch=$arg
  fi
done

if [[ $delete_all == y ]]; then
  echo
  if [[ $should_skip == y ]]; then
    echo_action 'Deleting all branches with exceptions...'
  else
    echo_action 'Deleting all branches...'
  fi

  all_branches=$(git for-each-ref --shell --format="%(refname:short)" refs/heads/)
  skip_branches=${skip_branches//\*/.\*}
  skip_branches="^(${skip_branches// /|})\$"

  for b in $all_branches; do
    branch=${b//"'"/}
    if [[ ! $branch =~ $skip_branches ]]; then
      ask_question input_response "Delete $branch?"

      if [[ $input_response == y ]]; then
        if [[ $branch == $current_branch ]]; then

          echo_warning "Deleting current branch, checkout $main_branch..."
          git checkout $main_branch
        fi

        git branch -D $branch
      fi
    else
      echo_gray "Skipping $branch..."
    fi
  done
else
  branch=${delete_branch:-$current_branch}

  if [[ $branch == $main_branch ]]; then
    echo_exception "Error: current branch is \"${branch}\"."
  fi

  echo_warning 'This is a hard delete, unpushed changes will be discarded'
  ask_continue

  if [[ $branch == $current_branch ]]; then
    git checkout $main_branch
  fi

  git branch -D $branch
fi

echo
echo_action 'Done!'
