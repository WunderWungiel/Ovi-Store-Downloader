# Ovi-Store-Downloader
Small shell script to ease browsing archived Ovi Store on Wayback Machine.

This small Python 3 script was was born by idea of browsing Ovi Store nowadays more easily. Actually, you needed to:
- Have direct link to app (e.g. http://store.ovi.com/content/260149);
- Then, you could add /download at the end of the url;
- And pray and pray that it will be archived on Wayback Machine.

Not more!  With this small script, it gets easier! You get:
- ability to search ONLY for apps, which are really archived on Wayback Machine;
- download chosen or all;
- download app with specific ID
- start bulk-downloading content with specific extension
- In future: change name of files automatically, to make them more pretty.

## Requirements:

- machine with Python 3 installed
- `requests` module. On Linux it's quite easy - Python should be installed by default. On Windows download it from Python.org OR you could use something like **Cygwin** / **WSL**.

To install `requests` module: On Windows, use pip (in cmd/PowerShell):

    pip install requests

On Arch Linux/Manjaro:

    sudo pacman -Syu python-requests

On Ubuntu/Debian:

    sudo apt-get install python3-requests

For other distros, search in Google. 

- `colorama` library, if not installed already. Use the same as above, replacing `requests` with `colorama`. 

## How to run and use?

Navigate to folder with `ovistore.py` file using your Terminal emulator:

      cd /path/to/folder

Run Ovi Store Downloader using Python 3:

Windows: `py .\ovistore.py`
Linux: `python3 ./ovistore.py`

Discover, use and have fun!
