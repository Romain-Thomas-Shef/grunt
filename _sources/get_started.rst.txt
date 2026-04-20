Getting started
===============

Command line interface
----------------------

.. note:: Before getting started with GRUNT you need to give your computer access to Garmin. To do this I am using `python_garminconnect <https://github.com/cyberjunky/python-garminconnect>`_. At the time of writing I am using v0.2.38.

Once installed properly, you can run GRUNT from the terminal. GRUNT comes with a command line interface that you can find using:
 
.. code-block:: text

    user@machine % grunt --help

And this will give:


.. code-block:: text

    usage: grunt [-h] [--download] [--yearcal YEARCAL] [--compare_distance] [--conf CONF] [--runtypes [RUNTYPES]] [--pvd] [--pace [{running,ultra_run,treadmill_running,trail_running,all}]] [--save]

    ------------------------------------------------
     - GRUNT: Garmin RUNning sTatistic
     - Authors: R. Thomas
     - Licence: MIT -
    ------------------------------------------------

    options:
      -h, --help            show this help message and exit
      --conf CONF           Configuration file, if not used, GRUNT will use default
      --download            Get the data from garmin connect
      --save                Instead of showing the plot,it will be saved (need a custom conf file)
      --yearcal YEARCAL     The year you want the calendar for, default is current year
      --compare_distance    Will compare the distance for all the years available in the data
      --runtypes [RUNTYPES]
                            Run types histograms
      --pvd                 All time pace vs distance for all types of run
      --pace [{running,ultra_run,treadmill_running,trail_running,all}]
                            All time pace evolution for a run type (default is running)

In details, there are three categories of arguments:

* Configuration:

  * ``--conf`` + ``file``: This loads your personnal configuration (see below). 

* Data download:

  * ``--download``: this download the latest data from your Garmin profile (see :doc:`download`)

* Plots:

  * ``--save``: can be used with all the other plot arguments. It saves the figure in disk.
  * ``--yearcal`` + ``year``: This creates a calendar of all your runs. Run distance is highlighter via a colormap scheme. 
  * ``--compare_distance``: This will create a plot with one single cumulative distance curve per year. 
  * ``--runtypes``: This will make a histogram of run types. 
  * ``--pvd``: This makes a scatter plot with distance vs pace. Points are color coded based on date. 
  * ``--pace`` + ``runtype``: This creates a scatter plot with pace vs date. Runtype are the one defined by Garmin. You can use these options: ``running``, ``ultra_run``, ``treadmill_running``, ``trail_running``, ``all``. 

Configuration file
------------------

GRUNT needs a configuration file to run. You can find it below and this can be copied to any text file. This is the default configuration that you can of course modify and test. Each section is explained in the rest of the documentation where it makes sense to talk about it.  

.. warning::

    You need to adjust the Directory at the bottom. This is the absolute path. 

.. code-block:: text

    [Data]
    yearsback = 10
    runtype = ultra_run,treadmill_running,trail_running,running

    [Plot_general]
    dpi = 200
    text = 228,223,202
    background = 37,42,52

    [Plot_calendar]
    colormap = gnuplot
    ##Would appreciate if that stays, so GRUNT gets more visibility
    credit = true
    credit_x = 0.90
    credit_y = 0.15

    [Compare_distance_plot]
    ####Compare distance plot
    compare_colors = white,gold,yellow,deeppink,darkorange,cyan,lime,red
    compare_signs = .,.,.,.,.,.,.,.,-.
    ##Would appreciate if that stays, so GRUNT gets more visibility
    credit = true
    credit_x = 0.75
    credit_y = 0.15


    [Pace_plot]
    colors = green,deeppink,darkorange,cyan
    signs = *,s,o,^
    fit_colors = lime,red,orange,deepskyblue
    ##Would appreciate if that stays, so GRUNT gets more visibility
    credit = true
    credit_x = 0.75
    credit_y = 0.13

    [Runtype_plot]
    rt_pad = -100
    ##Would appreciate if that stays, so GRUNT gets more visibility
    credit = true
    credit_x = 0.10
    credit_y = 0.80

    [Pacedistance_plot]
    signs = *,s,o,^
    colormap = gnuplot
    ##Would appreciate if that stays, so GRUNT gets more visibility
    credit = true
    credit_x = 0.70
    credit_y = 0.13

    [Output]
    directory = 
