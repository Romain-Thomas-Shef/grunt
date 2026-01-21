"""
This file is part of the grunt module 
Data loading and processing 

Author: R. Thomas
Place: Sheffield, UK
Year: 2025
"""

###Python standard library
from datetime import datetime, timedelta

##Third party
import pandas
import numpy

##Local imports


def load_data_csv(file):
    '''
    This simple function loads the csv datafile

    Parameter
    ---------
    file    :   str
                path of the csv file
    
    return
    ------
    data    :   panda dataframe
                loaded data
    '''
    ##We assume that the files exists. A check must be done before!
    data = pandas.read_csv(file, parse_dates=['date'])

    return data


def create_data_calendar(data, parameter, year, log=True, cut=False):
    '''
    This function creates to array:
        - one for dates
        - one for the parameter for each date

    Parameter:
    ----------
    data    :   panda dataframe
                data from stats.csv
    parameter:  str
                parameter to plot in the calendar
    year    :   str
                year to consider
    log     :   bool
                to use a logarithmic scale
    cut     :   bool
                if we cut the last year at today's date
    '''
    #Check that the parameter exists
    if parameter not in list(data):
        print('Parameter not in data')
        return numpy.array([]), numpy.array([])

    ##çreate the date range
    start = datetime.strptime(year+"-01-01", "%Y-%m-%d").date()
    end = datetime.strptime(year+"-12-31", "%Y-%m-%d").date()

    if cut is True and end>datetime.today().date():
        end = datetime.today().date()

    date_range = numpy.arange(start, end, timedelta(days=1)).astype(datetime)

    ##create the correspondionog array for the data
    parameter_data = numpy.zeros(len(date_range))

    ##total
    total = 0
    average = []

    ##select from data
    for i,d in enumerate(date_range):
        activities = data.loc[(data['date'] == pandas.Timestamp(d))]
        value = 0
        if activities.shape[0]>0: #Check number of rows
            if parameter in ['distance', 'calories', 'duration', 'elevation']:
                if log:
                    value = numpy.log(sum(activities[parameter]))
                else:
                    value = sum(activities[parameter])
                total += sum(activities[parameter])
                average.append(sum(activities[parameter]))

            elif parameter in ['pace', 'hr']:
                value = numpy.mean(activities[parameter])
                average.append(activities[parameter])

        ##assign the value in the parameter data array
        parameter_data[i] = value

    return date_range, parameter_data, total, numpy.mean(average)


def get_years_available(data):
    '''
    From a list-like of dates, find which years it is
    spanning.

    Parameters
    ----------
    data   :   data frame 
               with the 'date' column

    Return
    ------
    years   :   list
                of years (as str)
    '''
    ###get oldest and latest date
    first_year = min(data['date']).date().year
    last_year = max(data['date']).date().year

    ###create the full list of year
    years = [first_year]
    i = first_year
    while i<last_year:
        i += 1
        years.append(i)

    return years


def overlap_year(year, requested_year=2020):
    '''
    Take a list of dates and change the year bit
    to the requested one

    Parameter
    ---------
    year    :   lsit
                of dates
    requested_year: int
                    year to change from
    '''
    newyear = []
    for i in year:
        newyear.append(i.replace(year=int(requested_year)))

    return newyear


def get_runtypes(data, year, conf):
    '''
    Takes the list of dates, and create the
    dictonary of dates / runtypes

    Parameter
    ---------
    data    :   panda dataframe
                with dates and runtypes columns

    years   :   int
                year
                
    conf    :   dict
                configuration file

    return
    ------
    runtypes    :   nested dict
                    {year: {runtype1: X, runtype2: Y}, year2: (runtype1: XX, runtype2: YY)....}

    '''

    ##çreate the date range
    start = datetime.strptime(str(year)+"-01-01", "%Y-%m-%d").date()
    end = datetime.strptime(str(year)+"-12-31", "%Y-%m-%d").date()

    ##date_range
    date_range = numpy.arange(start, end, timedelta(days=1)).astype(datetime)

    ##Prepare the dictionary
    alltypes = conf['Data']['runtype'].split(',')
    dict_runtype = dict.fromkeys(alltypes, 0)

    ##select from data
    for i,d in enumerate(date_range):
        del i
        activities = data.loc[(data['date'] == pandas.Timestamp(d))]
        if activities.shape[0]>0: #Check number of rows
            for run in activities['runtype'].values:
                dict_runtype[run] += 1

    return dict_runtype
