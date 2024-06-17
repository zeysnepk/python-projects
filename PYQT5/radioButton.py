import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.gui()
        
    def gui(self):
        
        self.clickCount = 3
        self.firstOption = 0
        self.seconOption = 0
        
        self.radioText = QtWidgets.QLabel("Select one to survive:")
        self.labyrinth = QtWidgets.QRadioButton("A labyrinth with no exit.")
        self.hunger = QtWidgets.QRadioButton("A room you'll starve.")
        self.abyss = QtWidgets.QRadioButton("An abyss you hang down with a rope that will break.")
        self.label = QtWidgets.QLabel("")
        self.button = QtWidgets.QPushButton("SEND")
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.radioText)
        v_box.addWidget(self.labyrinth)
        v_box.addWidget(self.hunger)
        v_box.addWidget(self.abyss)
        v_box.addWidget(self.button)
        v_box.addWidget(self.label)
        
        self.setLayout(v_box)
                
        self.setWindowTitle("PYQT5.10")
        
        self.button.clicked.connect(self.click)
        
        self.show()
        
    def click(self):
        
        notClicked = False
        
        if self.clickCount % 3 == 0:
            self.firstOption = 0
            self.secondOption = 0
        
            if self.labyrinth.isChecked():
                self.firstOption = 1
                self.label.setText("You'll die :( Maybe you should try other options")
                
            elif self.hunger.isChecked():
                self.firstOption = 2
                self.label.setText("You'll die :( Maybe you should try other options")
                
            elif self.abyss.isChecked():
                self.firstOption = 3
                self.label.setText("You'll die :( Maybe you should try other options")
                
            else:
                self.label.setText("Please select one of the above!")
                notClicked = True
                
        elif self.clickCount % 3 == 1:
            if self.firstOption == 1:
                if self.labyrinth.isChecked():
                    self.label.setText("You're already dead!!!")
                    notClicked = True
                
                elif self.hunger.isChecked():
                    self.secondOption = 2
                    self.label.setText("You'll die again:( Maybe you should try the third option")
                
                elif self.abyss.isChecked():
                    self.secondOption = 3
                    self.label.setText("You'll die again:( Maybe you should try the second option")
                
                else:
                    self.label.setText("Please select one of the above!")
                    notClicked = True
                    
            elif self.firstOption == 2:
                if self.labyrinth.isChecked():
                    self.secondOption = 1
                    self.label.setText("You'll die again:( Maybe you should try the third option")
                
                elif self.hunger.isChecked():
                    self.label.setText("You're already dead!!!")
                    notClicked = True
                
                elif self.abyss.isChecked():
                    self.secondOption = 3
                    self.label.setText("You'll die again:( Maybe you should try the first option")
                
                else:
                    self.label.setText("Please select one of the above!")
                    notClicked = True
                    
            elif self.firstOption == 3:
                if self.labyrinth.isChecked():
                    self.secondOption = 1
                    self.label.setText("You'll die again:( Maybe you should try the second option")
                
                elif self.hunger.isChecked():
                    self.secondOption = 2
                    self.label.setText("You'll die again:( Maybe you should try the first option")
                
                elif self.abyss.isChecked():
                    self.label.setText("You're already dead!!!")
                    notClicked = True
                
                else:
                    self.label.setText("Please select one of the above!")
                    notClicked = True
                    
        elif self.clickCount % 3 == 2:
            if self.firstOption == 1:
                if self.secondOption == 2:
                    if self.labyrinth.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.hunger.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.abyss.isChecked():
                        self.label.setText("You'll die again :) You have 0 chance")
                        
                    else:
                        self.label.setText("Please select one of the above!")
                        notClicked = True
                        
                elif self.secondOption == 3:
                    if self.labyrinth.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.hunger.isChecked():
                        self.label.setText("You'll die again :) You have 0 chance")
                        
                        
                    elif self.abyss.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    else:
                        self.label.setText("Please select one of the above!")
                        notClicked = True
            
            elif self.firstOption == 2:
                if self.secondOption == 1:
                    if self.labyrinth.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.hunger.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.abyss.isChecked():
                        self.label.setText("You'll die again :) You have 0 chance")
                        
                    else:
                        self.label.setText("Please select one of the above!")
                        notClicked = True
                        
                elif self.secondOption == 3:
                    if self.labyrinth.isChecked():
                        self.label.setText("You'll die again :) You have 0 chance")
                        
                    elif self.hunger.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.abyss.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    else:
                        self.label.setText("Please select one of the above!")
                        notClicked = True
                        
            elif self.firstOption == 3:
                if self.secondOption == 1:
                    if self.labyrinth.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.hunger.isChecked():
                        self.label.setText("You'll die again :) You have 0 chance")
                        
                    elif self.abyss.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    else:
                        self.label.setText("Please select one of the above!")
                        notClicked = True
                        
                elif self.secondOption == 2:
                    if self.labyrinth.isChecked():
                        self.label.setText("You'll die again :) You have 0 chance")
                        
                    elif self.hunger.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    elif self.abyss.isChecked():
                        self.label.setText("You were already dead in your choices!")
                        notClicked = True
                        
                    else:
                        self.label.setText("Please select one of the above!")
                        notClicked = True
            
            
        if notClicked:
            self.clickCount -= 1
                
        self.clickCount += 1
                
        

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_()) 
        