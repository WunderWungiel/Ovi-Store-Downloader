from colorama import init, Fore, Style
from .clean import clean

def help_f():
    clean()
    print(f""" {Fore.CYAN}This script works using Wayback Machine APIs and use its snapshots.{Style.RESET_ALL}

 Available commands:

 {Fore.LIGHTGREEN_EX}--help{Style.RESET_ALL} - print this message

 {Fore.LIGHTGREEN_EX}--search{Style.RESET_ALL} {Fore.BLUE}<\"filename / app name\"> <\"extensions seperated by comma\">{Style.RESET_ALL} - search for apps in Ovi Store's archive database. * for any character. For example:
 
 {Fore.GREEN}./ovistore.py --search "opera*" "sis*, deb":{Style.RESET_ALL}
 
 searches for files with \"opera\" word in, after that word any characters and with extensions: sis, sisx, sis.dm, sisx.dm and deb.

 {Fore.LIGHTGREEN_EX}--cdn{Style.RESET_ALL} {Fore.BLUE}<extension>{Style.RESET_ALL} - download from Ovi Store \"CDN\" (d.ovi.com). {Fore.BLUE}<extension>{Style.RESET_ALL} is the extension of files to download.
 Currently supported: sis, sisx, sis.dm, sisx.dm, deb, jar, wgz, gif.dm, mp4.dm, 3gp.dm, 3gp.{Style.RESET_ALL}

 {Fore.LIGHTGREEN_EX}--content {Style.RESET_ALL}{Fore.BLUE}<min_id> <max_id>{Style.RESET_ALL} - download using apps ID (loop through range of IDs you've provided. {Fore.RED}Very slow and hungry!{Style.RESET_ALL} If you import one ID, it will download one app with this ID.

 {Fore.LIGHTGREEN_EX}--filename {Style.RESET_ALL}{Fore.BLUE}<filename>{Style.RESET_ALL} - download file with provided filename.

 {Fore.LIGHTGREEN_EX}--removedm {Style.RESET_ALL}{Fore.BLUE}<directory / filename>{Style.RESET_ALL} - removes DM from files (sisx.dm, sis.dm, 3gp.dm, mp4.dm, gif.dm).

 Wayback Machine often refuses connection after many requests. You will be notified about such case with a bunch of errors, you need to retry then.
 Sorry :(""")
    print()
    input(" Press Enter to return...")
    return
