import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from animals import Ui_MainWindow



class Window(QMainWindow):
    
    time = 2000
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.actionBlue.setCheckable(True)
        self.ui.actionGreen.setCheckable(True)
        self.ui.actionPurple.setCheckable(True)
        self.ui.actionRed.setCheckable(True)
        
        self.ui.actionBlue.toggled[bool].connect(self.Blue)
        self.ui.actionGreen.toggled[bool].connect(self.Green)
        self.ui.actionPurple.toggled[bool].connect(self.Purple)
        self.ui.actionRed.toggled[bool].connect(self.Red)
        
        
    def home(self):
        
        self.ui.frame.setStyleSheet("image: url(:/home/Martin-Berube-Flat-Animal-Turtle.256.png);")
        self.ui.statusbar.setStyleSheet("color : black; background-color: white")
        self.ui.statusbar.showMessage("TURTLE!", self.time)
            
    def set_checked_false(self, sended_color):
        
        colors = [self.ui.actionGreen, self.ui.actionBlue, self.ui.actionPurple, self.ui.actionRed]
        
        for color in colors:
            if color != sended_color:
                color.setChecked(False)
            
    
    def Green(self, state):
        
        self.set_checked_false(self.ui.actionGreen)
        self.ui.statusbar.showMessage("Green color has been selected!", self.time)
        self.ui.statusbar.setStyleSheet("color: green; background-color: white")
        
        if state == True:
            self.ui.frame.setStyleSheet("image: url(:/green/Martin-Berube-Flat-Animal-Frog.256.png);")
        
        else:
            self.home()
        
    def Purple(self, state):
        
        self.set_checked_false(self.ui.actionPurple)
        self.ui.statusbar.showMessage("Purple color has been selected!", self.time)
        self.ui.statusbar.setStyleSheet("color: purple; background-color: white")
        
        if state == True:
            self.ui.frame.setStyleSheet("image: url(:/purple/Martin-Berube-Flat-Animal-Squid.256.png);")   
        
        else:
            self.home()
            
    def Red(self, state):
        
        self.set_checked_false(self.ui.actionRed)
        self.ui.statusbar.showMessage("Red color has been selected!", self.time)
        self.ui.statusbar.setStyleSheet("color : red; background-color: white")
        
        if state == True:
            self.ui.frame.setStyleSheet("image: url(:/red/Martin-Berube-Flat-Animal-Crab.256.png);")   
        
        else:
            self.home()

    def Blue(self, state):
        
        self.set_checked_false(self.ui.actionBlue)
        
        if state == True:
            self.ui.frame.setStyleSheet("image: url(:/blue/Martin-Berube-Flat-Animal-Bird.256.png);")
            self.ui.statusbar.setStyleSheet("color : blue; background-color: white")
            self.ui.statusbar.showMessage("Blue color has been selected!", self.time)
        
        else:
            self.home()

        
                 
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
