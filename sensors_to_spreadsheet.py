#!/usr/bin/python
from datetime import datetime, timedelta
import os
import requests
import time
import Adafruit_DHT
import smbus

def output_spreadsheet(all_values_dict):
    url = "https://script.google.com/macros/s/AKfycbx5aYprqEydOmzUdt4Z4d0qIfBTRjIgRdDLWRWGgbs-UlaSea4l7WGqr6-iWPSzZDk/exec"
    response = requests.post(url, data=all_values_dict)
    print(response.text)

def get_temp_humid():
    sensor = Adafruit_DHT.DHT11

    pin = 14

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get temp and humid.')
    
    return temperature, humidity


def get_brightness():
    Bus = smbus.SMBus(1)
    Addr = 0x23
    try:
        LxRead = Bus.read_i2c_block_data(Addr,0x11)
        print('Brightness='+str(LxRead[1]))
        brightness = LxRead[1]
    except:
        brightness = None
        print('Failed to get brightness.')
    
    return brightness


if __name__ == '__main__':
    while 1:
        startdate = datetime.today()
        masterdate = startdate.replace(second=0, microsecond=0)
        if startdate.second >= 30:
            masterdate += timedelta(minutes=1)
            
        
        temperature, humidity = get_temp_humid()
        brightness = get_brightness()
        
        all_values_dict = None

        all_values_dict = {
            'Date_Master': str(masterdate),
            'Date': str(datetime.today()),
            'Temperature': temperature,
            'Humidity': humidity,
            'Brightness': brightness,
        }
        print(all_values_dict)
        
        output_spreadsheet(all_values_dict)
        
        time.sleep(300)
