import requests
import os
import re
import time
from colorama import init, Fore, Style

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

database_path = os.path.dirname(os.path.abspath(__file__)) + "/../database"

def cdn(ext):
    try:
        with open(database_path + "/OviDatabase.txt", "r") as database:
            content = database.read()
        links = re.findall(f"(https://d\.ovi\.com/p/g/store.*\.{ext}.*)\s+", content)
        for link in links:
            link = f"http://web.archive.org/web/20150215225841id_/{link}"
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
    input(" Press any key to return...")
    return