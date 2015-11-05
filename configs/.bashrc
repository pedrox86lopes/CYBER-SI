

if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi

cat /etc/motd
# Put your fun stuff here.


## Dir shortcuts
alias back='cd ..'
alias home='cd ~/'
alias documents='cd ~/Documentos'
alias downloads='cd ~/Downloads'
alias images='cd ~/Imagens'
alias videos='cd ~/Videos'
alias bin='cd ~/bin'
alias external='cd /media/XEHD'


# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if [ -f /etc/bash_completion ] && ! shopt -oq posix; then
    . /etc/bash_completion
fi

#----------------------------------------------
# Colors:
#----------------------------------------------
black='\e[0;30m'
blue='\e[0;34m'
green='\e[0;32m'
cyan='\e[0;36m'
red='\e[0;31m'
purple='\e[0;35m'
brown='\e[0;33m'
lightgray='\e[0;37m'
darkgray='\e[1;30m'
lightblue='\e[1;34m'
lightgreen='\e[1;32m'
lightcyan='\e[1;36m'
lightred='\e[1;31m'
lightpurple='\e[1;35m'
yellow='\e[1;33m'
white='\e[1;37m'
nc='\e[0m'
#------------------------------------------
#------Extraction of compressed files--------------
# from ARCH Wiki

extract () {
  if [ -f $1 ] ; then
      case $1 in
          *.tar.bz2)   tar xvjf $1    ;;
          *.tar.gz)    tar xvzf $1    ;;
          *.bz2)       bunzip2 $1     ;;
          *.rar)       rar x $1       ;;
          *.gz)        gunzip $1      ;;
          *.tar)       tar xvf $1     ;;
          *.tbz2)      tar xvjf $1    ;;
          *.tgz)       tar xvzf $1    ;;
          *.zip)       unzip $1       ;;
          *.Z)         uncompress $1  ;;
          *.7z)        7z x $1        ;;
          *)           echo "Não sei oque extrair???'$1'..." ;;
      esac
  else
      echo "'$1' is not a valid file!"
  fi
}

#------------------------------------------
#------BOAS VINDAS NIGGA--------------------
# customize this first message with a message of your choice.
# this will display the username, date, time, a calendar, the amount of users, and the up time.
clear
#-----------------------------------------------
# Startup:
#-----------------------------------------------
#!/bin/bash
echo ""
echo "───────────────┐ ░░░░░░░░░░░░░░░░░░░░░░░░░░░"
echo "   | || |_ | | | ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"
echo " |_  __  _|| | └──────────────────────────────┐"
echo -ne "  _| || |_ | |  [$USER@$HOSTNAME] [";date +"%d.%a.%b.%C%y]  |"
echo " |_  __  _||_| ┌──────────────────────────────┘"
echo "   |_||_|  (_) | ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓"
echo "───────────────┘ ░░░░░░░░░░░░░░░░░░░░░░░░░░░"


cat /etc/motd
# Put your fun stuff here.
