import sys

from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint 
from pyfiglet import figlet_format

#Fonts starwars, slant, isometric1

cprint(figlet_format('missile!', font='isometric1', width = 100 ),
       'yellow', 'on_red', attrs=['bold'])
