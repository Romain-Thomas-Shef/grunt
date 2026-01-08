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
from .load_conf import load

def main():
    '''
    This is the main function
    '''

    ##1st we use the command line interface to look at potential
    ##arguments
    args = cli.command_line_interface(sys.argv[1:])

    ##check configuration
    if args['conf'] is None:
        print('No configuration file found, using default...')
        conffile = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'conf_default.txt')

    else:
        if os.path.isfile(args['conf']):
            conffile = args['conf']
            print('Configuration file found...continue')
        else:
            print('Configuration file not found...exit')
            sys.exit()

    ##and load it
    conf = load(conffile)

    ###Then analyse each argument
    if args['download']:
        download_data.download(conf['Data'])

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
        ###see if we save the plot
        save = False
        if args['save']:
            save = True

        ###make the calendar
        title = f"{args['yearcal']}, Current total {round(total, 2)} km; average run length = {round(average,2)} km"
        filename = f"calendar_{args['yearcal']}.png"
        plots.create_calendar(dates, values, title, save, conf, filename)

    else:
        print('Nothing to do....exit...')
        sys.exit()
