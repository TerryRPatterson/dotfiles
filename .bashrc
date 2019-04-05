# .bashrc

function check_source {
        if [ -f $1 ]
        then
            source $1
        else
            echo missing $1
        fi
    }

# Source global definitions
check_source /etc/bashrc

export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"
export PATH="$HOME/activityReader/dev_tools:$PATH"

# customazations for interactive sessions
if [ -t 1 ]
then

    eval $(thefuck --alias)
    



    check_source $HOME/dtr-code/dev-tools/env/dtr_dev.bash
    # check_source $HOME/.dotfiles/z.sh
    check_source $HOME/.dotfiles/sensible.bash
    check_source $HOME/.dotfiles/.gitPrompt
    # check_source $HOME/.dotfiles/liquidprompt/liquidprompt
    check_source $HOME/.qfc/bin/qfc.sh
    check_source $HOME/.fzf.bash
    check_source $HOME/.secureKeys

    eval $(thefuck --alias darn)

    check_source $HOME/.dotfiles/liquidprompt/liquidprompt
	check_source $HOME/api_keys

    #typos
    alias gti='git';
    alias sl='ls';
    alias wkr='wrk';
    # User specific aliases and functions
    # function parse_git_branch {
    #      git branch --no-color 2> /dev/null | sed -e \
    #      '/^[^*]/d' -e 's/* \(.*\)/(\1)/';
    # }
    function get_wrk_env {
        if [[ -n "$WRK_ENV" ]]
        then
            echo -n "[$WRK_ENV]"
        fi
    }

    function get_previous {
        previous=$?
        if [[ -n "$WRK_ENV" ]]
        then
            current=$WRK_ENV
        else
            current=$(truncate_pwd)
        fi
        echo -ne "\033]0; ${current} \007"
        if [[ $previous != 0 ]]
        then
            echo -en "\e[0;41m[$previous]\e[0m"
        fi
    }

    function truncate_pwd {
     if [ $HOME == $PWD ]
     then
       newPWD="~"
     elif [ $HOME ==  ${PWD:0:${#HOME}} ]
     then
       newPWD="~${PWD:${#HOME}}"
     else
       newPWD=$PWD
     fi

      local pwdmaxlen=30
      if [ ${#newPWD} -gt $pwdmaxlen ]
      then
        local pwdoffset=$(( ${#newPWD} - $pwdmaxlen  ))
        newPWD="${newPWD:$pwdoffset:$pwdmaxlen}"
      fi
      echo $newPWD
    }

    function build_prompt {
        get_wrk_env;
        echo -en \W
        parse_git_branch;
    }
    PROMPT_COMMAND="get_previous"
    PS1="\[\e[0;41m\]\$(get_wrk_env)\$(parse_git_branch)\\$\[\e[0m\] "
    export LP_PS1_PREFIX="${get_wrk_env}"
    export PS1=$PS1;

    alias py='python3';

    alias chrome='google-chrome';

    alias ping='prettyping --nolegend';

    alias du='ncdu';

    alias grep='ag';

    alias more='less';

    alias rm='rm -r';

    alias update='sudo dnf update';

    function pipenv_remove {
        pipenv uninstall "$@";
    }

    export LESSOPEN='|~/.lessfilter %s'

    export dirtrim=3;

    export SYSTEMD_PAGER=less
    export PAGER=less
    export LESS='-R'
    export LESSOPEN='|~/.lessfilter %s'

    export ELECTRON_TRASH=gio

    export VISUAL='code'

    function reload_quotes {
        strfile -s -c % ~/Documents/quotes ~/Documents/quotes.dat;
        echo "Quotes updated!";
    }

    function tux_quote {
        fortune ~/Documents/quotes | cowsay -f tux;
    }

    if [[ -t 1 ]] && [[ -z $ATOM ]] && [[ -z $VS_CODE ]]; then
        tux_quote
    fi

    function server {
        python -m SimpleHTTPServer $1;
    }

    function mkcd {
        mkdir $1;
        cd $1;
    }

    function purgeHeresy {
        find $HOME -name .DS_Store -type f -print -exec rm -rf {} \;
    }

    function ls {
        if [ -d .git ]
        then
          exa --long --git "$@";
        else
          exa "$@";
        fi
    }

    alias urldecode='python -c "import sys, urllib as ul; \
        print ul.unquote(sys.argv[1])"'
    alias urlencode='python -c "import sys, urllib as ul; \
        print ul.quote(sys.argv[1])"'

    function sendJob {
        if [[ -z "$2" ]]
        then
            TYPE='OPORDR'
        else
            TYPE="$2"
        fi
        record_id=$(urlencode "$1")
        parent_id=$(urlencode "$4")
        echo $record_id
       curl --verbose  "http://localhost:8000/gateway/order_changes?id=DTR&file=$TYPE&record_id=$record_id&drv1=$driver&ver=4&drv2=none";
    }

fi
