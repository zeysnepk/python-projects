import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui()
        
    def ui(self):
        
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("keyPressEvent")
        
        label = QLabel("Please move the rectangle with the direction keys!", self)
        label.setGeometry(10,10,500,20)
        label.setAlignment(Qt.AlignHCenter)
        
        self.x = 200
        self.y = 200
        
    def keyPressEvent(self, e):
        print(e.key()) #prints the key that pressed
        
        if e.key() == Qt.Key_Left: #left direction key
            print("Pressed Left Button")
            self.x -= 5
            self.repaint()
            
        if e.key() == Qt.Key_Right: #right direction key
            print("Pressed Right Button")
            self.x += 5
            self.repaint()
            
        if e.key() == Qt.Key_Up: #right direction key
            print("Pressed Up Button")
            self.y -= 5
            self.repaint()
            
        if e.key() == Qt.Key_Down: #right direction key
            print("Pressed Down Button")
            self.y += 5
            self.repaint()
            
        if self.x <= 5:
            self.x = 5
            
        if self.x > self.width() - 45:
            self.x = self.width() - 45 
            
        if self.y <= 5:
            self.y = 5
            
        if self.y > self.height() - 25:
            self.y = self.height() - 25
       
    def paintEvent(self ,e): 

        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255,255,255)) 
        qp.setBrush(QColor(255,182,193)) 
        qp.drawRect(self.x,self.y,40,20)
        qp.end()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
