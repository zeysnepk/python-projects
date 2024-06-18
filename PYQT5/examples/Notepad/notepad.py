import sys
import os
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.gui()
        
    def gui(self):
        
        self.text = QtWidgets.QTextEdit()
        
        self.clear_button = QtWidgets.QPushButton("Clear")
        self.open_button = QtWidgets.QPushButton("Open")
        self.save_button = QtWidgets.QPushButton("Save")
        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addWidget(self.clear_button)
        h_box.addWidget(self.open_button)
        h_box.addWidget(self.save_button)
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.text)
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        
        self.setWindowTitle("Notepad")
        
        self.clear_button.clicked.connect(self.clear)
        self.open_button.clicked.connect(self.open)
        self.save_button.clicked.connect(self.save)
        
        self.show()
        
    def clear(self):
        
        self.text.clear()
        
    def open(self):
        
        file_path = QtWidgets.QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        
        with open (file_path[0], "r") as file:
            self.text.setText(file.read())
        
    def save(self):
        
        file_path = QtWidgets.QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
        
        with open (file_path[0], "w") as file:
            file.write(self.text.toPlainText())

        

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())