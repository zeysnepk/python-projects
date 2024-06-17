import sys
from PyQt5 import QtWidgets


def Window():
    
    app = QtWidgets.QApplication(sys.argv) #creating an application object from sys
    
    window = QtWidgets.QWidget() #creating a window
    
    window.setWindowTitle("PYQT5.1") #creating a title for window
    
    window.show() #shows window
    
    sys.exit(app.exec_()) #A loop for the window to appear until exit button is not clicked

Window()
