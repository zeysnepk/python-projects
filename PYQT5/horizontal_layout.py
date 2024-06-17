import sys
from PyQt5 import QtWidgets, QtGui

def Window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("PYQT5.4")
    
    window.setGeometry(100,100,400,400)
    
    okayButton = QtWidgets.QPushButton("OKAY")
    cancelButton = QtWidgets.QPushButton("CANCEL")
    
    hBox = QtWidgets.QHBoxLayout()
    
    #hBox.addStretch() --> if written before addWidget(), leans buttons to the right
    
    hBox.addWidget(okayButton)
    #hBox.addStretch()  ---> after okayButton is put, leaves a stretch gap
    hBox.addWidget(cancelButton)
    
    #hBox.addStretch() --> if written after addWidget(), leans buttons to the left
    
    window.setLayout(hBox)
    
    window.show()
    
    
    sys.exit(app.exec_())
    
    
Window()