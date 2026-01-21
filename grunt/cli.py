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
    parser.add_argument('--yearcal', type=str,
                        help='The year you want the calendar for, default is current year')
    parser.add_argument('--compare_distance',
                        action='store_true',
                        help='Will compare the distance for all the years available in the data')
    parser.add_argument('--conf', type=str,
                                  help='Configuration file, if not used, GRUNT will use default')
    parser.add_argument('--runtypes', nargs='?', help='Run types histograms', const='current')
    parser.add_argument('--save', action='store_true',
                        help='Instead of showing the plot,'+\
                             'it will be saved (need a custom conf file)')

    ###analyse the arguments
    parsed = vars(parser.parse_args(args))

    return parsed
