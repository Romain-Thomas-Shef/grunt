"""
This file is part of the grunt module 
It codes the command line interface


Author: R. Thomas
Place: Sheffield, UK
Year: 2025
"""

###Python standard library
import argparse

##Third party

##Local imports

def command_line_interface(args):
    '''
    This function defines the command line interface of the program.

    Parameters
    -----------
    args    :   sys.argv
                arguments passed to the interface

    Returns
    -------
    parsed  :   Namespace
                parsed arguments
    '''
    ##create parser object
    parser = argparse.ArgumentParser(description=\
            '------------------------------------------------'+\
            '\n - GRUNT: Garmin RUNning sTatistic'+\
            '\n - Authors: R. Thomas'+\
            '\n - Licence: MIT - '+\
            '\n------------------------------------------------', \
            formatter_class=argparse.RawTextHelpFormatter)

    ###add arguments
    parser.add_argument('--download', action='store_true',
                        help='Get the data from garmin connect')
    parser.add_argument('--yearcal', type=int,
                        help='The year you want the calendar for, default is current year')
    parser.add_argument('--compare_distance',
                        action='store_true',
                        help='Will compare the distance for all the years available in the data')

    ###analyse the arguments
    parsed = vars(parser.parse_args(args))

    return parsed
