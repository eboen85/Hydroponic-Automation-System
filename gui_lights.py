import sys
import os
import serial
import threading
import RPi.GPIO as GPIO 
import time       
from time import strftime
from PyQt4 import QtGui
from PyQt4 import QtCore

def lightcycle(light_on,light_off,days):
  off = QtCore.QTime.fromString(light_off, "hh:mm")
  on = QtCore.QTime.fromString(light_on, "hh:mm")
  nowDate = QtCore.QDate.currentDate()
  endDate = nowDate.addDays(days)
  print "Entering Light Loop"
  while QtCore.QDate.currentDate() < endDate:
      GPIO.setmode(GPIO.BCM)
      gpio_light=17
      GPIO.setwarnings(False)
      GPIO.setup(gpio_light, GPIO.OUT)
      GPIO.output(gpio_light, GPIO.LOW)
      time.sleep(30)
      while QtCore.QTime.currentTime() < on:
          print("Lights are out")
          GPIO.output(gpio_light, GPIO.LOW)
          time.sleep(30)
          while QtCore.QTime.currentTime() <= off:
              print("Lights are on")
              GPIO.output(gpio_light, GPIO.HIGH)
              time.sleep(30)
      
      
  print "Ending Light Script"


