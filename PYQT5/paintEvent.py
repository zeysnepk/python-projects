import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor




class Window(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui()
        
    def ui(self):
        
        self.setGeometry(100,100,500,500)
        self.i = 0
        
        #e --> event
    def paintEvent(self ,e): #a ready-made method that rewards every time when the window changes
        self.i += 1 
        self.setWindowTitle(str(self.i))
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255,255,255)) #White RGB color code
        qp.setBrush(QColor(255,182,193)) #Light Pink RGB color code
        qp.drawRect(45,50,400,200)
        qp.end()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
