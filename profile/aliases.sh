#!/bin/bash

# system
alias ls="ls -1"
alias ll="ls -l"
alias reprofile="source ~/.zshrc"
alias copypk="cat ~/.ssh/id_rsa.pub | pbcopy"
alias pbjson="pbpaste | python -m json.tool | bat -l json"
alias n='osascript -e "display notification \"Command finished executing 👍\" with title \"Terminal\" sound name \"Submarine\""'

# Git
alias gamd="git commit -a --amend"
alias gcha="git commit --amend"
alias gdel="$PROFILE_FOLDER/scripts/gdel.sh"
alias gdif="git diff"
alias glas="git checkout -"
alias glog="git log --pretty=oneline --abbrev-commit -10"
alias gmas="git checkout master"
alias gmit="git commit -am"
alias gnew="git checkout -b"
alias gpul="git pull"
alias gpus="$PROFILE_FOLDER/scripts/gpus.sh"
alias greb="git checkout master && git pull && git checkout - && git rebase -i master"
alias grebc="git add . && git rebase --continue"
alias gren="git branch -m"
alias gsta="git status"

alias gmasp="gmas && gpul"
alias grebp="greb && gpus"

# Docker
alias dprune="docker system prune -af --volumes"
alias dps="docker ps --format \"table {{.ID}}\t{{.Names}}\t{{.Command}}\t{{.Status}}\""
