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
import juillet

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
    plot, fig = juillet.heatmap(dates, values, title=title,
                             cmap=conf['Plot_calendar']['colormap'],
                             year_label=False, customfigsize=(18,5))
    fig.tight_layout()

    ###adjust background color
    background = tuple(float(i)/255 for i in conf['Plot_general']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i)/255 for i in conf['Plot_general']['text'].split(','))
    plot.set_title(title, color=color_text)
    plot.axes.tick_params(color=color_text, labelcolor=color_text)

    ###Add credit
    if conf['Plot_calendar']['credit'].lower() in ['true', 'yes']:
        xcredit = float(conf['Plot_calendar']['credit_x'])
        ycredit = float(conf['Plot_calendar']['credit_y'])
        plt.figtext(xcredit, ycredit, 'Made with GRUNT', fontsize=9, color=color_text)

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

    fig = plt.figure(dpi=int(conf['Plot_general']['dpi']))
    plot = fig.add_subplot(111)

    ###adjust background color
    background = tuple(float(i)/255 for i in conf['Plot_general']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i)/255 for i in conf['Plot_general']['text'].split(','))
    plot.set_title(title, color=color_text)
    plot.axes.tick_params(color=color_text, labelcolor=color_text, which="both")
    plot.set_xlabel('Day-Month', color=color_text)
    plot.set_ylabel(ylabel, color=color_text)

    ##add the plot
    for year,color,marker in zip(data, conf['Compare_distance_plot']['compare_colors'].split(','),
                                 conf['Compare_distance_plot']['compare_signs']):
        plot.plot(data[year][0], data[year][1], color=color, label=year,
                  marker=marker, markersize=3)

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
    if conf['Compare_distance_plot']['credit'].lower() in ['true', 'yes']:
        xcredit = float(conf['Compare_distance_plot']['credit_x'])
        ycredit = float(conf['Compare_distance_plot']['credit_y']) 
        plt.figtext(xcredit, ycredit, 'Made with GRUNT', fontsize=6, color=color_text)

    ###Saving or showing
    if not save:
        plt.show()
    else:
        fig.tight_layout()
        plt.savefig(os.path.join(conf['Output']['directory'], filename),
                                 dpi=int(conf['Plot_general']['dpi']))


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
    fig = plt.figure(dpi=int(conf['Plot_general']['dpi']))
    plot = fig.add_subplot(111)

    ###adjust background color
    background = tuple(float(i)/255 for i in conf['Plot_general']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i)/255 for i in conf['Plot_general']['text'].split(','))
    plot.axes.tick_params(color=color_text, labelcolor=color_text, which="both",
                          bottom=False, top=False, left=False, labelleft=False)

    values = plt.bar(runtypes.keys(), runtypes.values(), linestyle='--')
    plt.bar_label(values, fontsize=15, color=color_text)

    plot.set_xticklabels([i.replace('_', ' ').split()[0] for i in runtypes.keys()], rotation=90)
    plot.xaxis.set_tick_params(pad=int(conf['Runtype_plot']['rt_pad']))

    ##set ylimit
    plot.set_ylim(0, max(runtypes.values()) + 2)

    ###frame color
    for spine in plot.spines.values():
        spine.set_edgecolor(color_text)

    ###Add credit
    if conf['Runtype_plot']['credit'].lower() in ['true', 'yes']:
        xcredit = float(conf['Runtype_plot']['credit_x'])
        ycredit = float(conf['Runtype_plot']['credit_y']) 
        plt.figtext(xcredit, ycredit, 'Made with GRUNT', fontsize=6, color=color_text)

    ###Saving or showing
    if not save:
        plt.show()
    else:
        fig.tight_layout()
        plt.savefig(os.path.join(conf['Output']['directory'], filename),
                                 dpi=int(conf['Plot_general']['dpi']))

def pace_scatter(data, runtypes, conf, title, save, filename):
    '''
    This function makes a scatter plot
    with pace vs date

    Parameters
    ----------
    data    : pandas dataframe
              with a date and pace column

    types   : list
              of string with runtypes

    conf    : dictionary
              configuration of grunt

    title   :   str
                title of the plot

    save    :   bool
                if we save the plot or not
    ''' 
    fig = plt.figure(dpi=int(conf['Plot_general']['dpi']))
    plot = fig.add_subplot(111)

    ###adjust background color
    background = tuple(float(i)/255 for i in conf['Plot_general']['background'].split(','))
    fig.patch.set_facecolor(background)
    plot.set_facecolor(background)

    ###text
    color_text = tuple(float(i)/255 for i in conf['Plot_general']['text'].split(','))
    plot.set_title(title, color=color_text)
    plot.axes.tick_params(color=color_text, labelcolor=color_text, which="both")
    plot.set_xlabel('Year', color=color_text)
    plot.set_ylabel('Pace [min/km]     (slow --> fast)', color=color_text)

    ###frame color
    for spine in plot.spines.values():
        spine.set_edgecolor(color_text)

    ##we revert the axis (faster at the top)
    plot.yaxis.set_inverted(True)
    plot.tick_params(axis='x', labelrotation=10, pad=-2)

    ##make the plot
    colors = conf['Pace_plot']['colors'].split(',')
    colors_fit = conf['Pace_plot']['fit_colors'].split(',')
    signs = conf['Pace_plot']['signs'].split(',')

    for d,color,runtype,marker,fit in zip(data, colors, runtypes, signs, colors_fit):
        plot.scatter(d['date'], d['pace'], marker=marker, color=color,
                     label=runtype.replace('_', ' ').split()[0], facecolor="None")
        plot.plot(d['date'], d['Fit'], color=fit, ls='-.')
    

    plot.legend(labelcolor=color_text, frameon=False, loc='lower left')

    ###Add credit
    if conf['Pace_plot']['credit'].lower() in ['true', 'yes']:
        xcredit = float(conf['Pace_plot']['credit_x'])
        ycredit = float(conf['Pace_plot']['credit_y']) 
        plt.figtext(xcredit, ycredit, 'Made with GRUNT', fontsize=6, color=color_text)

    ###Saving or showing
    if not save:
        plt.show()
    else:
        fig.tight_layout()
        plt.savefig(os.path.join(conf['Output']['directory'], filename),
                                 dpi=int(conf['Plot_general']['dpi']))


