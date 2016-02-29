import RPi.GPIO as GPIO #import the GPIO library
import time       #import the 'time' library.  Allows the use of sleep
import MySQLdb
from time import strftime

print "Welcome to the pHASS pump script"

phss = MySQLdb.connect("localhost","dick","smile","phss")
GPIO.setmode(GPIO.BCM)          # Uses the broadcom pin numbering
gpio_pump=18                    # Sets the pump to pin 18

GPIO.setwarnings(False)          # Set GPIO warnings to False
GPIO.setup(gpio_pump, GPIO.OUT) # Sets pump output to GPIO
GPIO.output(gpio_pump, GPIO.HIGH)    # Sets pump output to True

def pumpcycle(pump_time,wait_time,cycle_count):
    if cycle_count ==0:
	cycle_count=999
    for i in range(0,cycle_count): ## Run the cycle numTime
        ##pump cycle
        print strftime("%Y-%m-%d %H:%M:%S") + "Pump is coming on for " + str(pump_time*60)
	GPIO.output(gpio_pump, GPIO.LOW) #Turn pump on
	
	now = time.strftime("%Y-%m-%d %H:%M:%S")
	sql_on = 'INSERT INTO Cycle(starttime) VALUES ("%s")' %(now)
	
	time.sleep(pump_time*60) # pump timer

	print strftime("%Y-%m-%d %H:%M:%S") + "Pump is turning off "
	GPIO.output(gpio_pump, GPIO.HIGH) # switch off pump
	
	now = time.strftime("%Y-%m-%d %H:%M:%S")
	sql_off = 'INSERT INTO Cycle(endtime) VALUES ("%s")' %(now)

	print strftime("%Y-%m-%d %H:%M:%S") + "Pump is going into standby for: " + str(wait_time*60)

	time.sleep(wait_time*60)  # system go to sleep

    print "DONE!"
    GPIO.cleanup()

#Prompt user for inputs
pump_time_input = raw_input("Mintues to run the pump: ")
wait_time_input = raw_input("Mintues to wait between watering: ")
print("1 cycle = pump time + wait_time")
cycle_count_input = raw_input("How many cycles: ")

pumpcycle(float(pump_time_input),float(wait_time_input),int(cycle_count_input))
