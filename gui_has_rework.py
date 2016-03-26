import sys
from PyQt4 import QtGui

class HAS(QtGui.QWidget):
	
	def __init__(self):
        super(HAS, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
		
		self.setToolTip('This is a <b>QWidget</b> widget')
        
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
		
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('HAS')
        self.setWindowIcon(QtGui.QIcon('leaflogotest.pgn'))        
    
        self.show()
	def main():
		app = QtGui.QApplication(sys.argv)
		gui = HAS()                          #just a handy label for the window
		sys.exit(app.exec_())
  
  
if __name__ == '__main__':
	main()	
