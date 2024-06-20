import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot
from signal import Ui_Form

class Run(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.verticalScrollBar.valueChanged[int].connect(self.progress) #creating a signal to connect a method when scroll bar's value changed
        
    def progress(self, value):
        
        self.ui.progressBar.setValue(value) #setting the value of progress bar during scroll bar's value changes
        
        
        
        
app = QApplication(sys.argv)
run = Run()
run.show()
sys.exit(app.exec_())