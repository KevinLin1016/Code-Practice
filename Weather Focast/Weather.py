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
def download_forecast(api_key,city):
    url2='http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=imperial'.format(city,api_key)
    res=requests.get(url2)
    print(url2)
    return res.json()

def load_map(api_key,x,y):
    url='https://tile.openweathermap.org/map/{}/{}/{}/{}.png?appid={}'.format('temp_new',10,x,y,api_key)
    print(url)
    res=requests.get(url)
    return res
    
    
def plot_weather():
    fig=plt.figure(figsize=(15,7))
    custom_collor=["#ffffe5","#f7fcb9","#d9f0a3","#addd8e","#78c679","#41ab5d","#238443","#006837","#004529"]
    custom_cmap = colors.ListedColormap(custom_color)
    custom_cmap.set_over((0.,0.,1.,0))
    custom_cmap.set_under((0.,0.,1.,0))
    
    plt.imshow(ndvi)

def show_forecast(d):
    d.get('forecast')
    
    
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
