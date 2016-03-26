import sys
from PyQt4 import QtGui

class HAS(QtGui.QWidget):
	
	def __init__(self):
        super(HAS, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
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
