import sys
import RPi.GPIO as GPIO
import time
from time import strftime

from PyQt4 import QtGui
from PyQt4 import QtCore

class HAS(QtGui.QMainWindow):
        
    def __init__(self):
                super(HAS, self).__init__()
        
                self.initUI()
        
        
    def initUI(self):
        
                exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
                exitAction.setShortcut('Ctrl+Q')
                exitAction.setStatusTip('Exit application')
                exitAction.triggered.connect(self.close)

                menubar = self.menuBar()
                fileMenu = menubar.addMenu('&File')
                fileMenu.addAction(exitAction)

        
                pump_btn = QtGui.QPushButton('Pump', self)
                pump_btn.setToolTip('Starts pump script')
                pump_btn.resize(pump_btn.sizeHint())
                pump_btn.move(25, 30)
                pump_btn.clicked.connect(pump_click)
                
                pH_btn = QtGui.QPushButton('pH Meter', self)
                pH_btn.setToolTip('Starts pH script')
                pH_btn.resize(pH_btn.sizeHint())
                pH_btn.move(25, 70)
                pH_btn.clicked.connect(pH_click)
                
                light_btn = QtGui.QPushButton('Light', self)
                light_btn.setToolTip('Starts light script')
                light_btn.resize(light_btn.sizeHint())
                light_btn.move(25, 110)
                light_btn.clicked.connect(light_click)
                
                self.setGeometry(500, 500, 250, 150)
                self.setWindowTitle('HAS')
                self.setWindowIcon(QtGui.QIcon('leaf.jpg'))        
    
                self.show()
    def closeEvent(self, event):
                reply = QtGui.QMessageBox.question(self, 'Message',
                    "Are you sure you want to close the HAS", QtGui.QMessageBox.Yes | 
                    QtGui.QMessageBox.No, QtGui.QMessageBox.No)

                if reply == QtGui.QMessageBox.Yes:
                    event.accept()
                else:
                    event.ignore()
                    
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
                            pumpcycle(float(pump_time),float(wait_time),int(cycle_count))  

    def pH_click():
                print "pH meter start"

    def light_click(self):
                light_on, ok = QtGui.QInputDialog.getInt(self, 'Light Cycle On', 'Pump will come on for:', 100, 1, 1000, 1)

                if ok:
                    light_off, ok = QtGui.QInputDialog.getInt(self, 'Light Cycle Off', 'Pump will turn off for:', 1000, 1, 1000, 1)
                    if ok:
                        day_count, ok = QtGui.QInputDialog.getInt(self, 'Day', 'Lights will run for how many days:', 10000, 1, 1000, 1)

                        if ok:
                            GPIO.setmode(GPIO.BCM)
                            gpio_pump=18
            
                            GPIO.setwarnings(False)
                            GPIO.setup(gpio_pump, GPIO.OUT)
                            GPIO.output(gpio_pump, GPIO.HIGH)    

                            def lightCycle(light_on,light_off,day_count):
                                    print light_on + light_off + day_count
    
        
        
            

        
            
def main():
        app = QtGui.QApplication(sys.argv)
        ex = HAS()                          #just a handy label for the window
        sys.exit(app.exec_())
  
  
if __name__ == '__main__':
        main()  
