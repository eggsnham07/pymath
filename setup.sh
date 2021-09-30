#!/usr/bin/env bash
declare -A osInfo;
osInfo[/etc/arch-release]=pacman
osInfo[/etc/debian_version]=apt

for f in ${!osInfo[@]}
do
    if [[ -f $f ]]; then
        HOME=/home/$USER
        if [ ! "$(cat $HOME/.bashrc | grep pymath)" == "" ]; then
          echo "PyMath executabe path already in $HOME/.bashrc"
        else 
          echo "export PATH=\$PATH:$HOME/.local/bin/pymath" | tee -a $HOME/.bashrc
        fi;
        if [ "$USER" == "root" ]; then
          echo "You must run this as a non root user!"
        elif [ ! "$USER" == "root" ]; then
          if [ ! -d "$HOME/.local" ]; then mkdir "$HOME/.local" || echo "Making folder '$HOME/.local' failed!"; fi
          if [ ! -d "$HOME/.local/bin" ]; then mkdir $HOME/.local/bin || echo "Making folder '$HOME/.local/bin' failed!"; fi
          if [ ! -d "$HOME/.local/bin/pymath" ]; then mkdir $HOME/.local/bin/pymath || echo "Making folder '$HOME/.local/bin/pymath' failed!"; fi
          if [ ! -d "$HOME/.local/bin/pymath/pylib" ]; then mkdir $HOME/.local/bin/pymath/pylib || echo "Making folder '$HOME/.local/bin/pymath/pylib' failed!"; fi
          cp -r $PWD/* $HOME/.local/bin/pymath || echo "Moving files to '$HOME/.local/bin/pymath' failed"
          if [ "$1" == "--install-required" ]; then
            echo "Using ${osInfo[$f]} for installing python3 and python3-tk"
            if [[ ${osInfo[$f]} == pacman ]]; then
              sudo pacman -S python3 tk
            elif [[ ${osInfo[$f]} == apt ]]; then
              echo "Using ${osInfo[$f]} for installing python3 and python3-tk"
              sudo apt install python3 python3-tk
            else
              echo "Linux distro not supported!"
            fi
          else
            echo "PyMath still requires python3-tk and python3 to be installed if it is not already!"
          fi
          echo "Done!"
        fi
    fi
done