"""
This file is part of the grunt module 
makes the plot

Author: R. Thomas
Place: Sheffield, UK
Year: 2025
"""

###Python standard library
import os

##Third party
import matplotlib.pyplot as plt
import july

##Local imports

def create_calendar(dates, values, title, save, conf, filename):
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
    conf:   dict
            configuration of grunt
    filename:   str
                name of the file in case of saving
    '''

    ###make the plot
    plot, fig = july.heatmap(dates, values, title=title, cmap=conf['Plot']['colormap_calendar'], year_label=False)
    fig.tight_layout()

    ###adjust background color
    background = tuple(float(i) for i in conf['Plot']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i) for i in conf['Plot']['text'].split(','))
    plot.set_title(title, color=color_text)
    plot.axes.tick_params(color=color_text, labelcolor=color_text)
    
    ###Add credit
    if conf['Plot']['credit'].lower() in ['true', 'yes']:
        plt.figtext(0.93, 0.2, f'Made with GRUNT', fontsize=9, color=color_text)

    ###Saving or showing
    if not save:
        plt.show()
    else:
        plt.savefig(os.path.join(conf['Output']['directory'], filename))
