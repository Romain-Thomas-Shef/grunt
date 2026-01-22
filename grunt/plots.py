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
import matplotlib.dates as mdates
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
    background = tuple(float(i)/255 for i in conf['Plot']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i)/255 for i in conf['Plot']['text'].split(','))
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


def compare_year(data, title, ylabel, save, conf, filename):
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
    
    fig = plt.figure(dpi=int(conf['Plots']['dpi']))
    plot = fig.add_subplot(111)

    ###adjust background color
    background = tuple(float(i)/255 for i in conf['Plot']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i)/255 for i in conf['Plot']['text'].split(','))
    plot.set_title(title, color=color_text)
    plot.axes.tick_params(color=color_text, labelcolor=color_text, which="both")
    plot.set_xlabel('Day-Month', color=color_text)
    plot.set_ylabel(ylabel, color=color_text)
 

    ##add the plot
    for year,color,marker in zip(data, conf['Plot']['compare_colors'].split(','), conf['Plot']['compare_signs']):
        plot.plot(data[year][0], data[year][1], color=color, label=year, marker=marker, markersize=3)

    ##add legend
    plot.legend(loc = 'upper left', fancybox=False, framealpha=0, labelcolor=color_text, ncol=2)
    plot.xaxis.set_minor_locator(mdates.MonthLocator())
    plot.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plot.tick_params(axis="both",direction="in", top=True, right=True)
    plot.tick_params(axis="both",which="minor", bottom=False)
    


    ###frame color
    for spine in plot.spines.values():
        spine.set_edgecolor(color_text)

    ###Add credit
    if conf['Plot']['credit'].lower() in ['true', 'yes']:
        plt.figtext(0.78, 0.89, f'Made with GRUNT', fontsize=6, color=color_text)

    ###Saving or showing
    if not save:
        plt.show()
    else:
        fig.tight_layout()
        plt.savefig(os.path.join(conf['Output']['directory'], filename))
        



def runtypes_hist(runtypes, save, conf, filename):
    '''
    Histogram with run types
    
    Parameters
    ----------
    dates   :   numpy array
                with dates
    save:   bool
            if we save the plot or not
    conf:   dict
            configuration of grunt
    filename:   str
                name of the file in case of saving
    '''
    fig = plt.figure(dpi=int(conf['Plots']['dpi']))
    plot = fig.add_subplot(111)

    ###adjust background color
    background = tuple(float(i)/255 for i in conf['Plot']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i)/255 for i in conf['Plot']['text'].split(','))
    plot.axes.tick_params(color=color_text, labelcolor=color_text, which="both", bottom=False, top=False, left=False, labelleft=False)
 
    values = plt.bar(runtypes.keys(), runtypes.values(), linestyle='--')
    plt.bar_label(values, fontsize=15, color='white')
    
    plot.xaxis.set_tick_params(pad=-160)
    xtickNames = plot.set_xticklabels([i.replace('_', ' ') for i in runtypes.keys()], rotation=90)

    ##set ylimit
    plot.set_ylim(0, max(runtypes.values()) + 2)


    ###frame color
    for spine in plot.spines.values():
        spine.set_edgecolor(color_text)

    ###Saving or showing
    if not save:
        plt.show()
    else:
        fig.tight_layout()
        plt.savefig(os.path.join(conf['Output']['directory'], filename))
 
