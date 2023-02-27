import requests
import re
import sys
import os
from colorama import init, Fore, Style
from tqdm import tqdm
import time 

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

database_path = os.path.dirname(os.path.abspath(__file__)) + "/../database"

def filename(file):
    try:
        with open(database_path + "/OviDatabase.txt", "r") as database:
            content = database.read()
        time.sleep(1)
        apps = []
        apps += re.findall(f"(?i)(https://d\.ovi\.com/p/g/store/\d+/{file}\?.*)\n", content)
        if not len(apps) > 0:
            print(f" {Fore.RED}Nothing found{Style.RESET_ALL}")
            print()
            input(" Press any key to return...")
            return
        else:
            link = apps[0]
        link = link.replace("d.ovi.com/p/g/store", "web.archive.org/web/20150000000000id_/http://d.ovi.com/p/g/store")
        file_content = requests.get(link, allow_redirects=True, stream=True)
        total_size_in_bytes= int(file_content.headers.get('content-length', 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        if os.path.exists(file):
            print(f" {file} already exists, skipping...")
            print()
            input(" Press any key to return...")
            return
        with open(file, "wb") as f:
            for data in file_content.iter_content(block_size):
                progress_bar.update(len(data))
                f.write(data)
        progress_bar.close()
        print()
        print(f" Saved {file}\n")
    except KeyboardInterrupt:
        print(f" {Fore.RED}KeyboardInterrupt{Style.RESET_ALL}")
        sys.exit(0) 
    input(" Press any key to return...")
    return