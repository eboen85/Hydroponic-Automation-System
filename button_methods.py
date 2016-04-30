def pump_click(self):
        
        pump_time, ok = QtGui.QInputDialog.getInt(self, 'Pump Cycle On', 'Pump will come on for:', 100, 1, 1000, 1)

        if ok:
            wait_time, ok = QtGui.QInputDialog.getInt(self, 'Pump Cycle Off', 'Pump will turn off for:', 1000, 1, 1000, 1)

            if ok:
                cycle_count, ok = QtGui.QInputDialog.getInt(self, 'Pump Cycles', 'Pump will cycle on and off for:', 10000, 1, 1000, 1)

                if ok:
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
                    pumpcycle(float(pump_time),float(wait_time),int(cycle_count)_click():
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

    def light_click(self):
        light_on, ok = QtGui.QInputDialog.getText(self, "Light on", "Lights on at: hh:mm")

        if ok:
            
            light_off, ok = QtGui.QInputDialog.getText(self, "Light off", "Lights off at: hh:mm")

            if ok:
                days, ok = QtGui.QInputDialog.getInt(self, "Days on", "Number of days to run(0-15): ", 15, 0, 1, 1)

                if ok:
                    
                    
                    off = QtCore.QTime.fromString(light_off, "hh:mm")
                    nowDate = QtCore.QDate.currentDate()
                    endDate = nowDate.addDays(days)
                    print "Entering Light Loop"
                    while QtCore.QDate.currentDate() < endDate:
                        GPIO.setmode(GPIO.BCM)
                        gpio_pump=18
                        
                        GPIO.setwarnings(False)
                        GPIO.setup(gpio_pump, GPIO.OUT)
                        GPIO.output(gpio_pump, GPIO.LOW)
                        print "Lights are out"
                        time.sleep(60*60)
                        while QtCore.QTime.currentTime() <= on:
                            GPIO.output(gpio_pump, GPIO.LOW)
                            time.sleep(60)
                            print "Lights on"
                            while QtCore.QTime.currentTime() <= off:
                                GPIO.output(gpio_pump, GPIO.HIGH)
                                time.sleep(60)
                                print "Not off yet"
                        GPIO.output(gpio_pump, GPIO.LOW)
                        print "Lights Off"
                    print "Ending Light Script"

                   def light_click():
        print "Light start"
