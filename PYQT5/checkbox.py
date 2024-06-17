import sys
from PyQt5 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.gui()
        
    def gui(self):
        
        self.checkbox = QtWidgets.QCheckBox("Do you love me?")
        self.button = QtWidgets.QPushButton("SEND")
        self.text = QtWidgets.QLabel("")
        
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.text)
        v_box.addWidget(self.button)
        
        self.setLayout(v_box)
        
        self.setWindowTitle("PYQT5.9")
        
        self.button.clicked.connect(self.click)
        
        self.show()
        
    def click(self):
        
        if (self.checkbox.isChecked()):
            self.text.setText("I love you too")
            
        else:
            self.text.setText("Maybe in another universe...")
            
        
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())