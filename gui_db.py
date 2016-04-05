import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import QtSql

class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        
        
        phsql = QtSql.QSqlQuery("select phvalue from (select max(values(phid)), phvalue from reading order by 1) as ph")
        while (phsql.next()):
            ph = str(phsql.value(0))
            
        posql = QtSql.QSqlQuery("select pumpon from (select max(values(cid)), pumpon from cycle order by 1) as pumpon")
        while (posql.next()):
            po = posql.value(0).toString("MMM dd yyyy 'at' hh:mm:ss ap")

        pfsql = QtSql.QSqlQuery("select pumpoff from (select max(values(cid)), pumpoff from cycle order by 1) as pumpoff")
        while (pfsql.next()):
            pf = pfsql.value(0).toString("MMM dd yyyy 'at' hh:mm:ss ap")

        lbpot = QtGui.QLabel('Pump last on at: ', self)
        lbpot.move(15, 10)
        
        lbpo = QtGui.QLabel(po, self)
        lbpo.move(100, 10)
        
        lbpft = QtGui.QLabel('Pump last off at: ', self)
        lbpft.move(15, 40)
        
        lbpf = QtGui.QLabel(pf, self)
        lbpf.move(100, 40)
        
        lbpht = QtGui.QLabel("pH last recorded value: ", self)
        lbpht.move(15, 70)
        
        lbph = QtGui.QLabel(ph, self)
        lbph.move(135, 70)        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Database')    
        self.show()
def main():
    
    app = QtGui.QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName("localhost")
    db.setPort(3306)
    db.setDatabaseName("has")
    db.setUserName("root")
    db.setPassword("671092")
    db.open()
    w = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()