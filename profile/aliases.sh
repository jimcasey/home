#!/bin/bash

script_dir="$(cd "$(dirname ${BASH_SOURCE[0]-$0})" && pwd)"

# tools
alias ls='ls -1'
alias ll='ls -lGA'
alias bat='bat --paging=never'
alias reprofile='exec zsh'
alias copypk='cat $(ls ~/.ssh/*.pub | head -1) | pbcopy'
alias pbjson='pbpaste | python3 -m json.tool | bat -l json'
alias boop='osascript -e "display notification \"Command finished executing 👍\" with title \"Terminal\" sound name \"Submarine\""'
alias restartcal='launchctl stop com.apple.CalendarAgent && launchctl start com.apple.CalendarAgent'
alias ssht='function _ssht(){ ssh "$1" "echo Touched\!"; };_ssht'
alias uuid='uuidgen | tr "[:upper:]" "[:lower:]" | pbcopy'

# Git
alias gamd='git commit -a --amend'
alias gbra='git rev-parse --abbrev-ref HEAD'
alias gc='git checkout'
alias gdel="$script_dir/scripts/gdel.sh"
alias gdif='git diff'
alias glas='git checkout -'
alias glog='git log --pretty=oneline --abbrev-commit -10'
alias glogs='for k in $(git branch | perl -pe s/^..//); do echo -e $(git show --pretty=format:"%ci\t%cr" $k -- | head -n 1)\\t$k; done | sort'
alias gm='git checkout $(gmasb)'
alias gmas='git checkout $(gmasb)'
alias gmasb="git remote show origin | awk -F': ' '/HEAD branch/ {print \$2}' | xargs"
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
alias grmi='for f in $(git ls-files --ignored --others --exclude-standard --directory | grep -v "\.env$"); do rm -rf $f; done'
alias grun='git reset head^'
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
alias nv="$script_dir/scripts/nv.sh"

# Python
alias py='python3'

# VSCode
alias codea='code --add'
alias codew='code --reuse-window'

# Cursor
alias cursora='cursor --add'
alias cursorw='cursor --reuse-window'

# Copilot
alias suggest='ghcs'
alias explain='ghce'
