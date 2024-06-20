
from PyQt5.QtWidgets import QWidget
from messageYou import Ui_Form
from PyQt5.QtCore import pyqtSignal


class widgetYou(QWidget):
    
    signal = pyqtSignal(str)
    
    def __init__(self):
        
        super().__init__()
        
        self.you = Ui_Form()
        self.you.setupUi(self)
        
        self.you.pushButton_you.clicked.connect(self.click)
        
    def click(self):
        
        message = self.you.textEdit_from_you.toPlainText()
        self.signal.emit(message)
        
              
