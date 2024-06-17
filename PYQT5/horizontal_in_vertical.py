import sys
from PyQt5 import QtWidgets, QtGui


def Window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("PYQT5.6")
    window.setGeometry(100,100,400,400)
    
    h_box = QtWidgets.QHBoxLayout()
    v_box = QtWidgets.QVBoxLayout()
    
    okButton = QtWidgets.QPushButton("OKAY")
    canButton = QtWidgets.QPushButton("CANCEL")
    
    h_box.addStretch()
    h_box.addWidget(okButton)
    h_box.addWidget(canButton)
    
    v_box.addStretch()
    v_box.addLayout(h_box)
    
    window.setLayout(v_box)
    
    window.show()
    
    sys.exit(app.exec_())
  
  
Window()