import sys
from PyQt5.QtWidgets import QWidget, QApplication
from options import Ui_Form


class Window(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.adj_list = []
        self.noun_list = []
        self.verb_list = []
        
        for i in self.ui.groupBox_adjective.findChildren(QWidget):
            i.clicked.connect(self.Adj)
            
        for i in self.ui.groupBox_noun.findChildren(QWidget):
            i.clicked.connect(self.Noun)
            
        for i in self.ui.groupBox_verb.findChildren(QWidget):
            i.clicked.connect(self.Verb)
        
        
        
    def Adj(self):
        option = self.sender()
        
        if option.isChecked:
            option_selected = option.text()
            
            if option_selected in self.adj_list:
                self.adj_list.remove(option_selected)
            else:
                self.adj_list.append(option_selected)
            
            
            
        self.adjectives = ", ".join(self.adj_list)
        
        self.ui.label.setText(self.adjectives)
        
    def Noun(self):
        option = self.sender()
        
        if option.isChecked:
            option_selected = option.text()
            self.noun = option_selected
            
        self.adjectives_and_noun = self.adjectives + " " + self.noun
        
        self.ui.label.setText(self.adjectives_and_noun)      
        
    def Verb(self):
        option = self.sender()
        
        if option.isChecked:
            option_selected = option.text()
            option_selected = option_selected.replace("\n","")
            self.verb = option_selected
            
        self.adjectives_noun_verb = self.adjectives + " " + self.noun + " " + self.verb
    
        self.ui.label.setText(self.adjectives_noun_verb)            
            
        
        
        
        
        
        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())