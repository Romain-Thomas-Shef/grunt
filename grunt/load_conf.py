"""
This file is part of the grunt module 
load the configuration file

Author: R. Thomas
Place: Sheffield, UK
Year: 2025
"""

###Python standard library
import configparser

##Third party

##Local imports

def load(file):
    '''
    Function that load the configuration
    
    Parameters
    ----------
    file    :   str
                path to file

    Return
    ------
    conf    : dictionary
              with configuration
    '''
    ##load the conf
    conf = configparser.ConfigParser()
    conf.read(file)

    return conf._sections
