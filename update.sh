#!/bin/bash
python3 background.py

export DISPLAY=:0
export XAUTHORITY=/home/pi/.Xauthority
export XDG_RUNTIME_DIR=/run/user/1000

pcmanfm --set-wallpaper temp.jpg
pcmanfm --reconfigure
