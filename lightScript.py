import RPi.GPIO as GPIO #import the GPIO library
import time       #import the 'time' library.  Allows the use of sleep
import MySQLdb
from time import strftime

print "Welcome to the HAS Lighting script"

phss = MySQLdb.connect("localhost","dick","smile","phss")
GPIO.setmode(GPIO.BCM)          # Uses the broadcom pin numbering
gpio_pump=18                    # Sets the pump to pin 18

GPIO.setwarnings(False)          # Set GPIO warnings to False
GPIO.setup(gpio_light, GPIO.OUT) # Sets light output to GPIO
GPIO.output(gpio_light, GPIO.HIGH)    # Sets light output to True

def lightcycle(light_time,wait_time,cycle_count):
    if cycle_count ==0:
	cycle_count=999
    for i in range(0,cycle_count): ## Run the cycle numTime
        ##light cycle
        print strftime("%Y-%m-%d %H:%M:%S") + "Light is coming on for " + str(light_time*3600) + " hours."
	GPIO.output(gpio_light, GPIO.LOW) #Turn light on
	
	light_on = time.strftime("%Y-%m-%d %H:%M:%S")
	
	time.sleep(light_time*3600) # pump timer

	print strftime("%Y-%m-%d %H:%M:%S") + "Light is turning off "
	GPIO.output(gpio_light, GPIO.HIGH) # switch off light
	
	light_off = time.strftime("%Y-%m-%d %H:%M:%S")
	sql = 'INSERT INTO Lighting(starttime, endtime) VALUES ("%s, %s")' %(light_on, light_off)

	print strftime("%Y-%m-%d %H:%M:%S") + "Light is going into standby for: " + str(wait_time*60)

	time.sleep(wait_time*60)  # system go to sleep

    print "DONE!"
    GPIO.cleanup()

#Prompt user for inputs
light_time_input = raw_input("Hours to turn on the light: ")
wait_time_input = raw_input("Hours to wait between lighting: ")
print("1 cycle = light time + wait_time")
cycle_count_input = raw_input("How many cycles: ")

lightcycle(float(light_time_input),float(wait_time_input),int(cycle_count_input))
