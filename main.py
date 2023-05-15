#!/usr/bin/python3

import sys
import os
import sys

try:
    import colorama
except ImportError:
    sys.stderr.write(" \"colorama\" module not found, install it with pip.\n")
    sys.exit(1)

try:
    import requests
except ImportError:
    sys.stderr.write(" \"requests\" module not found, install it with pip.\n")
    sys.exit(1)

try:
    import tqdm
except ImportError:
    sys.stderr.write(" \"tqdm\" module not found, install it with pip.\n")
    sys.exit(1)

from colorama import init, Fore, Style
from functions.id_f import id_f
from functions.search import search
from functions.cdn import cdn
from functions.help_f import help_f
from functions.changename import changename
from functions.dmremover import dmremover
from functions.filename import filename
from functions.menu import menu
from functions.about import about
from functions.clean import clean

sup_extensions = ["sis", "sisx", "sis.dm", "sisx.dm", "deb", "jar", "wgz", "gif.dm", "mp4.dm", "3gp.dm", "3gp", "jpg"]

functions = ["--cdn", "--id", "--help", "--search", "--about", "--changename", "--removedm", "--filename"]

ls = os.listdir

if __name__ == "__main__":
    if len(sys.argv) > 1:
    
        print()
        print(" ################################################################")
        print(" ################################################################")
        print(" ##################### Ovi Store Downloader #####################")
        print(" ################################################################")
        print(" ####################### By Wunder Wungiel ######################")
        print(" ################################################################")
        print(" ################################################################")
        print()
    
        function = sys.argv[1]
        
        if not function in functions:
            print(" First argument is wrong! See --help.")
            print()
            sys.exit(1)
    
        if function == "--id":
            if not len(sys.argv) > 2:
                print(" First argument after --id argument should be the minimal ID for search")
                print()
                sys.exit(1)
            arg1 = sys.argv[2]
            arg1 = int(arg1)
            if not len(sys.argv) > 3:
                arg2 = arg1 + 1
            else:
                arg2 = sys.argv[3]
                arg2 = int[arg2]
            id(arg1, arg2)

        elif function == "--cdn":
            if not len(sys.argv) > 2:
                print(" First argument after --cdn should be the extension to search.")
                print()
                sys.exit(1)
            ext = str(sys.argv[2])
            if ext not in sup_extensions:
                print(" Wrong extension!")
                print(" Allowed extensions (for now): " + ", ".join(str(item) for item in sup_extensions))
                print()
                sys.exit(1)
            print(f" Picking *.{ext} extension.")
            print()
            cdn(ext)
        elif function == "--removedm":
            if not len(sys.argv) >2:
                print(" Second argument should be filename / directory.")
                print()
                sys.exit(1)
            argument = str(sys.argv[2]               )
            if os.path.isfile(argument):
                if not argument.endswith(".dm"):
                    print(" Filename doesn't end with .dm - try again!")
                    print()
                    sys.exit(1)
                function = "file"
            elif os.path.isdir(argument):
                isdm = False
                for filename in ls(argument):
                    if filename.endswith(".dm"):
                        isdm = True
                        break
                if not isdm:
                    print(" No .dm files in specified directory - try again!")
                    print()
                    sys.exit(1)
                function = "dir"
            elif not os.path.exists(argument):
                print(" No such file or directory.")
                print()
                sys.exit(1)
            else:
                print(" Unkown error. Argument may not be a regular file or directory. Try again")
                print()
                sys.exit(1)
            dmremover(argument, function)
        elif function == "--about":
            about()
        elif function == "--search":
            if not len(sys.argv) > 2:
                print(" First argument after --search should be the filename to search.\nSecond can be list of extensions seperated by comma and space in quotation.\n* is \"any character\"")
                print()
                sys.exit(1)
            name = str(sys.argv[2])
            name = name.replace("*", ".*")
            if len(sys.argv) > 3:
                extensions = sys.argv[3]
                extensions = extensions.split(", ")
                extensions = [ext.replace("*", ".*") for ext in extensions]
            else:
                extensions = None
            search(name, extensions)
        elif function == "--filename":
            if not len(sys.argv) > 2:
                print(" First argument after --filename should be the filename to download.")
                print()
                sys.exit(1)
            file = str(sys.argv[2])
            filename(file)
            
        elif function == "--changename":
            if not len(sys.argv) > 2:
                print(" First argument after --change-name should be the directory of jar files.")
                print()
                sys.exit(1)
            directory = str(sys.argv[2])
            changename(directory)
        elif function == "--help":
            help_f()
    else:
        while True:
            menu()
            clean()
