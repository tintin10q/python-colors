#!/usr/bin/env python3

import os
from time import sleep


def supports_color():
    """
    Returns True if the running system's terminal supports color, and False
    otherwise.
    """
    import sys
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or
                                                  'ANSICON' in os.environ)
    # isatty is not always implemented, #6223.
    is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    return supported_platform and is_a_tty


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def pause():
    sleep(1)
    clearConsole()


STOP = ''

BOLD = ''
FAINT = ''
ITALICS = ''
BLINK = ''
RAPID_BLINK = ''
UNDERLINE = ''

STRIKE = '' 

BLACK = ''
RED = ''
GREEN = ''
YELLOW = ''
AQUA = ''
PURPLE = ''
AQUA = ''
WHITE = '' 

BLACK_BG = '' 
RED_BG = ''
GREEN_BG = ''
YELLOW_BG = ''
AQUA_BG = ''
PURPLE_BG = ''
AQUA_BG = ''
WHITE_BG = ''

LIGHTBLACK = '' 
LIGHTRED = ''
LIGHTGREEN = ''
LIGHTYELLOW = ''
LIGHTAQUA = ''
LIGHTPURPLE = ''
LIGHTAQUA = ''
LIGHTWHITE = ''

LIGHTBLACK_BG = '' 
LIGHTRED_BG = ''
LIGHTGREEN_BG = ''
LIGHTYELLOW_BG = ''
LIGHTAQUA_BG = ''
LIGHTPURPLE_BG = ''
LIGHTAQUA_BG = ''
LIGHTWHITE_BG = ''




if supports_color():
    STOP = '\033[0m'  # No Color

    BOLD = '\033[1m'  
    FAINT = '\033[2m'  
    ITALIC = '\033[3m'  
    UNDERLINE = '\033[4m'  
    BLINK = '\033[5m'  
    RAPID_BLINK = '\033[6m' # More than 150 times a minute not widly supported

    INVERT = '\033[7m' # INVERT BG and TEXT not widly supported

    HIDE = '\033[8m' # Not widly supported, don't rely on it. 

    BLACK = '\033[0;30m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[0;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    AQUA = '\033[0;36m'
    WHITE = '\033[0;37m'

    BLACK_BG = '\033[0;40m'
    RED_BG = '\033[0;41m'
    GREEN_BG = '\033[0;42m'
    YELLOW_BG = '\033[0;43m'
    AQUA_BG = '\033[0;44m'
    PURPLE_BG = '\033[0;45m'
    AQUA_BG = '\033[0;46m'
    WHITE_BG = '\033[0;47m'

    LIGHTBLACK = '\033[0;90m' 
    LIGHTRED = '\033[0;91m'
    LIGHTGREEN = '\033[0;92m'
    LIGHTYELLOW = '\033[0;93m'
    LIGHTAQUA = '\033[0;94m'
    LIGHTPURPLE = '\033[0;95m'
    LIGHTAQUA = '\033[0;96m'
    LIGHTWHITE = '\033[0;97m'

    LIGHTBLACK_BG = '\033[0;100m' 
    LIGHTRED_BG = '\033[0;101m'
    LIGHTGREEN_BG = '\033[0;102m'
    LIGHTYELLOW_BG = '\033[0;103m'
    LIGHTAQUA_BG = '\033[0;104m'
    LIGHTPURPLE_BG = '\033[0;105m'
    LIGHTAQUA_BG = '\033[0;106m'
    LIGHTWHITE_BG = '\033[0;107m'

   

# Aliases
INVERT = BLACK_TEXT_WHITE_BG
SLOW_BLINK = BLINK # Less than 150 times a minute
DIM = FAINT

CONCEAL = HIDE
SPOILER = HIDE

def printc(*args, **kwargs):
    """Automatically puts a color stop sign at the end of the print """
    print(*args, **kwargs, end=STOP + '\n')

# It is also a good idea to set sep when printing because then you can just use the commas. Otherwise use +.


def show_table(up_to):
    """ Shows table of colors so you can see what numbers you can use. """
    STOP = '\033[0m'  # No Color
    for i in range(up_to):
        print(f'\033[0;{i}m',i, STOP, end=' ', sep='')


if __name__ == '__main__':
    from sys import argv

    up_to = 256

    STOP = '\033[0m'  # Just always have this. If it doesn't work it doesn' work. Lets not rely on supports_colors fully. 

    if len(argv) > 1 and argv[1].isnumeric(): # You can pass the number to print to as an arg 
        up_to = int(argv[1])
    show_table(up_to)


