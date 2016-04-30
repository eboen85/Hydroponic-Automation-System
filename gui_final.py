import sys

import gui_pump
import gui_lights
import gui_ph

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 300)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.startPump = QtGui.QPushButton(self.centralWidget)
        self.startPump.setGeometry(QtCore.QRect(50, 50, 100, 30))
        self.startPump.setObjectName(_fromUtf8("startPump"))
        self.startPump.clicked.connect(self.pump_start)
        self.turnLights = QtGui.QPushButton(self.centralWidget)
        self.turnLights.setGeometry(QtCore.QRect(50, 90, 100, 30))
        self.turnLights.setObjectName(_fromUtf8("turnLights"))
        self.turnLights.clicked.connect(self.lights_start)
        self.monitorPH = QtGui.QPushButton(self.centralWidget)
        self.monitorPH.setGeometry(QtCore.QRect(50, 130, 100, 30))
        self.monitorPH.setObjectName(_fromUtf8("monitorPH"))
        self.monitorPH.clicked.connect(self.ph_start)
        self.programName = QtGui.QLabel(self.centralWidget)
        self.programName.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.programName.setFont(font)
        self.programName.setTextFormat(QtCore.Qt.AutoText)
        self.programName.setObjectName(_fromUtf8("programName"))
        self.horizSep = QtGui.QFrame(self.centralWidget)
        self.horizSep.setGeometry(QtCore.QRect(190, 0, 20, 301))
        self.horizSep.setFrameShape(QtGui.QFrame.VLine)
        self.horizSep.setFrameShadow(QtGui.QFrame.Sunken)
        self.horizSep.setObjectName(_fromUtf8("horizSep"))
        self.eventLogLabel = QtGui.QLabel(self.centralWidget)
        self.eventLogLabel.setGeometry(QtCore.QRect(290, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eventLogLabel.setFont(font)
        self.eventLogLabel.setObjectName(_fromUtf8("eventLogLabel"))
        self.eventLog = QtGui.QPlainTextEdit(self.centralWidget)
        self.eventLog.setGeometry(QtCore.QRect(210, 40, 231, 251))
        self.eventLog.setReadOnly(True)
        self.eventLog.setObjectName(_fromUtf8("eventLog"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HAS", None))
        self.startPump.setText(_translate("MainWindow", "Start Pump", None))
        self.turnLights.setText(_translate("MainWindow", "Turn On Lights", None))
        self.monitorPH.setText(_translate("MainWindow", "Monitor pH", None))
        self.programName.setText(_translate("MainWindow", "Hydroponic Automation System", None))
        self.eventLogLabel.setText(_translate("MainWindow", "Event Log", None))
        
    def pump_start(arg1,arg2):
        pump_time, ok = QtGui.QInputDialog.getDouble(None, 'Pump Cycle On', 'Pump will come on for:', 1, .25, 1000, 1)
        if ok:
            wait_time, ok = QtGui.QInputDialog.getDouble(None, 'Pump Cycle Off', 'Pump will turn off for:', 1, .25, 1000, 1)
            if ok:
                cycle_count, ok = QtGui.QInputDialog.getInt(None, 'Pump Cycles', 'Pump will cycle on and off for:', 10000, 1, 1000, 1)
                if ok:
                  gui_pump.pumpcycle(pump_time,wait_time,cycle_count)
      
    def lights_start(arg1,arg2):
        light_on, ok = QtGui.QInputDialog.getText(None, "Light on", "Lights on at: hh:mm")
        if ok:
            light_off, ok = QtGui.QInputDialog.getText(None, "Light off", "Lights off at: hh:mm")
            if ok:
                days, ok = QtGui.QInputDialog.getInt(None, "Days on", "Number of days to run(0-15): ", 15, 0, 15, 1)
                if ok:
                  gui_lights.lightcycle(light_on,light_off,days)
      
    def ph_start(arg1,arg2):
      gui_ph.main()
      
    def add_log_line(arg1):
      string = QtCore.QString(arg1)
      self.eventLog.append(self,string)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

