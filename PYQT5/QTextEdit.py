import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.gui()
        
    def gui(self):
        
        self.Qtext = QtWidgets.QTextEdit()
        self.clear = QtWidgets.QPushButton("CLEAR")
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.Qtext)
        v_box.addWidget(self.clear)
        
        self.setLayout(v_box)
        
        self.setWindowTitle("PYQT5.11")
        
        self.clear.clicked.connect(self.click)
        
        self.show()
        
    def click(self):
        
        self.Qtext.clear()
        

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())