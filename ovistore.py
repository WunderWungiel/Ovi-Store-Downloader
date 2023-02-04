#!/usr/bin/python3
import requests
import re
import sys
import time
import os
import sys
sys.path.insert(0, 'functions')
from changename import change_name
from id_f import id_f
from search import search
from cdn import cdn
from help_f import help_f
from colorama import init, Fore, Style

extensions = ["sis", "sisx", "sis.dm", "sisx.dm", "deb", "jar", "wgz", "gif.dm", "mp4.dm", "3gp.dm", "3gp", "jpg"]

functions = ["--cdn", "--id", "--help", "--change-name", "--search" ]

if len(sys.argv) > 1:
    print()
    print(" ################################################################")
    print(" ################################################################")
    print(" ################ Universal Ovi Store downloader ################")
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
        if ext not in extensions:
            print(" Wrong extension!")
            print(" Allowed extensions (for now): " + ", ".join(str(item) for item in extensions))
            print()
            sys.exit(1)
        print(f" Picking *.{ext} extension.")
        print()
        cdn(ext)

    elif function == "--search":
        if not len(sys.argv) > 2:
            print(" First argument after --search should be the filename to search.\nSecond can be list of extensions seperated by comma and space in quotation.\n* is \"any character\"")
            print()
            sys.exit(1)
        name = str(sys.argv[2])
        name = name.replace("""*""", """.*""")
        if len(sys.argv) > 3:
            extensions = sys.argv[3]
            extensions = extensions.split(", ")
            extensions = [ext.replace("""*""", """.*""") for ext in extensions]
        else:
            extensions = None
        search(name, extensions)
    elif function == "--change-name":
        if not len(sys.argv) > 2:
            print(" First argument after --change-name should be the directory of jar files.")
            print()
            sys.exit(1)
        if not len(sys.argv) > 3:
            print(" First argument after --change-name should be the extension of files to change names of.")
            print()
            sys.exit(1)
        directory = str(sys.argv[2])
        extension = str(sys.argv[3])
        change_name(directory, extension)

    elif function == "--help":
        help_f()

else:
    print()
    print(" ##############################################################################")
    print(" #########                                                            #########")
    print(" #########               Universal Ovi Store downloader               #########")
    print(" ######### ---------------------------------------------------------- #########")
    print(" #########           Browse archived Ovi Store more easily!           #########")
    print(" ######### ---------------------------------------------------------- #########")
    print(" #########                                                            #########")
    print(" #########                    Choose an option:                       #########")
    print(" #########                                                            #########")
    print(" #########     1) Download app(s) using ID  |  2) Search for apps     #########")
    print(" #########     3) Download apps with specific extension               #########")
    print(" #########     4) Print help  |  5) Exit                              #########")
    print(" #########                                                            #########")
    print(" ##############################################################################")
    print()

    while True:
        function = input(" ")
        function = int(function)
        if function not in range(1, 6):
            print("\n Wrong option! Type correct number.\n")
        else:
            break
    print()

    if function == 1:
        print(" Picking ID function. Type ID of app you'd like to download, or two IDs to take a range of IDs of apps.")
        print()
        while True:
            args = input(" ")
            if not re.search("\d+", args):
                print()
                print(" You didn't provide ID(s). Try again.")
                print()
            else:
                break
        if not re.search("\d+\s+(\d+)", args):
            arg1 = re.search("(\d+)\s*", args)
            arg1 = arg1[0]
            arg1 = int(arg1)
            arg2 = arg1 + 1
        else:
            arg1 = re.search("(\d+)\s+", args)
            arg1 = arg1[0]
            arg1 = int(arg1)
            arg2 = re.search("\s+(\d+)", args)
            arg2 = arg2[0]
            arg2 = int(arg2)
        print()
        id_f(arg1, arg2)
    
    elif function == 2:
        print(" Picking Search function. Type name of app / game you'd like to search to.")
        print()
        while True:
            name = input(" ")
            if not name:
                print(" You didn't provide app / game name. Try again.")
                print()
            else:
                break
        name = name.replace("""*""", """.*""")
        print()
        print(" I will search for \"" + name + "\". Do you want to filter results by extension(s)? If yes, type them by comma and space. Else, press Enter.")
        print()
        extensions = input(" ")
        if extensions:
            extensions = extensions.split(", ")
            extensions = [ext.replace("""*""", """.*""") for ext in extensions]
        else:
            extensions = None
        print()
        search(name, extensions)

    elif function == 3:
        print(" Picking CDN function. Type extension of apps you want to find end with.")
        print()
        while True:
            ext = input(" ")
            if not ext:
                print()
                print(" You didn't provide extension, try again!")
                print()
                continue
            if ext not in extensions:
                print()
                print(" This extension isn't supported. Use Help to show supported extensions.")
                print()
                continue
            break
        print()
        cdn(ext)
    elif function == 4:
        help_f()
    elif function == 5:
        sys.exit(0)

sys.exit(0)