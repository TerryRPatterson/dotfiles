# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	source /etc/bashrc
fi
export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

#customazations for interative sessions
if [ -t 1 ]
then
    function check_source {
        if [ -f $1 ]
        then
            source $1
        else
            echo missing $1
        fi
    }

    check_source /usr/share/fzf/shell/key-bindings.bash;
    check_source $HOME/.dotfiles/z.sh
    check_source $HOME/.dotfiles/sensible.bash
    check_source $HOME/.dotfiles/liquidprompt/liquidprompt

    #typos
    alias gti='git';
    alias sl='ls';
    # User specific aliases and functions
    function parse_git_branch {
         git branch --no-color 2> /dev/null | sed -e \
         '/^[^*]/d' -e 's/* \(.*\)/(\1)/';
    }
    export PS1="\[\e[0;41m\]{\$?}[\$(parse_git_branch)\W: \u]\\$\[\e[0m\] ";

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

    function reload_quotes {
        strfile -s -c % ~/Documents/quotes ~/Documents/quotes.dat;
        echo "Quotes updated!";
    }

    function tux_quote {
        fortune ~/Documents/quotes | cowsay -f tux;
    }

    if [[ -t 1 ]] && ! [[ -n $ATOM ]]; then
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
    if [ -s "$HOME/.qfc/bin/qfc.sh" ]
    then
    source "$HOME/.qfc/bin/qfc.sh"
    fi
fi
