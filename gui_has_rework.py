import sys
from PyQt4 import QtGui

class HAS(QtGui.QWidget):
	
	def __init__(self):
        super(HAS, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
	
	    exitAction = QtGui.QAction(QtGui.QIcon('exit24.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		
		self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtGui.QPushButton('Pump', self)
        btn.setToolTip('Starts pump script')
        btn.resize(btn.sizeHint())
        btn.move(25, 25)
		
		btn = QtGui.QPushButton('pH Meter', self)
        btn.setToolTip('Starts pH script')
        btn.resize(btn.sizeHint())
        btn.move(25, 50)
		
		btn = QtGui.QPushButton('Light', self)
        btn.setToolTip('Starts light script')
        btn.resize(btn.sizeHint())
        btn.move(25, 75)
		
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('HAS')
        self.setWindowIcon(QtGui.QIcon('leaflogotest.pgn'))        
    
        self.show()
	
	def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure you want to close the HAS", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
		
		
def main():
	app = QtGui.QApplication(sys.argv)
	gui = HAS()                          #just a handy label for the window
	sys.exit(app.exec_())
  
  
if __name__ == '__main__':
	main()	
