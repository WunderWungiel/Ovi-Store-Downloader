import os
from colorama import init, Fore, Style
from zipfile import ZipFile
import shutil

filetypes = [".jar"]
cd = os.chdir
ls = os.listdir

def changename(directory):
    files = []
    os.chdir(directory)
    for file in ls():
        if os.path.isfile(file):
            files.append(file)
    if not len(files) > 0:
        print()
        print( "No supported files in directory you've provided, returning to menu...")
        print()
        return
    for file in files:
        if file.endswith(".jar"):
            with ZipFile(file, "r") as zObject:
                zObject.extractall(directory + "_u")
            with open(f"{directory}_u/META-INF/MANIFEST.MF", "r") as f:
                for line in f:
                    if line.startswith("MIDlet-Name:"):
                        display_name = line.split(":")[1].strip()
                    if line.startswith("MIDlet-Version:"):
                        version = line.split(":")[1].strip()
            shutil.rmtree(directory + "_u")
            os.rename(file, f"{display_name} v{version}.jar")
    print(" ")
    print(f" {Fore.CYAN}Done!{Style.RESET_ALL}")
    print(" ")
    input(" Press Enter to return...")
    return