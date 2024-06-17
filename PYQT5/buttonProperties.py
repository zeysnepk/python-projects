import sys
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QWidget): #self = QtWidgets.QWidget
    
    def __init__(self):
        
        super().__init__() #runs QtWidgets.QWidget
        
        self.init_gui()
        
    def init_gui(self):
        
        self.text = QtWidgets.QLabel("No Click Yet!")
        self.button = QtWidgets.QPushButton("CLICK")
        self.click_count = 0
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.button)
        v_box.addWidget(self.text)
        v_box.addStretch()
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        self.setLayout(h_box)
        
        self.button.clicked.connect(self.click)
         
        self.setWindowTitle("PYQT5.7")
        
        self.show()
        
    def click(self):
        
        
        self.click_count += 1
        self.text.setText(str(self.click_count) + " click")
        self.text.setAlignment(QtCore.Qt.AlignCenter) #aligns text to the center
        
   

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())