import sys
from PyQt5 import QtWidgets, QtGui

def create_window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    
    window.setWindowTitle("PYQT5.2")
    
    label_text = QtWidgets.QLabel(window) #creating a text label in window
    label_text.setText("HELLO WORLD!")
    label_text.move(150,50) #label coordinates
    
    label_image = QtWidgets.QLabel(window) #creating an image label in window
    label_image.setPixmap(QtGui.QPixmap("/Users/zeynepkaplan/Desktop/PythonProjects/PYQT5/Subject.png")) #getting image 
    label_image.move(-87,120)
        
    window.setGeometry(100,100,400,400) 
    window.setFixedSize(400, 400) #setting fixed size
    window.show()
    
    sys.exit(app.exec_())
    

create_window()
