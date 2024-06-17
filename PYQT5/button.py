import sys
from PyQt5 import QtWidgets, QtGui

def createWindow():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("PYQT5.3")
    
    window.setGeometry(100,100,300,300)
    window.setFixedSize(500,100)
    
    button = QtWidgets.QPushButton(window)
    button.setText("CLICK")
    button.move(205,50)
    
    label = QtWidgets.QLabel(window)
    label.setText("HELLO AGAIN!")
    label.move(200,30)
        
    window.show()
    
    sys.exit(app.exec_())
    

createWindow()