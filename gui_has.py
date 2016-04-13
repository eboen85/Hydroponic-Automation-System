import sys
import guihelp_sleep

from PyQt4 import QtGui, QtCore         #QtGui for mainwindow, QtCore for easy buttons

class Window(QtGui.QMainWindow):        #same as before but class based and object oriented

  def __init__(self):                   #init method runs every time a Window object is made in this program...once, generally
    super(Window, self).__init__()      #return parent object (QMainWindow object)
    #line below unused if fullscreen
    #self replaces window because using object and inside that object while defining initial state __init__
    self.setGeometry(200,150,500,300)   #setGeometry(start point x, start point y, x [width], y [height]) from top left, in px
    self.setWindowTitle("Gardener UI Test")
    self.setWindowIcon(QtGui.QIcon('leaflogotest.png'))
    self.home()                         #replaces self.show() with user method created below
    
    ctrlClose = QtGui.QAction
    
  
  def home(self):
  
    # top bar
    graphicsScene_logo = QtGui.QGraphicsScene()
    pixmap = QtGui.QGraphicsPixmapItem(QtGui.QPixmap("leaf.jpg"))
    graphicsScene_logo.addItem(pixmap)
    graphicsView_logo = QtGui.QGraphicsView(graphicsScene_logo)
    graphicsView_logo.setGeometry(20, 20, 51, 51)
    graphicsView_logo.show()
    
    label_title = QtGui.QLabel("Hydroponic Automation System", self)
    label_title.setGeometry(250, 20, 480, 50)
    font = QtGui.QFont()
    font.setPointSize(25)
    label_title.setFont(font)
    
    btnSleep = QtGui.QPushButton("Sleep", self)
    btnSleep.setGeometry(750, 20, 75, 23)
    btnSleep.clicked.connect(self.sleep_app)
    
    btnClose = QtGui.QPushButton("Close", self)
    btnClose.setGeometry(750, 50, 75, 23)
    btnClose.clicked.connect(self.close_app)
    btnClose.setShortcut("Ctrl+Q")
    
    
    
    # logs and pump cycles
    tabs = QtGui.QTabWidget()
    tabs.setGeometry(20,100,800,525)
    
    tab_pumpCycles = QtGui.QWidget()
    tabs.addTab(tab_pumpCycles, "Pump Cycles")
    
    tab_logs = QtGui.QWidget()
    log_display = QtGui.QComboBox(tab_logs)
    log_display.setGeometry(160,10,330,22)
    label_chooselog = QtGui.QLabel("Please choose log to view:", tab_logs)
    label_chooselog.setGeometry(20,10,130,16)
    txtb_chooselog = QtGui.QTextBrowser(tab_logs)
    txtb_chooselog.setGeometry(10,40,780,450)
    tabs.addTab(tab_logs, "Logs")
    
    tabs.setCurrentIndex(1)
    tabs.show()
    
    
    
    # system log
    label_syslog = QtGui.QLabel("System Log", self)
    label_syslog.setGeometry(1000,20,120,40)
    font = QtGui.QFont()
    font.setPointSize(16)
    label_syslog.setFont(font)
    
    txtb_syslog = QtGui.QTextBrowser()
    txtb_syslog.setGeometry(860,70,480,640)
    
    
    
    # check bar
    label_waterCheck = QtGui.QLabel("Last User Water Check", self)
    font = QtGui.QFont()
    font.setPointSize(12)
    label_waterCheck.setFont(font)
    label_waterCheck.setGeometry(20, 660, 160, 40)
    
    bar_water = QtGui.QProgressBar()
    bar_water.setGeometry(190, 660, 170, 40)
    bar_water.setMinimum(0)
    bar_water.setMaximum(14)
    bar_water.setProperty("value",2)
    bar_water.setInvertedAppearance(True)
    bar_water.setFormat(" %v days ago")
    
    btn_waterSet = QtGui.QPushButton("Reset", self)
    btn_waterSet.setGeometry(360,670,50,25)
    
    label_pH = QtGui.QLabel("Last System pH Check", self)
    label_pH.setGeometry(430,660,160,40)
    font = QtGui.QFont()
    font.setPointSize(12)
    label_pH.setFont(font)
    
    bar_ph = QtGui.QProgressBar()
    bar_ph.setGeometry(600, 660, 190, 40)
    bar_ph.setMinimum(0)
    bar_ph.setMaximum(30)
    bar_ph.setProperty("value",25)
    bar_ph.setInvertedAppearance(True)
    bar_ph.setFormat(" %v minutes ago")
    
    label_phVal = QtGui.QLabel("Value:", self)
    label_phVal.setGeometry(820,650,30,15)
    
    pH_LCD = QtGui.QLCDNumber()
    pH_LCD.setGeometry(810,650,40,30)
    pH_LCD.setProperty("value",3.3)
     
                                        
    self.showFullScreen()
    #alternatives showMaximized, show (windowed, using the geometry set...also showWindowed), showMinimized
    
    
  def close_app(self):
    print("Application closed by user.")
    sys.exit()
  
  def sleep_app(self):
    guihelp_sleep.main(self)
    
    
def main():
  app = QtGui.QApplication(sys.argv)
  GUI = Window()                          #just a handy label for the window

  #better doorstop, window based
  sys.exit(app.exec_())
  
main()