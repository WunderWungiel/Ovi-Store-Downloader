import requests
import re
import sys
import os
from colorama import init, Fore, Style

def id_f(arg1, arg2):
    for i in range(arg1, arg2):
        try:
            url = f"http://web.archive.org/web/20150128233153/http://store.ovi.com/content/{i}/download"
            response = requests.get(url, allow_redirects=True)
            if response.status_code == 200 and len(response.history) > 0 and "d.ovi" in response.url:
                content_disposition = response.headers.get("Content-Disposition")
                if content_disposition:
                    filename = re.findall("filename=(.+)", content_disposition)[0]
                else:
                    continue
                if filename.endswith(".dm"):
                    filename = filename.strip('"')
                if os.path.exists(filename):
                    print(f" {filename} already exists, skipping...")
                    print()
                    continue
                with open(filename, "wb") as f:
                    f.write(response.content)
                    print(f"Saved {filename} with ID {i}\n")
        except KeyboardInterrupt:
            print(f" {Fore.RED}KeyboardInterrupt{Style.RESET_ALL}")
            sys.exit(0)
        except:
            continue 
    return