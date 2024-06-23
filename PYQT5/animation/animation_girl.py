import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import QTimer
import pictures_rc


class Window(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        self.ui()
        self.timer = QTimer()
        self.timer.timeout.connect(self.time)
        self.timer.start(17)
        
        self.x = 0
        
    def time(self):
        
        
        if self.x > self.width():
            self.x = 0
            
        self.x += 8
            
        self.repaint()
        
        
    def ui(self):
        
        self.setGeometry(10,200,1810,800)
        self.setWindowTitle("Walking Girl")
        self.colorCount
        self.setStyleSheet("border-image: url(:/background/background.jpeg)")
        
    def paintEvent(self, event):
        
        qp = QPainter()
        image = QPixmap(":/girl/girl.png")
        qp.begin(self)
        qp.drawPixmap(self.x, 300, image.width(), image.height(), image)
        qp.end()
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
        