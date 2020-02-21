# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:50:11 2020

@author: mojia
"""
import configparser
import threading
import logging
import time
import requests
import json

from pyowm import OWM
from pyowm.utils import geo
from pyowm.alertapi30.enums import WeatherParametersEnum
from pyowm.alertapi30.trigger import Trigger
from pyowm.alertapi30.alert import Alert


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import colors
from pprint import pprint
import webbrowser
import os

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

#def thread_function(name):
#    logging.info("Download 5 days / 3 hour forecast")
#    time.sleep(2)
#    logging.infor("Download weather forecast complete! ")
#    logging.info("Download waether maps")
# 
#threads=list()
#f=threading.Thread(target=download_forecast,args=(index,),daemon=True)
#threads.append(f)
#f.start()
#
#m=threading.Thread(target=download_map,args=(index,),daemon=True)
#threads.append(m)
#m.start

#Get current weather
def get_weather_record():
    city = input ('Enter your city:')
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=a62dddf6c81eec52d9dcffd3cf152d67&units=metric'.format(city)
    
    res = requests.get(url)
    
    data = res.json()
    
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    
    description = data['weather'][0]['description']
    
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))
    
#Download 5 days/ 3 h forecast weather
def download_forecast(api_key,city):
    url2='http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=imperial'.format(city,api_key)
    res=requests.get(url2)
    print(url2)
    return res.json()

#Download weathermap
def load_map(api_key,x,y):
    url='https://tile.openweathermap.org/map/{}/{}/{}/{}.png?appid={}'.format('temp_new',10,x,y,api_key)
    print(url)
    res=requests.get(url)
    return res

#gerenerate weather alert
def weather_alert(location,api_key):
    owm = OWM(API_Key=api_key)
    am = owm.alert_manager()
    

    reg = owm.city_id_registry()
    geoms = reg.geopoints_for(location)
    
    # ... also, add to Location class a .to_geopoint() method that returns a geo.Point instance
    
    
    # condition
    condition_1 = alerting.Condition('TEMPERATURE', 'LESS_THAN', 2)  # kelvin
    condition_2 = alerting.Condition('RAIN','EQUAL', 80)                   # clouds % coverage
    condition_3 = alerting.Condition('SNOW','EQUAL',50)
     
    # triggers
    trigger = am.create_trigger(start_ts=1234567890, end_ts=1278654300, conditions=[condition_1, condition_2,condition_3], area=[geoms], alert_channel=AlertChannelsEnum.OWM_API)
    triggers_list = am.get_triggers()
    
    
    alerts_list = trigger.get_alerts()
    alerts_list = trigger.get_alerts_since('2020-02-20T23:07:24Z')  # useful for polling alerts
    alerts_list = trigger.get_alerts_on(WeatherParametersEnum.TEMPERATURE)
    alert = trigger.get_alert('alert_id')
    
    am.delete_all_alerts_for(trigger)
    am.delete_alert_for(trigger, alert)

  
    
def main():
    location=input("Enter your city: ")
    api_key=get_api_key()
    data=download_forecast(api_key,location)
    
    temp=data['list'][0]['main']['temp']
    w=data['list'][0]['weather'][0]['main']
    icon=data['list'][0]['weather'][0]['icon']
    description=data['list'][0]['weather'][0]['description']
    x=data['city']['coord']['lat']
    y=data['city']['coord']['lon']
    date=data['list'][0]['dt']
    #weather_alert(location,api_key)
    m=load_map(api_key,int(x),int(y))
    print(temp,w,description,icon,data)
    icon=plt.imread('http://openweathermap.org/img/wn/{}@2x.png'.format(icon))
    
    plt.imshow(icon)
    plt.show()
    path='file:///'+os.path.realpath('leaflet-owm.html')
    path=path.replace(os.sep,'/')
    print(path)
    webbrowser.open(path,new=2)


if __name__=='__main__':
    main()
