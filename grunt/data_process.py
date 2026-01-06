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


def create_data_calendar(data, parameter, year):
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
    '''
    #Check that the parameter exists
    if parameter not in list(data):
        print('Parameter not in data')
        return numpy.array([]), numpy.array([])

    ##çreate the date range
    start = datetime.strptime(year+"-01-01", "%Y-%m-%d").date()
    end = datetime.strptime(year+"-12-31", "%Y-%m-%d").date()
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
                value = numpy.log(sum(activities[parameter]))
                total += sum(activities[parameter])
                average.append(sum(activities[parameter]))

            elif parameter in ['pace', 'hr']:
                value = numpy.mean(activities[parameter])
                average.append(activities[parameter])

        ##assign the value in the parameter data array
        parameter_data[i] = value

    return date_range, parameter_data, total, numpy.mean(average)
