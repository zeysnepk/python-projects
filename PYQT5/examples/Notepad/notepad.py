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


class Menu(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.window = Window()
        self.setCentralWidget(self.window)
        
        self.createMenu()
        
    def createMenu(self):
        
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")
        
        open_file = QtWidgets.QAction("Open", self)
        open_file.setShortcut("Ctrl+O")
        
        save_file = QtWidgets.QAction("Save", self)
        save_file.setShortcut("Ctrl+S")
        
        exitApp = QtWidgets.QAction("Exit", self)
        exitApp.setShortcut("Ctrl+Q")
        
        file_menu.addAction(open_file)
        file_menu.addAction(save_file)
        file_menu.addAction(exitApp)
        
        clear = QtWidgets.QAction("Clear", self)
        clear.setShortcut("Ctrl+D")
        
        edit_menu.addAction(clear)
        
        file_menu.triggered.connect(self.fileClick)
        edit_menu.triggered.connect(self.editClick)
        
        self.show()
        
    def fileClick(self, action):
        
        if action.text() == "Open":
            self.window.open()
            
        elif action.text() == "Save":
            self.window.save()
            
        elif action.text() == "Exit":
            QtWidgets.qApp.quit()
            
    def editClick(self, action):
        
        if action.text() == "Clear":
            self.window.clear()
        
    

app = QtWidgets.QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())