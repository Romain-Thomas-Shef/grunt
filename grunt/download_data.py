"""
This file is part of the grunt module 
the download of the data


Author: R. Thomas
Place: Sheffield, UK
Year: 2025
"""

###Python standard library
import datetime
import os

##Third party
import numpy
from tqdm import tqdm
import pandas
from garminconnect import Garmin

##Local imports

def download(conf):
    '''
    This function download all the data from garmin connect
    it will save them in a txt file call stats.csv.
    If a file already exists, we will just append to the end of the file for additional entries

    Parameters
    -----------
    conf    :   dictionary
                with configuration [just the 'Data' part]

    Returns
    -------
    none
    '''
    #Get today
    today = datetime.datetime.today()

    ##connect to garmin
    tokenstore = os.getenv("GARMINTOKENS") or "~/.garminconnect"
    garmin = Garmin()
    garmin.login(tokenstore)

    ##check if a file exist
    if os.path.isfile('stats.csv'):
        print('\nFound already a stats.csv file...check for last date')
        data = pandas.read_csv('stats.csv', parse_dates=['date'])
        ##And get the last date in the file
        past = data['date'].iloc[-1].date() + datetime.timedelta(days=1)
        ###open the file
        f = open('stats.csv', 'a', encoding="utf-8")
    else:
        ##We download the last X years (x given in the configuration)
        past = today - datetime.timedelta(days=int(conf['yearsback'])*365)

        ###open the file and create the header#
        f = open('stats.csv', 'a', encoding="utf-8")
        f.write('date,runtype,distance,duration,pace,elevation,calories,hr,eventtype\n')

    ###if the last day is different from today...
    if past != today:
        print('\nCreate/Append to stats.csv file....this may take a while...for the first download')

        ###Get all dates
        alldates = numpy.arange(past, today+datetime.timedelta(days=1),
                                datetime.timedelta(days=1)).astype(datetime.datetime)

        for d in tqdm(alldates):
            ##get the activities for that date
            activities = garmin.get_activities_by_date(startdate=str(d.date()), enddate=str(d.date()))
            for i in activities:
                ##only get the running activities
                if i['activityType']['typeKey'] in conf['runtype'].split(','):

                    ####Get all the useful data from the activity
                    runtype = i['activityType']['typeKey']
                    daterun = i['startTimeLocal'].split(' ')[0]
                    distance = round(i['distance']/1000, 2) #garmin in meter, we change to km
                    if 'movingDuration' in i.keys():
                        duration = round(i['movingDuration'], 2) ##in s
                    else:
                        duration = round(i['duration'], 2) ##in s
                    if 'elevationGain' in i.keys():
                        elevation = round(i['elevationGain'], 2) #in m
                    else:
                        elevation = 0
                    calories = i['calories']
                    pace = round(60/(i[ 'averageSpeed']*3.6), 2) ##in m/s, change to min/km (pace)
                    if 'averageHR' in i.keys():
                        hr = i['averageHR']
                    else:
                        hr = str(numpy.nan)
                    eventtype = i['eventType']['typeKey']
                    ###create the line and write it to file
                    line = f'{daterun},{runtype},{distance},{duration},{pace},{elevation},{calories},{hr},{eventtype}\n'
                    f.write(line)

        f.close()
