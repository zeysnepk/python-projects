import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        
        menubar = self.menuBar() #creating menu bar
        
        menubar.setNativeMenuBar(False) #must be typed for menu bar to appear on mac
        
        file = menubar.addMenu("File") #adding menu
        edit = menubar.addMenu("Edit")
        
        open_file = QtWidgets.QAction("Open file", self) #defining an action
        open_file.setShortcut("Ctrl+O") #setting shortcut for action
        
        save_file = QtWidgets.QAction("Save file", self)
        save_file.setShortcut("Ctrl+S")
        
        exit_app = QtWidgets.QAction("Exit", self)
        exit_app.setShortcut("Ctrl+Q")
        
        file.addAction(open_file) #adding action to the menu
        file.addAction(save_file)
        file.addAction(exit_app)
        
        search_and_replace = edit.addMenu("Search and Replace") #adding another menu to the menu
        
        search = QtWidgets.QAction("Search", self)
        replace = QtWidgets.QAction("Replace", self)
        
        search_and_replace.addAction(search)
        search_and_replace.addAction(replace)
        
        clear = QtWidgets.QAction("Clear", self)
        
        edit.addAction(clear)
        
        exit_app.triggered.connect(self.exit) #connecting a function when clicked an action
        
        file.triggered.connect(self.response) #connecting a function when clicked any action in a menu
        
        self.setGeometry(100,100,400,400)
        
        self.setWindowTitle("PYQT5.12")
        
        self.show()
        
    def exit(self):
        
        QtWidgets.qApp.quit() #quit the application
        
    def response(self, action):
        
        if action.text() == "Open file":
            print("Clicked 'Open File'.")
            
        if action.text() == "Save file":
            print("Clicked 'Save File'.")
            
        if action.text() == "Exit":
            print("Clicked 'Exit'.")
        
        
        
        
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())