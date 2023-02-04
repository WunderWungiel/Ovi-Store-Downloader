import shutil
from zipfile import ZipFile
import os

def change_name(directory, extension):
    files = os.listdir(directory)
    for file in files:
        with ZipFile(f"{directory}/{file}", "r") as jar:
            jar_dir = file.strip(".jar")
            jar.extractall(path=f"{directory}/{jar_dir}")
        with open(f"{directory}/{jar_dir}/META-INF/MANIFEST.MF", "r") as jar:
            for line in jar:
                if line.startswith("MIDlet-Name:"):
                    name = line.split(":")[1].strip()
                if line.startswith("MIDlet-Version:"):
                    version = line.split(":")[1].strip()
        shutil.rmtree(f"{directory}/{jar_dir}")
        try:
            os.rename(f"{directory}/{file}", f"{directory}/{name} v{version}.jar")
        except FileExistsError:
            print("The same file exists")
            continue
