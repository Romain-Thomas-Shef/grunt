"""
This file is part of the grunt module 
makes the plot

Author: R. Thomas
Place: Sheffield, UK
Year: 2025
"""

###Python standard library

##Third party
import matplotlib.pyplot as plt
import july

##Local imports

def create_calendar(dates, values, title, save):
    '''
    This creates the calendar plot
    
    Parameters
    ----------
    dates   :   numpy array
                with dates
    values: numpy array
            values of the parameter
    save:   bool
            if we save the plot or not
    '''
    plot, fig = july.heatmap(dates, values, title=title, cmap="gnuplot", year_label=False)
    fig.tight_layout()
 
    if not save:
        plt.show()
    else:
        plot.savefig('test.png')
