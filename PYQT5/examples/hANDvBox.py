import sys
from PyQt5 import QtWidgets, QtGui


def Window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("PYQTe1.0")
    window.setGeometry(100,100,400,400)
    
    h_box = QtWidgets.QHBoxLayout()
    v_box = QtWidgets.QVBoxLayout()
    
    redButton = QtWidgets.QPushButton("RED")
    blueButton = QtWidgets.QPushButton("BLUE")
    
    h_box.addWidget(redButton)
    h_box.addStretch()
    h_box.addWidget(blueButton)
    
    okayButton = QtWidgets.QPushButton("OKAY")
    cancelButton = QtWidgets.QPushButton("CANCEL")
    
    v_box.addLayout(h_box)
    v_box.addStretch()
    v_box.addWidget(okayButton)
    v_box.addStretch()
    v_box.addWidget(cancelButton)
    
    window.setLayout(v_box)
    
    window.show()
    
    sys.exit(app.exec_())
    
    
Window()
    
    