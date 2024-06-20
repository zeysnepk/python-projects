
#Sending signal with pyqtSlot

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from signal import Ui_Form
from PyQt5.QtCore import pyqtSlot


class Run2(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
    @pyqtSlot(int)
    def on_verticalScrollBar_valueChanged(self, value):
        
        self.ui.progressBar.setValue(value)
        
app = QApplication(sys.argv)
run2 = Run2()
run2.show()
sys.exit(app.exec_())
        
