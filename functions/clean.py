import subprocess
import os

def clean():
    subprocess.call('cls' if os.name == "nt" else "clear", shell=True)
    return 
