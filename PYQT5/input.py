import sys
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.initGUI()
        
    def initGUI(self):
        
        self.text_user = QtWidgets.QLineEdit()
        self.clear = QtWidgets.QPushButton("CLEAR")
        self.print = QtWidgets.QPushButton("PRINT")
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.text_user)
        v_box.addWidget(self.clear)
        v_box.addWidget(self.print)
        v_box.addStretch()

        self.setLayout(v_box)   
        
        self.clean.clicked.connect(self.click)   
        self.print.clicked.connect(self.click)  
        
        self.show()
        
    def click(self):
        
        sender = self.sender() #sender() function gets data from the clicked location
        
        if sender.text() == "CLEAN":
            self.text_user.clear() #clear() function clears text
            
        else:
            print(self.text_user.text())

        
        
        
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())