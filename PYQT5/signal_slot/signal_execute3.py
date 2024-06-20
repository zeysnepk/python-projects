
#Sending signals with pyqtSignal

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from signal import Ui_Form
from PyQt5.QtCore import pyqtSignal


class Run2(QWidget):
    
    signal1 = pyqtSignal(int)
    signal2 = pyqtSignal(int)
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    
        self.ui.verticalScrollBar.valueChanged[int].connect(self.signal1[int])
        self.signal1[int].connect(self.signal2[int])
        #...
        self.signal2[int].connect(self.exe)
        
    def exe(self, value):
        self.ui.progressBar.setValue(value)
        
app = QApplication(sys.argv)
run2 = Run2()
run2.show()
sys.exit(app.exec_())
