import sys
from PyQt5.QtWidgets import QWidget, QApplication
from messageYou_execute import widgetYou
from messageMe import Ui_Form


class Main(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.you = widgetYou()
        self.you.show()
        
        self.me = Ui_Form()
        self.me.setupUi(self)
        
        self.you.signal.connect(self.connectSlot)
        
        self.me.pushButton_me.clicked.connect(self.sendMessage)
        
    def connectSlot(self, text):
        
        self.me.label_message_you.setText(text)
        
    def sendMessage(self):
        
        message_to_send = self.me.textEdit_from_me.toPlainText()
        self.you.you.label_message_me.setText(message_to_send)
        
    
        
        
app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())