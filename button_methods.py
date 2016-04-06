def pump_click():
        print "Pump Script Start"
        pumpMsg = QMessageBox()
        pumpMsg.setWindowTitle("Pump Script Starter")
        
        GPIO.setmode(GPIO.BCM)
        gpio_pump=18

        GPIO.setwarnings(False)
        GPIO.setup(gpio_pump, GPIO.OUT)
        GPIO.output(gpio_pump, GPIO.HIGH)
        def pumpcycle(pump_time,wait_time,cycle_count):
            if cycle_count ==0:
                cycle_count=999
            for i in range(0,cycle_count):
                GPIO.output(gpio_pump, GPIO.LOW)
                time.sleep(pump_time*60)
                GPIO.output(gpio_pump, GPIO.HIGH)
                time.sleep(wait_time*60)
                GPIO.cleanup()
        
def pH_click():
        print "pH meter start"

def light_click():
        print "Light start"
