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
import os

####Third party

####Local imports
from . import cli
from . import download_data
from . import data_process
from . import plots

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

        ###check if file exists
        if not os.path.isfile('stats.csv'):
            question = input('File stats.csv not found in working directory'+
                             '..do you want to create one?[y/n]')
            if question in ['y', 'Y', 'yes']:
                download_data.download()
            else:
                print('Data not found and not created...exit...')
                sys.exit()

        ###load the data
        dates, values,\
               total, average = data_process.create_data_calendar(data_process.load_data_csv('stats.csv'),
                                                                  'distance', args['yearcal'])
        ###make the calendar
        plots.create_calendar(dates, values,
                              f"{args['yearcal']}, Current total {round(total, 2)} km; average run length = {round(average,2)} km/day", False)

    else:
        print('Nothing to do....exit...')
        sys.exit()
