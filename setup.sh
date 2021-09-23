#!/usr/bin/env bash
HOME=/home/$USER
if [ "$USER" == "root" ]; then
  echo "You must run this as a non root user!"
elif [ ! "$USER" == "root" ]; then
  if [ ! -d "$HOME/.local/bin" ]; then mkdir $HOME/.local/bin || echo "Making folder '$HOME/.local/bin' failed!"; fi
  if [ ! -d "$HOME/.local/bin/pymath" ]; then mkdir $HOME/.local/bin/pymath || echo "Making folder '$HOME/.local/bin/pymath' failed!"; fi
  if [ ! -d "$HOME/.local/bin/pymath/pylib" ]; then mkdir $HOME/.local/bin/pymath/pylib || echo "Making folder '$HOME/.local/bin/pymath/pylib' failed!"; fi
  cp -r $PWD/* $HOME/.local/bin/pymath
  echo "Done!"
fi
