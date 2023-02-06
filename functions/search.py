import re
import requests
import os
import sys
from colorama import init, Fore, Style
import time

def search(name, extensions):
    try:
        url = "http://wunderwungiel.pl/Symbian/OviDatabase.txt"
        headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 11; SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Safari/537.36 OPR/72.5.3767.69342'}
        response = requests.get(url, headers=headers)
        content = response.content.decode("utf-8")
        apps = []
        whitespaces = ["\s*", "_", "-", ""]
        if " " in name:
            name = name.replace(" ", ".*")
        if extensions == None:
            for whitespace in whitespaces:
                apps += re.findall(f"(?i)https\:\/\/d\.ovi\.com\/p\/g\/store\/\d+\/({name}{whitespace}.*)\?", content)
        else:
            for ext in extensions:
                apps += re.findall(f"(?i)https\:\/\/d\.ovi\.com\/p\/g\/store\/\d+\/({name}.*\.{ext})\?", content)
        if not len(apps) > 0:
            print(f" {Fore.RED}Nothing found{Style.RESET_ALL}")
            print()
            sys.exit(0)
        print(f" {Fore.CYAN}Found:{Style.RESET_ALL}")
        print()

        all_links = []
        all_apps = []
        for app in apps:
            links = re.findall(f"(?i)(https\:\/\/d\.ovi\.com\/p\/g\/store.*{app}.*)\s+", content)
            link = links[0]
            link = f"http://web.archive.org/web/20150215225841/{link}"
            all_links.append(link)
            all_apps.append(app)
            print(f" {app}")
            print()

        while True:
            ask = input(f" {Fore.BLUE}Download what has been found?{Style.RESET_ALL} Insert filenames seperated by comma and space, or type \"a\" to download everything.\n\n ")
            if ask == "a":
                print()
                print(f" {Fore.BLUE}Downloading everything{Style.RESET_ALL}")
                print()
                for link in all_links:
                    response = requests.get(link, headers=headers, allow_redirects=True)
                    filename = re.search("store/\d+\/(.*?)\?", link)
                    filename = filename.group(1)
                    if os.path.exists(filename):
                        print(f" {filename} already exists, skipping...")
                        print()
                        continue
                    with open(filename, "wb") as f:
                        f.write(response.content)
                        print(f" Saved {filename}")
                        print()
                print(f" {Fore.LIGHTGREEN_EX}Downloaded everything!{Style.RESET_ALL}")
                print()
                sys.exit(0)
            todl = ask.split(", ")
            todl = list(set(todl))
            if ask != "a" and not all(item in apps for item in todl):
                print()
                print(f" {Fore.RED}One of filenames is wrong!{Style.RESET_ALL}")
                print()
                continue
            else:
                print()
                break
        matches = []
        for dl in todl:
            for link in all_links:
                if dl in link:
                    matches.append(link)
        for match in matches:
            response = requests.get(match, headers=headers, allow_redirects=True)
            filename = re.search("store/\d+\/(.*?)\?", match)
            filename = filename.group(1)
            if os.path.exists(filename):
                print(f" {filename} already exists, skipping...")
                print()
                continue
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f" Saved {filename}")
                print()
            
    except KeyboardInterrupt:
        print(f" {Fore.RED}KeyboardInterrupt, exiting.{Style.RESET_ALL}")
        print()
        sys.exit(1) 
    time.sleep(10)
    return