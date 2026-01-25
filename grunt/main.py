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
import datetime

####Third party
import numpy

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

    ###see if we save the plot
    save = False
    if args['save']:
        save = True

    ###Then analyse each argument
    if args['download']:
        download_data.download(conf['Data'])

    elif args['yearcal']:
        print(f"Making calendar plot for {args['yearcal']}")

        load_data()

        ###load the data
        dates, values,\
               total, average = data_process.create_data_calendar(load_data(),
                                                                  'distance', args['yearcal'])
        ###make the calendar
        title = f"{args['yearcal']}, Current total {round(total, 2)} km; average run length = {round(average,2)} km"
        filename = f"calendar_{args['yearcal']}.png"
        plots.create_calendar(dates, values, title, save, conf, filename)


    elif args['compare_distance']:
        print("Making distance plots over the years")

        ##load data
        data = load_data()

        ##get the years
        years = data_process.get_years_available(data)

        ###And corresponding data
        years_km = dict.fromkeys(years)
        for year in years:
            ###load the data
            dates, values, total, \
                   average = data_process.create_data_calendar(data, 'distance', str(year),
                                                               False, cut=True)
            years_km[year] = [data_process.overlap_year(dates, '2020'), numpy.cumsum(values)]

        ##make the plot
        filename = "Compare_distance_year.png"
        plots.compare_year(years_km, 'Cumulative km / year', 'distance [km]', save, conf, filename)


    elif args['runtypes']:
        print("Making runtypes histograms\n")

        ##load data
        data = load_data()

        ##get the years
        if args['runtypes'] == 'current':
            year = datetime.datetime.today().year
        else:
            year = args['runtypes']

        ###get the runtypes
        runtypes = data_process.get_runtypes(data, year, conf)

        ##make the plot
        filename = f"runtype_{year}.png"
        plots.runtypes_hist(runtypes, save, conf, filename)

    elif args['pace'] in ['running', 'trail_running', 'ultra_run', 'treadmill_running', 'all']:
        print(f"Computing {args['pace']} pace evolution\n")

        ##load the data
        data = load_data()

        ###get the runtype
        if args['pace'] == 'all':
            types = ['running', 'trail_running', 'treadmill_running', 'ultra_run']
        else:
            types = [args['pace']]

        #extract the pace for the given run types
        allpaces = data_process.get_allpaces(data, types)

        ###fit a straight line for each type
        allpaces_with_fit = []
        slopes = []
        for typesrun in allpaces:
            newdf, slope = data_process.data_fit_straight(typesrun, 'pace')
            allpaces_with_fit.append(newdf)
            slopes.append(slope)

        ##make the plot
        filename=f"pace_evolution.png"
        plots.pace_scatter(allpaces_with_fit, types,    
                           conf, f'All time pace evolution for different run types', save, filename)

    else:
        print('Nothing to do....exit...')
        sys.exit()

def load_data():
    '''
    This function just loads the file of data
    if it is not found, grunt asks if the user wants to download data.

    Parameter
    ---------
    None

    Return (only if data can be found)
    ------
    data    :   pandas dataframe
                running data
    '''
    ###check if file exists
    if not os.path.isfile('stats.csv'):
        question = input('File stats.csv not found in working directory'+
                         '..do you want to create one?[y/n]')
        if question in ['y', 'Y', 'yes']:
            download_data.download()
        else:
            print('Data not found and not created...exit...')
            sys.exit()

    ##load data
    data = data_process.load_data_csv('stats.csv')

    return data
