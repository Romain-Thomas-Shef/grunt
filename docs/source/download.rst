Download data
=============

.. note:: Before getting started with GRUNT you need to give your computer access to Garmin. To do this I am using `python_garminconnect <https://github.com/cyberjunky/python-garminconnect>`_. At the time of writing I am using v0.2.38.

In order to visualise your data on plots you need to download the data. This is very easy and can be done with the command line interface (see :doc:`get_started`). The command to make this download is:

.. code-block:: text

    user@machine % grunt --download

The number of years and run types that it will go back depends on what you have in the configuration file. Two parameters are controlling this:

.. code-block:: test
    
    [Data]
    yearsback = 10
    runtype = ultra_run,treadmill_running,trail_running,running 

* ``yearsback`` controls the number of years you wanna download.
* ``runtype`` controls the run types you wanna download. By default it is all the Garmin available runtypes. 

.. warning:: 

    During the first downloads, it will take time to make build the final file. Especially if you are downloading a lot of years worth of data. A progress bar will indicate you the status of the download.


For each downloaded run, the following data will be recorded:

* ``date``: date of the run (*startTimeLocal* in Garmin)
* ``runtype``: type of run (*activityType* in Garmin)
* ``distance``: in km (*distance* in Garmin, converted to km)
* ``duration``: in second 
* ``elevation``: in meter (*elevationGain* in Garmin)
* ``pace``: in min/km. Note that for a pace of 5.9, you must read, 5 min and 0.9 x 1 minute. It corresponds the *averageSpeed* in Garmin.Garmin gives it in m/s, we convert it to min/km.
* ``calories``: same in Garmim
* ``hr``: average heartrate (*averageHR* in Garmin)
* ``eventtype``: same in Garmin. 

After download, a ``stats.csv`` is available and you can read it with any text editor. It will look like this: 


.. code-block:: text

    date,runtype,distance,duration,pace,elevation,calories,hr,eventtype
    2019-02-01,treadmill_running,10.0,3590.0,6.04,0,851.0,147.0,uncategorized
    2019-02-02,treadmill_running,8.01,2799.0,5.91,0,639.0,142.0,uncategorized
    2019-02-03,treadmill_running,10.02,3403.0,5.94,0,806.0,144.0,uncategorized
    2019-02-05,treadmill_running,7.01,2294.0,5.82,0,505.0,143.0,uncategorized
    2019-02-06,treadmill_running,5.26,1720.0,5.78,0,381.0,145.0,uncategorized
    2019-02-12,treadmill_running,10.25,3409.0,5.85,0,721.0,143.0,uncategorized
    2019-02-17,running,10.13,3465.56,5.73,68.0,713.0,143.0,uncategorized
    2019-02-24,running,5.89,2041.0,5.82,42.0,466.0,150.0,uncategorized
    2019-02-27,running,10.62,3541.13,5.76,79.0,764.0,145.0,uncategorized
    2019-03-02,running,14.26,4902.27,5.92,119.0,1115.0,152.0,uncategorized
    2019-03-03,running,7.77,2557.72,5.66,64.0,561.0,147.0,uncategorized
    2019-03-16,treadmill_running,5.01,1820.0,6.48,0,428.0,148.0,uncategorized
    2019-03-17,treadmill_running,6.65,2302.0,6.12,0,526.0,147.0,uncategorized
    2019-03-18,treadmill_running,8.01,2781.0,6.1,0,629.0,147.0,uncategorized
    2019-03-20,treadmill_running,9.58,3251.0,5.93,0,697.0,143.0,uncategorized
    2020-03-21,treadmill_running,11.01,3777.54,6.01,0,892.0,153.0,uncategorized
    2020-03-23,treadmill_running,9.51,3109.0,5.79,0,647.0,140.0,uncategorized
    2020-03-24,treadmill_running,8.01,2586.0,5.75,0,485.0,133.0,uncategorized
    2022-04-24,running,21.15,6967.19,5.5,85.0,1709.0,166.0,race
