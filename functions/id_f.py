import requests
import re
import sys
import os
from colorama import init, Fore, Style
from tqdm import tqdm

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0'
}

def id_f(arg1, arg2):
    for i in range(arg1, arg2):
        try:
            url = f"http://web.archive.org/web/20150128233153id_/http://store.ovi.com/content/{i}/download"
            response = requests.get(url, allow_redirects=True, stream=True)
            if response.status_code == 200 and len(response.history) > 0 and "d.ovi" in response.url:
                content_disposition = response.headers.get("Content-Disposition")
                total_size_in_bytes= int(response.headers.get('content-length', 0))
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
                block_size = 1024
                progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                with open(filename, "wb") as f:
                    for data in response.iter_content(block_size):
                        progress_bar.update(len(data))
                        f.write(data)
                    progress_bar.close()
                    print()
                    print(f" Saved {filename} with ID {i}\n")
        except KeyboardInterrupt:
            print(f" {Fore.RED}KeyboardInterrupt{Style.RESET_ALL}")
            sys.exit(0)
        except:
            continue 
    input(" Press Enter to return...")
    return