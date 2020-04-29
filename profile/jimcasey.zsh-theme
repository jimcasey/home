# local time, color coded by last return code
time="%(?.%{$fg[green]%}.%{$fg[red]%})%*%{$reset_color%}"

# working directory
working_directory="%{$fg[cyan]%}%~%{$reset_color%}"

# git_prompt_info properties
ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[yellow]%}"
ZSH_THEME_GIT_PROMPT_DIRTY=" "
ZSH_THEME_GIT_PROMPT_CLEAN=" %{$fg_bold[green]%}✓"
ZSH_THEME_GIT_PROMPT_SUFFIX=""

# git_prompt_status properties
# xterm color chart: https://upload.wikimedia.org/wikipedia/commons/1/15/Xterm_256color_chart.svg
ZSH_THEME_GIT_PROMPT_ADDED="%{$FG[082]%}✚"
ZSH_THEME_GIT_PROMPT_MODIFIED="%{$FG[166]%}✹"
ZSH_THEME_GIT_PROMPT_DELETED="%{$FG[160]%}✖"
ZSH_THEME_GIT_PROMPT_RENAMED="%{$FG[220]%}➜"
ZSH_THEME_GIT_PROMPT_UNMERGED="%{$FG[082]%}═"
ZSH_THEME_GIT_PROMPT_UNTRACKED="%{$FG[190]%}✭"

# build the prompt
# prompt reference: http://zsh.sourceforge.net/Doc/Release/Prompt-Expansion.html
PROMPT='
${time} ${working_directory} $(git_prompt_info)$(git_prompt_status)%{$reset_color%}
$ '
