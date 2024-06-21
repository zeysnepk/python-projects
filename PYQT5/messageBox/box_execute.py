#QMessageBox.Ok
#QMessageBox.Open
#QMessageBox.Close
#QMessageBox.Save
#QMessageBox.Cancel
#QMessageBox.Abort
#QMessageBox.Retry
#QMessageBox.Ignore
#QMessageBox.Yes
#QMessageBox.No

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
from box import Ui_Form

class Window(QWidget):
    
    def __init__(self):
        
        
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.pushButton_7.clicked.connect(self.critical)
        self.ui.pushButton_9.clicked.connect(self.warning)
        self.ui.pushButton_10.clicked.connect(self.information)
        self.ui.pushButton_12.clicked.connect(self.question)
        self.ui.pushButton_11.clicked.connect(self.boxDesign)
        self.ui.pushButton_8.clicked.connect(self.about)
        
        
    def critical(self):
        
        QMessageBox.critical(self, "CRITICAL", "Wrong choise!",QMessageBox.Cancel)
        
    def warning(self):
        
        QMessageBox.warning(self, "WARNING", "Far Away...",QMessageBox.Ignore)
        
    def information(self):
        
        QMessageBox.information(self, "INFORMATION", "So Close...",QMessageBox.Ok)
        
    def question(self):
        
        if QMessageBox.question(self, "QUESTION", "Are you still going on?",QMessageBox.Yes, QMessageBox.No) == QMessageBox.No:
            app.exit()
            
    def boxDesign(self):
        
        message = QMessageBox()
        message.setIcon(QMessageBox.Information)
        message.setWindowTitle("Congratulations!!!")
        message.setText("You are one box away :)")
        message.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        message.setEscapeButton(QMessageBox.Yes)
        message.button(QMessageBox.Yes).setText("Keep going on!!!")
        message.button(QMessageBox.No).setText("I'm tired, get out!")
        
        if message.exec_() == QMessageBox.No:
            app.exit()
            
    def about(self):
        
        QMessageBox.about(self,"AWARD","<div align = 'center'><b><font size = '5'> Bravo!!</b></div><br>You did a very good job and found the box.</br>")
        
        
            
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())