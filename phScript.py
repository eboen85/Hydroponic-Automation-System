import os         #import OS module to easily exit the program 
import serial     #import serial module to enable serial commands 
import threading  #import threading module to create a separate thread for reading the serial port
import time	  #import time
from time import strftime #import string format for time
import MySQLdb 
print "Welcome pHASS!"

ser = serial.Serial(      #initiate the serial connection into the 'ser' variable
  port='/dev/ttyAMA0',    #set the port address of the Atlas stamp
  baudrate=9600          #set the baudrate 
)

ser.write('\r')     #an initial write to clear the serial buffer
flush = ser.read(3) #flush into variable (only needed for EZO circuits) 
ser.write("L, 1\r")
f = open('pi Reading', 'a')
print f
phss = MySQLdb.connect("localhost","dick","smile","phss")
def read_from_port(ser):    #create definition for your serial read thread
    
  cur = phss.cursor()    #perpare cursor object
  

  line =" "                #initiate read variable we'll call 'line'
  while True:               #start the While loop
   # data = ser.read()       #read the serial port and store in the 'data' variable
    data2 = ser.read()
    
    
    if(data2 == "\r"):       #if there is a carriage return 
      
      now = time.strftime("%Y-%m-%d %H:%M:%S")
     
      sql = 'INSERT INTO Reading(Date,Reading) VALUES ("%s","%s")' %(now,line)
            
      print line + " " + now
      f.write(line + " " + now)
      cur.execute(sql)
      phss.commit()
     
      line = " "             #set the variable back to nothing

    else:
      line = line + data2    #append the data onto the line variable 
      
thread = threading.Thread(target=read_from_port, args=(ser,)) #create the thread to read the serial port, include the target definition and the serial protocol
thread.start()  #start the thread

print '\r\nEnter your commands below.\r\nInsert "exit" to leave the application.\n'


while True: 
    input = raw_input("")  # get keyboard/command input

    if input == 'exit':     #if you type 'exit'
     phss.close()
     ser.close()           #close the serial port
     os._exit(1)           #exit the program
    
    else:
     ser.write(input + "\r") #write the command to the serial port 

