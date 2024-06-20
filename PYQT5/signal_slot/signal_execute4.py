
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
    
        self.ui.verticalScrollBar.valueChanged[int].connect(self.slot1)
        
        self.signal1.connect(self.slot2)
        #...
        self.signal2.connect(self.execute)
        
    def slot1(self, value):
        
        self.signal1.emit(value)
        
    def slot2(self, value):
        
        self.signal2.emit(value)
        
    #...
    
    def execute(self, value):
        
        self.ui.progressBar.setValue(value)
        
app = QApplication(sys.argv)
run2 = Run2()
run2.show()
sys.exit(app.exec_())
