import sys
import os
import serial
import threading
import RPi.GPIO as GPIO 
import time       
from time import strftime
from PyQt4 import QtGui
from PyQt4 import QtCore

def pumpcycle(pump_time,wait_time,cycle_count):
    print ("Pump Script Starting")
    GPIO.setmode(GPIO.BCM)
    gpio_pump=18
    GPIO.setwarnings(False)
    GPIO.setup(gpio_pump, GPIO.OUT)
    GPIO.output(gpio_pump, GPIO.LOW)
    if cycle_count ==0:
        cycle_count=999
    for i in range(0,cycle_count):
        GPIO.output(gpio_pump, GPIO.HIGH)
        print ("Pump Starting")
        time.sleep(pump_time*60)
        GPIO.output(gpio_pump, GPIO.LOW)
        print ("Pump Stopping")
        time.sleep(wait_time*60)
    
    


                


                    


       
   
