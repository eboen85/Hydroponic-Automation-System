import sys
import os
import serial
import threading
import RPi.GPIO as GPIO 
import time       
from time import strftime
from PyQt4 import QtGui
from PyQt4 import QtCore

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)      

        ct = QtCore.QTime.currentTime();
        


        light_btn = QtGui.QPushButton('Light', self)
        light_btn.resize(light_btn.sizeHint())
        light_btn.move(25, 70)
        light_btn.clicked.connect(self.light_click)
        self.eventLogLabel = QtGui.QLabel('Event Log', self)
        self.eventLogLabel.setGeometry(QtCore.QRect(290, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eventLogLabel.setFont(font)
        
        self.eventLog = QtGui.QPlainTextEdit(self)
        self.eventLog.setGeometry(QtCore.QRect(210, 40, 231, 251))
        self.eventLog.setReadOnly(True)
        sb = self.eventLog.verticalScrollBar()
        sb.setValue(sb.maximum())
        
        
        self.setGeometry(300, 300, 500, 300)
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
                    while QtCore.QDate.currentDate() <= endDate:
                        GPIO.setmode(GPIO.BCM)
                        gpio_pump=18
                        
                        GPIO.setwarnings(False)
                        GPIO.setup(gpio_pump, GPIO.OUT)
                        GPIO.output(gpio_pump, GPIO.LOW)
                        print "Lights are out"
                        time.sleep(60*60)
                        while QtCore.QTime.currentTime() >= on and QtCore.QTime.currentTime() <= off:
                            GPIO.output(gpio_pump, GPIO.HIGH)
                            time.sleep(60)
                            self.eventLog.insertPlainText("Lights on at: " + QtCore.QTime.currentTime())
                            if QtCore.QTime.currentTime() == off:
                                GPIO.output(gpio_pump, GPIO.LOW)
                                self.eventLog.insertPlainText("Lights off at: " + QtCore.QTime.currentTime())
                    print "Ending Light Script"

       
def main():
   
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()   
