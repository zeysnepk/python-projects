import sys
from PyQt5 import QtWidgets, QtGui

def Window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("PYQT5.5")
    window.setGeometry(100,100,400,400)
    
    topButton = QtWidgets.QPushButton("TOP")
    bottomButton = QtWidgets.QPushButton("BOTTOM")
    
    vBox = QtWidgets.QVBoxLayout()
    
    #vBox.addStretch()  --> leaves a stretch gap at the top
    
    vBox.addWidget(topButton)
    #vBox.addStretch()  --> leaves a stretch gap between buttons
    vBox.addWidget(bottomButton)
    
    #vBox.addStretch()  --> leaves a stretch gap at the bottom
    
    window.setLayout(vBox)
    
    window.show()
    
    sys.exit(app.exec_())
    

Window()