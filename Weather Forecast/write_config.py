# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:49:19 2020

@author: mojia
"""

import configparser

config = configparser.RawConfigParser()

config.add_section('openweathermap')
config.set('openweathermap','api','a62dddf6c81eec52d9dcffd3cf152d67')
config.set('openweathermap','freq','3')

with open('config.ini','w') as configfile:
    config.write(configfile)