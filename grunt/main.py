"""
This file is part of the grunt module project
It is where the application starts.

Author: R. Thomas
Place: Sheffield UK
Year: 2025
version: 25.1.1

changelog:
----------
25.1.1 : RTh - Creation of the file
"""

####Standard Library
import sys

####Local imports
from . import cli
from . import download_data

def main():
    '''
    This is the main function
    '''

    ##1st we use the command line interface to look at potential
    ##arguments
    args = cli.command_line_interface(sys.argv[1:])

    if args['download']:
        download_data.download()

    elif args['yearcal']:
        print(f"Making calendar plot for {args['yearcal']}")

    else:
        print('Nothing to do....exit...')
        sys.exit()
