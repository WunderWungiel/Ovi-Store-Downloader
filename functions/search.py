import re
import requests
import os
import sys
from colorama import init, Fore, Style
from tqdm import tqdm
import time

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

database_path = os.path.dirname(os.path.abspath(__file__)) + "/../database"

def search(name, extensions):
    try:
        with open(database_path + "/OviDatabase.txt", "r") as database:
            content = database.read()
        with open(database_path + "/MaemoOviDatabase.txt", "r") as database:
            content2 = database.read()
        time.sleep(1)
        if " " in name:
            name = name.replace(" ", ".*")
        apps = []
        mapps = []
        if extensions == None:
            apps += re.findall(f"(?i)https://d\.ovi\.com/p/g/store/\d+/({name}.*)\?", content)
            mapps += re.findall(f"(?i)http://archive.org/download/maemo-fremantle-ovi/maemo-fremantle-ovi.tar/maemo-fremantle-ovi/mirror/downloads.maemo.nokia.com/fremantle1.2/ovi/({name}.*\..*)\n", content2)
        else:
            for ext in extensions:
                apps += re.findall(f"(?i)https://d\.ovi\.com/p/g/store/\d+/({name}.*\.{ext})\?", content)
                mapps += re.findall(f"(?i)http://archive.org/download/maemo-fremantle-ovi/maemo-fremantle-ovi.tar/maemo-fremantle-ovi/mirror/downloads.maemo.nokia.com/fremantle1.2/ovi/({name}.*\.{ext})\n", content2)
        apps_nums = {}
        mapps_nums = {}
        all_nums = {}
        for i, app in enumerate(apps, start=1):
            apps_nums.update({str(i) : app})
        last_app = len(apps)
        for i, mapp in enumerate(mapps, start=last_app + 1):
            mapps_nums.update({str(i) : mapp})
        all_nums.update(apps_nums)
        all_nums.update(mapps_nums)
        if not len(apps) > 0:
            if not len(mapps) > 0:
                print(f" {Fore.RED}Nothing found{Style.RESET_ALL}")
                print()
                input(" Press Enter to return...")
                return
        print(f" {Fore.CYAN}Found:{Style.RESET_ALL}")
        print()

        apps_links = {}
        mapps_links = {}
        all_links = {}
        for num, app in apps_nums.items():
            links = re.findall(f"(?i)(https://d\.ovi\.com/p/g/store.*{app}.*)\s+", content)
            link = links[0]
            link = f"http://web.archive.org/web/20150215225841id_/{link}"
            apps_links.update({app : link})
            if not app.endswith(".deb"):
                print(f" {num}. {app}")
            else:
                print(f" {num}. [MeeGo] {app}")
            print()
            
        for num, mapp in mapps_nums.items():
            links = re.findall(f"(?i)(http://archive.org/download/maemo-fremantle-ovi/maemo-fremantle-ovi.tar/maemo-fremantle-ovi/mirror/downloads.maemo.nokia.com/fremantle1.2/ovi/.*{mapp}.*)\n", content2)
            link = links[0]
            mapps_links.update({mapp : link})
            print(f" {num}. [Maemo] {mapp}")
            print()
        all_links.update(apps_links)
        all_links.update(mapps_links)
        all_answers = ["a", "all"]
        while True:
            ask = input(f" {Fore.BLUE}Download what has been found?{Style.RESET_ALL} Insert numbers seperated by comma and space, type \"a\" to download everything, or press 0 to return.\n\n ")
            if ask.lower() in [ask.lower() for ask in all_answers]:
                print()
                print(f" {Fore.BLUE}Downloading everything{Style.RESET_ALL}")
                print()
                for link in all_links.values():
                    response = requests.get(link, headers=headers, allow_redirects=True, stream=True)
                    total_size_in_bytes= int(response.headers.get('content-length', 0))
                    block_size = 1024
                    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                    filename = re.search("store/\d+/(.*?)\?", link)
                    if not filename:
                        filename = re.search("/ovi/(.*)", link)
                    filename = filename.group(1)
                    if os.path.exists(filename):
                        print(f" {filename} already exists, skipping...")
                        print()
                        continue
                    with open(filename, "wb") as f:
                        for data in response.iter_content(block_size):
                            progress_bar.update(len(data))
                            f.write(data)
                        progress_bar.close()
                        print()
                        print(f" Saved {filename}")
                    print()
                print(f" {Fore.LIGHTGREEN_EX}Downloaded everything!{Style.RESET_ALL}")
                print()
                input(" Press Enter to return...")
                return
            todl = ask.split(" ")
            todl = list(set(todl))
            if ask == "0":
                return
            if ask != "a" and not all(num in all_nums.keys() for num in todl):
                print()
                print(f" {Fore.RED}One of numbers is wrong!{Style.RESET_ALL}")
                print()
                continue
            else:
                print()
                break
        for num in todl:
            link = all_links[all_nums[num]]
            app = all_nums[num]
            if os.path.exists(app):
                print(f" {app} already exists, skipping...")
                print()
                continue
            response = requests.get(link, headers=headers, allow_redirects=True, stream=True)
            total_size_in_bytes= int(response.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
            with open(app, "wb") as f:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    f.write(data)
            progress_bar.close()
            print()
            print(f" Saved {app}")
            print()
            
    except KeyboardInterrupt:
        print(f" {Fore.RED}KeyboardInterrupt, exiting.{Style.RESET_ALL}")
        print()
        sys.exit(1) 
    input(" Press Enter to return...")
    return