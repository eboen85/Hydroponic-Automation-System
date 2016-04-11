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

        pump_btn = QtGui.QPushButton('Pump', self)
        pump_btn.resize(pump_btn.sizeHint())
        pump_btn.move(25, 30)
        pump_btn.clicked.connect(self.pump_click)

        light_btn = QtGui.QPushButton('Light', self)
        light_btn.resize(light_btn.sizeHint())
        light_btn.move(25, 70)
        light_btn.clicked.connect(self.light_click)

        pH_button = QtGui.QPushButton('pH Sensor', self)
        pH_button.resize(light_btn.sizeHint())
        pH_button.move(25,110)
        pH_button.clicked.connect(self.pH_click)

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
        print "Pump started"
    def light_click(self):
        print "Lights ON"
    def pH_click(self):
        print "pH Clicked"
        pHcont, ok = QtGui.QInputDialog.getText(self, "pH runs", "c,1 to start ph reading: c,1")
        if ok:
            ser.write(pHcont + "\r")
               
def pHscript():
    print "pH sensor started"
    ser = serial.Serial(      #initiate the serial connection into the 'ser' variable
        port='/dev/ttyAMA0',    #set the port address of the Atlas stamp
        baudrate=9600)          #set the baudrate 
    ser.write('\r')     #an initial write to clear the serial buffer
    ser.write("L, 1\r")
    def read_from_port(ser):
        line =" "                #initiate read variable we'll call 'line'
        while True:               #start the While loop
        # data = ser.read()       #read the serial port and store in the 'data' variable
            data2 = ser.read()
            if(data2 == "\r"):       #if there is a carriage return 
                now = time.strftime("%Y-%m-%d %H:%M:%S")
                print line + " " + now
                line = " "             #set the variable back to nothing
            else:
                line = line + data2    #append the data onto the line variable 
    thread = threading.Thread(target=read_from_port, args=(ser,)) #create the thread to read the serial port, include the target definition and the serial protocol
    thread.start()  #start the thread
 
        
def main():
    pHscript()
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()   
