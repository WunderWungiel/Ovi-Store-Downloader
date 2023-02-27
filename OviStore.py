#!/usr/bin/python3

import re
import sys
import os
import sys
import subprocess
from colorama import init, Fore, Style
functions = os.path.dirname(os.path.abspath(__file__)) + "/functions"
sys.path.insert(0, functions)
from id_f import id_f
from search import search
from cdn import cdn
from help_f import help_f
from changename import changename
from dmremover import dmremover
from filename import filename
#Supported extensions

sup_extensions = ["sis", "sisx", "sis.dm", "sisx.dm", "deb", "jar", "wgz", "gif.dm", "mp4.dm", "3gp.dm", "3gp", "jpg"]

#Supported arguments

functions = ["--cdn", "--id", "--help", "--search", "--about", "--changename", "--removedm", "--filename"]

def clean():
    subprocess.call('cls' if os.name == "nt" else "clear", shell=True)
    return

ls = os.listdir

def about():
    clean()
    print(""" 
 ###############################################################
 ###############################################################
 #######                                                 #######
 #######         Made with love by Wunder Wungiel.       #######
 #######                                                 #######
 #######         Website: http://wunderwungiel.pl        #######
 #######         Telegram: https://t.me/WunderW_PL       #######
 #######         Mail: dredlok706@yandex.com             #######
 #######                                                 #######
 ###############################################################
 ###############################################################
 """)
    return

############################
############################
#Non-interactive mode script
############################
############################

if len(sys.argv) > 1:
    
    #Script info

    print()
    print(" ################################################################")
    print(" ################################################################")
    print(" ################ Universal Ovi Store downloader ################")
    print(" ################################################################")
    print(" ####################### By Wunder Wungiel ######################")
    print(" ################################################################")
    print(" ################################################################")
    print()

    #Get first argument from command
    
    function = sys.argv[1]
    
    #If argument not supported
    
    if not function in functions:
        print(" First argument is wrong! See --help.")
        print()
        sys.exit(1)
    
    #ID argument

    if function == "--id":
        if not len(sys.argv) > 2:
            print(" First argument after --id argument should be the minimal ID for search")
            print()
            sys.exit(1)
        #Get arguments and integer them
        arg1 = sys.argv[2]
        arg1 = int(arg1)
        if not len(sys.argv) > 3:
            arg2 = arg1 + 1
        else:
            #If second ID exists
            arg2 = sys.argv[3]
            arg2 = int[arg2]
        id(arg1, arg2)
    
    #CDN argument

    elif function == "--cdn":
        if not len(sys.argv) > 2:
            print(" First argument after --cdn should be the extension to search.")
            print()
            sys.exit(1)
        ext = str(sys.argv[2])
        #Check if extension is supported
        if ext not in sup_extensions:
            print(" Wrong extension!")
            #print list of exts
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
    #Search argument
    elif function == "--about":
        about()
    elif function == "--search":
        if not len(sys.argv) > 2:
            print(" First argument after --search should be the filename to search.\nSecond can be list of extensions seperated by comma and space in quotation.\n* is \"any character\"")
            print()
            sys.exit(1)
        #Get name from command
        name = str(sys.argv[2])
        #Replace * with .* for RegEx
        name = name.replace("""*""", """.*""")
        if len(sys.argv) > 3:
            extensions = sys.argv[3]
            #Create list of extensions
            extensions = extensions.split(", ")
            extensions = [ext.replace("""*""", """.*""") for ext in extensions]
        else:
            extensions = None
        search(name, extensions)
    elif function == "--filename":
        if not len(sys.argv) > 2:
            print(" First argument after --filename should be the filename to download.")
            print()
            sys.exit(1)
        #Get name from command
        file = str(sys.argv[2])
        filename(file)
    
    #change name argument, WIP
        
    elif function == "--changename":
        if not len(sys.argv) > 2:
            print(" First argument after --change-name should be the directory of jar files.")
            print()
            sys.exit(1)
        #Get two arguments
        directory = str(sys.argv[2])
        changename(directory)
    #print help
    elif function == "--help":
        help_f()

########################
########################
#Interactive mode script
########################
########################

else:
    #To display menu always
    while True:
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
        
        #Selecting function
        while True:
            function = input(" ")
            if re.search("\d+", function):
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
        
        #first option

        if function == 1:
            print(" Picking ID function. Type ID of app you'd like to download, or two IDs to take a range of IDs of apps.")
            print()
            #loop for checking ID
            while True:
                args = input(" ")
                if not re.search("\d+", args):
                    print("\n You didn't provide ID(s). Try again.\n")
                else:
                    break
            #If second ID not provided
            if not re.search("\d+\s+(\d+)", args):
                arg1 = re.search("(\d+)\s*", args)
                arg1 = arg1[0]
                arg1 = int(arg1)
                arg2 = arg1 + 1
            #If second ID provided
            else:
                arg1 = re.search("(\d+)\s+", args)
                arg1 = arg1[0]
                arg1 = int(arg1)
                arg2 = re.search("\s+(\d+)", args)
                arg2 = arg2[0]
                arg2 = int(arg2)
            print()
            id_f(arg1, arg2)
        
        #search function

        elif function == 2:
            print(" Picking Search function. Type name of app / game you'd like to search to.")
            print()
            #loop for checking name
            while True:
                name = input(" ")
                if not name:
                    print(" You didn't provide app / game name. Try again.")
                    print()
                else:
                    break
            #replace * with .*
            print()
            print(" I will search for \"" + name + "\". Do you want to filter results by extension(s)? If yes, type them by comma and space. Else, press Enter.")
            print()
            name = name.replace("""*""", """.*""")
            extensions = input(" ")
            if extensions:  
                #make list
                extensions = extensions.split(", ")
                #replace * with .* again
                extensions = [ext.replace("""*""", """.*""") for ext in extensions]
                print()
            else:
                extensions = None
            search(name, extensions)
        
        #cdn function

        elif function == 3:
            print(" Picking CDN function. Type extension of apps you want to find end with.")
            print()
            #loop to check extension
            while True:
                ext = input(" ")
                if not ext:
                    print()
                    print(" You didn't provide extension, try again!")
                    print()
                    continue
                if ext not in sup_extensions:
                    print()
                    print(" This extension isn't supported. Use Help to show supported extensions.")
                    print()
                    continue
                break
            print()
            cdn(ext)
        elif function == 4:
            print(" Picking Name Changer function. Type directory with files, which names need to be changed.")
            print()
            while True:
                directory = input(" ")
                if not os.path.exists(directory):
                    print()
                    print(" Invalid directory!")
                    print()
                    continue
                break
            changename(directory)
        elif function == 5:
            print(" Picking DM remover function. Type directory with files, which names need to be changed OR name / path of ONE file.")
            print()
            while True:
                argument = input(" ")
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
            print(" Picking Filename function. Type name of file you'd like to search to.")
            print()
            #loop for checking name
            while True:
                file = input(" ")
                if not file:
                    print(" You didn't provide filename. Try again.")
                    print()
                else:
                    break
            filename(file)
        elif function == 7:
            #print help
            help_f()
        elif function == 8:
            about()
            input(" Press Enter to return...")
        elif function == 9:
            #close script
            sys.exit(0)
        #clear console window
        clean()

sys.exit(0)