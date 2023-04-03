#!/bin/bash

script_dir="$(cd "$(dirname ${BASH_SOURCE[0]-$0})" && pwd)"

# system
alias ls='ls -1'
alias ll='ls -lGA'
alias bat='bat --paging=never'
alias reprofile='source ~/.zshrc'
alias copypk='cat $(ls ~/.ssh/*.pub | head -1) | pbcopy'
alias pbjson='pbpaste | python -m json.tool | bat -l json'
alias boop='osascript -e "display notification \"Command finished executing 👍\" with title \"Terminal\" sound name \"Submarine\""'
alias restartcal='launchctl stop com.apple.CalendarAgent && launchctl start com.apple.CalendarAgent'

# Git
alias gamd='git commit -a --amend'
alias gbra='git rev-parse --abbrev-ref HEAD'
alias gdel="$script_dir/scripts/gdel.sh"
alias gdif='git diff'
alias glas='git checkout -'
alias glog='git log --pretty=oneline --abbrev-commit -10'
alias gmas='git checkout $(gmasb)'
alias gmasb='git show-ref --verify --quiet refs/heads/main && echo main || echo master'
alias gmasp='git checkout $(gmasb) && git pull'
alias gmer='git checkout $(gmasb) && git pull && git checkout - && git merge $(gmasb)'
alias gmerc='git add . && git commit'
alias gmit='git commit -am'
alias gnew='git checkout -b'
alias gpul='git pull'
alias gpus="$script_dir/scripts/gpus.sh"
alias greb='git checkout $(gmasb) && git pull && git checkout - && git rebase -i $(gmasb)'
alias grebc='git add . && git rebase --continue'
alias gren='git branch -m'
alias gres='git reset --hard origin/$(gbra)'
alias gsta='git status'

# Docker
alias dkill='docker kill $(docker ps -q)'
alias dprune='docker system prune -af --volumes'
alias dps="docker ps --format \"table {{.ID}}\t{{.Names}}\t{{.Command}}\t{{.Status}}\""
alias drm='docker rm $(docker ps -a -q)'
alias drmi='docker rmi $(docker images -q)'

# Node
alias denode='$(TMP=$(mktemp -d) && mv -f node_modules $TMP && rm -rf $TMP) &> /dev/null &'
alias npy='npx --yes'

# VSCode
alias codea='code --add'
alias codew='code --reuse-window'
