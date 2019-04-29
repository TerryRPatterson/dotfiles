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

    # check_source $HOME/.dotfiles/z.sh
    check_source $HOME/.dotfiles/sensible.bash
    check_source $HOME/.dotfiles/.gitPrompt
    check_source $HOME/.qfc/bin/qfc.sh
    check_source /usr/share/fzf/shell/key-bindings.bash
    check_source $HOME/.dotfiles/secureKeys


    eval $(thefuck --alias darn)

    check_source $HOME/.dotfiles/bash_prompt

    #typos
    alias gti='git';
    alias sl='ls';
    alias wkr='wrk';

    # User specific aliases and functions

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

    export PROMPT_DIRTIRM=3;

    export SYSTEMD_PAGER=less
    export PAGER=less
    export LESS='-R'
    export LESSOPEN='|~/.lessfilter %s'

    export ELECTRON_TRASH=gio

    export VISUAL='code --wait -n'

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
        if [[ -z "$1" ]]
        then
            read unencoded_id
        else
            unencoded_id="$1"
        fi

        if [[ -z "$2" ]]
        then
            TYPE='OPORDR'
        else
            TYPE="$2"
        fi
        record_id=$(urlencode "$unencoded_id")
        parent_id=$(urlencode "$4")
        echo $record_id
       curl --verbose  "http://localhost:8000/gateway/order_changes?id=DTR&file=$TYPE&record_id=$record_id&drv1=$driver&ver=4&drv2=none";
    }

    alias sj="sendJob"
fi
