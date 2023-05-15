#!/bin/sh

if ! command -v python3 &> /dev/null
then
    echo "Python3 not found."
    exit 1
fi

if [ -f "/usr/bin/konsole" ]; then
    /usr/bin/konsole -e python3 main.py
elif [ -f "/bin/xterm" ]; then
    /usr/bin/xterm -e python3 main.py
elif [ -f "/usr/bin/gnome-terminal" ]; then
    /usr/bin/gnome-terminal -- python3 main.py
else
    echo "I didn't find Terminal emulator."
    exit 1
fi
exit 0
