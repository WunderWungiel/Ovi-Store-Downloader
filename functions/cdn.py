import requests
import os
import re
import time
from colorama import init, Fore, Style

def cdn(ext):
    try:
        url = "http://wunderwungiel.pl/Symbian/OviDatabase.txt"
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Safari/537.36 OPR/72.5.3767.69342'}
        response = requests.get(url, headers=headers, allow_redirects=True)
        content = response.content.decode("utf-8")
        links = re.findall(f"(https\:\/\/d\.ovi\.com\/p\/g\/store.*\.{ext}.*)\s+", content)
        for link in links:
            link = f"http://web.archive.org/web/20150215225841/{link}"
            link_resp = requests.get(link, headers=headers, allow_redirects=True)
            filename = re.search("store/\d+\/(.*?)\?", link)
            filename = filename.group(1)
            if os.path.exists(filename):
                print(f" {filename} already exists, skipping...")
                print()
                continue
            with open(filename, "wb") as f:
                f.write(link_resp.content)
                print(f" Saved {filename}")
                print()
            time.sleep(5)
    except KeyboardInterrupt:
        print(f" {Fore.RED}KeyboardInterrupt, exiting.{Style.RESET_ALL}")
        print()
        exit(1) 
