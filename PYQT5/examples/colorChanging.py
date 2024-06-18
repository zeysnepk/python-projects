import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.gui()
        
    def gui(self):
        
        labelText = QtWidgets.QLabel("SELECT COLOR")
        
        red = QtWidgets.QRadioButton("Red")
        blue = QtWidgets.QRadioButton("Blue")
        yellow = QtWidgets.QRadioButton("Yellow")
        purple = QtWidgets.QRadioButton("Purple")
        
        self.labelColor = QtWidgets.QLabel("")
        self.labelColor.setFixedHeight(100)
        
        button = QtWidgets.QPushButton("SEND")
        
        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        
        v_box.addStretch()
        v_box.addWidget(labelText)
        v_box.addWidget(red)
        v_box.addWidget(blue)
        v_box.addWidget(yellow)
        v_box.addWidget(purple)
        v_box.addWidget(self.labelColor)
        v_box.addWidget(button)
        v_box.addStretch()
        
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        self.setLayout(h_box)
        
        
        self.setWindowTitle("COLORS")
        
        button.clicked.connect(lambda : self.click(red.isChecked(), blue.isChecked(), yellow.isChecked(), purple.isChecked()))
        
        self.show()
        
    def click(self, red, blue, yellow, purple):
        
        self.labelColor.setText("")
         
        if red:
            self.labelColor.setStyleSheet("background-color: red;")
            
        elif blue:
            self.labelColor.setStyleSheet("background-color: blue;")
            
        elif yellow:
            self.labelColor.setStyleSheet("background-color: yellow;")
            
        elif purple:
            self.labelColor.setStyleSheet("background-color: purple;")
            
        else:
            self.labelColor.setText("Please select a color!")
            
        
        
        
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())
