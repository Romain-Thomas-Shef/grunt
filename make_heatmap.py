import july
import os
from july.utils import date_range
import matplotlib.pyplot as plt
import numpy
import pandas
from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)
import datetime


year = '25'

dates = date_range("20"+year+"-01-01", "20"+year+"-12-31")
data = numpy.zeros(len(dates))
elevation = numpy.zeros(len(dates))
pace = numpy.zeros(len(dates))
speed = numpy.zeros(len(dates))
calories = numpy.zeros(len(dates))
duration = numpy.zeros(len(dates))
averageHR = numpy.zeros(len(dates))
steps_per_min = numpy.zeros(len(dates))


##login to garmin
tokenstore = os.getenv("GARMINTOKENS") or "~/.garminconnect"
garmin = Garmin()
garmin.login(tokenstore)
test = garmin.get_last_activity()
print(test['activityType']['typeKey'])

##load garmin files
#garmin = pandas.read_csv('Activities.csv', parse_dates=['Date'])


##process the data
for d,km in zip(dates, range(len(data))):
    date1 = str(d)
    date2 = str(d + pandas.Timedelta(days=1))
    test = garmin.get_activities_by_date(startdate=date1, enddate=date1)    
    paceindiv = []
    HRindiv = []
    spm_indiv = []
    for i in test:
        if i['activityType']['typeKey'] in ['running', 'trail_running', 'treadmill_running', 'ultra_run']:
            print(date1, i['activityType']['typeKey'], float(i['distance'])/1000, i['startTimeLocal'])
            elevation[km] += float(i['elevationGain'])# in m 
            data[km] += float(i['distance'])/1000 ##converted to km
            duration[km] += float(i['movingDuration']) #in s
            calories[km] += float(i['calories'])
            #paceindiv.append(i[''])
            spm_indiv.append(i['averageRunningCadenceInStepsPerMinute'])
            HRindiv.append(i['averageHR'])
            speed = 60/(i['averageSpeed']*3.6) #given in m/s by garmin. Move to km/h and then to min/km.
            paceindiv.append(speed) #in km/hr (given in m/s by garmin)
    
    if data[km]>0:
        data[km] = numpy.log(data[km])
    
    """
    activities = garmin.loc[(garmin['Date'] >= pandas.Timestamp(date1)) & \
                  (garmin['Date'] <  pandas.Timestamp(date2))]
    if len(activities)>0:
        for i,act in activities.iterrows():
            data[km] += float(act['Distance'].replace(',', '.'))
            print(act['Date'], act['Distance'], km, data[km])
        if data[km]>0:
            data[km] = numpy.log(data[km]) 
    """
totalkm = sum(numpy.exp(data))
    
###pre-processing
plot, fig = july.heatmap(dates, data, title='20%s, Current total: %s km'%(year, round(totalkm,1)),
                    cmap="gnuplot", year_label=False)
fig.tight_layout()

plt.show()

