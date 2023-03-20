import os
import re
import sys

from .id_f import id_f
from .search import search
from .cdn import cdn
from .help_f import help_f
from .changename import changename
from .dmremover import dmremover
from .filename import filename
from .clean import clean
from .about import about

sup_extensions = ["sis", "sisx", "sis.dm", "sisx.dm", "deb", "jar", "wgz", "gif.dm", "mp4.dm", "3gp.dm", "3gp", "jpg"]
ls = os.listdir

def menu():
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
    print(" #########     4) Name Changer  |  5) DM remover                      #########")
    print(" #########     6) Download using filename  |  7) Print help           #########")
    print(" #########     8) About  |  9) Exit                                   #########")
    print(" #########                                                            #########")
    print(" ##############################################################################")
    print()
        
    while True:
        function = input(" ")
        if function.isnumeric():
            function = int(function)
        else:
            print(" Option should be number from 1 - 9!\n")
            continue
        if function not in range(1, 10):
            print("\n Wrong option! Type correct number.\n")
            continue
        else:
            break
    print()

    if function == 1:
        print(" Type ID of app you'd like to download, or two IDs to take a range of IDs of apps, or 0 to return.")
        print()
        while True:
            args = input(" ")
            if args == "0":
                return
            if not args.isnumeric():
                print("\n You didn't provide ID(s). Try again.\n")
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
        print(" Type name of app / game to search, or press 0 to return to return.")
        print()
        name = input(" ")
        if name == "0":
            return
        print()
        print(" Do you want to filter results by extension(s)? If yes, type them by comma and space. Else, press Enter.")
        print()
        name = name.replace("""*""", """.*""")
        extensions = input(" ")
        if extensions == "0":
            return
        if extensions: 
            extensions = extensions.split(", ")
            extensions = [ext.replace("""*""", """.*""") for ext in extensions]
            print()
        else:
            extensions = None
        search(name, extensions)
        
    elif function == 3:
        print(" Type extension of apps you want to find end with, or press 0 to return to return.")
        print()
        while True:
            ext = input(" ")
            if ext == "0":
                return
            if ext not in sup_extensions:
                print()
                print(" This extension isn't supported. Use Help to show supported extensions.")
                print()
                continue
            break
        print()
        cdn(ext)
    elif function == 4:
        print(" Type directory with files, which names need to be changed, or press 0 to return to return.")
        print()
        while True:
            directory = input(" ")
            if directory == "0":
                return
            if not os.path.exists(directory):
                print()
                print(" Invalid directory!")
                print()
                continue
            break
        changename(directory)
    elif function == 5:
        print(" Type directory with files, which names need to be changed OR name / path of ONE file, or press 0 to return to return.")
        print()
        while True:
            argument = input(" ")
            if argument == "0":
                return
            if os.path.isfile(argument):
                if not argument.endswith(".dm"):
                    print()
                    print(" Filename doesn't end with .dm - try again!")
                    print()
                    continue
                function = "file"
            elif os.path.isdir(argument):
                isdm = False
                for filename in ls(argument):
                    if filename.endswith(".dm"):
                        isdm = True
                        break
                if not isdm:
                    print()
                    print(" No .dm files in specified directory - try again!")
                    print()
                    continue
                function = "dir"
            elif not os.path.exists(argument):
                print()
                print(" No such file or directory.")
                print()
                continue
            else:
                print()
                print(" Unkown error. Argument may not be a regular file or directory. Try again")
                print()
                continue
            break
        dmremover(argument, function)
    elif function == 6:
        print(" Type name of file to download, or press 0 to return to return..")
        print()
        while True:
            file = input(" ")
            if file == "0":
                return
            else:
                break
        filename(file)
    elif function == 7:
        help_f()
    elif function == 8:
        about()
        input(" Press Enter to return...")
    elif function == 9:
        sys.exit(0)